#!/usr/bin/env python3
"""Audit a text file of IP addresses and export a CSV report.

Input format: one IPv4 or IPv6 address per line. Blank lines and # comments
are ignored. This tool performs local syntax/scope checks only; it does not
identify residential, mobile, ISP, or datacenter ownership.
"""
from __future__ import annotations

import argparse
import csv
import ipaddress
import sys
from pathlib import Path


def classify(address: ipaddress.IPv4Address | ipaddress.IPv6Address) -> str:
    if address.is_unspecified:
        return "unspecified"
    if address.is_loopback:
        return "loopback"
    if address.is_link_local:
        return "link_local"
    if address.is_multicast:
        return "multicast"
    if address.is_private:
        return "private_or_local"
    if address.is_global:
        return "global"
    return "reserved_or_special"


def audit(input_path: Path, output_path: Path) -> tuple[int, int, int]:
    if input_path.resolve() == output_path.resolve():
        raise ValueError("输出文件不能覆盖输入文件。")
    seen: dict[str, int] = {}
    rows: list[dict[str, str | int]] = []
    valid = invalid = duplicates = 0

    with input_path.open("r", encoding="utf-8-sig") as source:
        for line_number, raw_line in enumerate(source, start=1):
            candidate = raw_line.split("#", 1)[0].strip()
            if not candidate:
                continue
            try:
                address = ipaddress.ip_address(candidate)
                normalized = str(address)
                duplicate_of = seen.get(normalized)
                if duplicate_of is None:
                    seen[normalized] = line_number
                    status = "valid"
                    duplicates_field = ""
                else:
                    status = "duplicate"
                    duplicates_field = str(duplicate_of)
                    duplicates += 1
                valid += 1
                rows.append({
                    "line_number": line_number,
                    "input": candidate,
                    "normalized_ip": normalized,
                    "ip_version": address.version,
                    "classification": classify(address),
                    "status": status,
                    "duplicate_of_line": duplicates_field,
                })
            except ValueError:
                invalid += 1
                rows.append({
                    "line_number": line_number,
                    "input": candidate,
                    "normalized_ip": "",
                    "ip_version": "",
                    "classification": "unknown",
                    "status": "invalid",
                    "duplicate_of_line": "",
                })

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "line_number", "input", "normalized_ip", "ip_version",
        "classification", "status", "duplicate_of_line",
    ]
    with output_path.open("w", encoding="utf-8-sig", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return valid, invalid, duplicates


def main() -> int:
    parser = argparse.ArgumentParser(
        description="检查 IP 列表格式、地址范围类别和重复项，并导出 CSV。"
    )
    parser.add_argument("input", type=Path, help="输入文本文件：每行一个 IPv4 或 IPv6")
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("ip-audit-report.csv"),
        help="CSV 报告路径（默认：ip-audit-report.csv）",
    )
    args = parser.parse_args()

    if not args.input.is_file():
        print(f"输入文件不存在：{args.input}", file=sys.stderr)
        return 2

    try:
        valid, invalid, duplicates = audit(args.input, args.output)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"处理失败：{exc}", file=sys.stderr)
        return 2

    print(f"有效地址记录：{valid}")
    print(f"无效记录：{invalid}")
    print(f"重复记录：{duplicates}")
    print(f"CSV 报告：{args.output}")
    print("注意：global 仅表示地址范围分类，不代表住宅 IP 或 IP 信誉。")
    return 1 if invalid else 0


if __name__ == "__main__":
    raise SystemExit(main())
