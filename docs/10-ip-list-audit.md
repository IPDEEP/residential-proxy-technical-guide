# IP List Audit Tool：批量 IP 地址检查

## 工具用途

`ip-list-audit.py` 用于在本地检查 IP 地址列表，识别：

- IPv4 / IPv6 格式是否有效；
- 地址属于本地、回环、链路本地、多播、保留或 global 等范围类别；
- 列表中是否存在重复地址；
- 将检查结果导出为 CSV，便于后续人工整理。

**重要边界：** 该工具只使用 Python 标准库的 `ipaddress` 模块，不查询第三方数据库。它不能识别 IP 是否属于住宅网络、移动网络、ISP 或数据中心，也不能判断 IP 信誉、纯净度或平台接受情况。global 地址不等于住宅 IP。

## 环境要求

- Python 3.10 或更高版本；
- 无需安装第三方依赖；
- 输入文件采用 UTF-8 编码，每行一个 IPv4 或 IPv6 地址；
- 空行和 `#` 注释会被忽略。

## 输入示例

创建 `ips.txt`：

```text
# 示例地址，仅用于演示
192.0.2.10
2001:db8::10
192.0.2.10
not-an-ip
```

以上地址来自文档示例网段，不是可用于实际业务的代理出口。

## 运行方式

在仓库根目录执行：

```bash
python examples/ip-list-audit.py ips.txt
```

指定输出文件：

```bash
python examples/ip-list-audit.py ips.txt --output reports/ip-audit.csv
```

## CSV 字段

| 字段 | 说明 |
|---|---|
| line_number | 输入文件行号 |
| input | 原始输入内容 |
| normalized_ip | 标准化后的 IP 地址 |
| ip_version | IPv4 或 IPv6 版本号 |
| classification | 本地地址范围类别 |
| status | valid、duplicate 或 invalid |
| duplicate_of_line | 首次出现该地址的行号 |

## 结果解释

- `global`：Python 地址库判断为全局可路由范围；不代表住宅属性。
- `private_or_local`：私有或本地地址范围。
- `reserved_or_special`：特殊用途或保留范围。
- `loopback`、`link_local`、`multicast`、`unspecified`：对应特殊地址类型。
- `duplicate`：该地址此前已出现。
- `invalid`：无法按 IPv4 或 IPv6 地址解析。

地址范围判断依赖当前 Python 运行时内置的标准库数据，特殊地址分类可能随 Python 版本更新而调整。

## 隐私与安全

工具在本机读取输入文件并生成 CSV，不会主动联网或上传列表。输入文件和输出报告可能包含业务 IP 清单，请按内部数据管理要求保存，不要将敏感清单提交到公开仓库。

## 相关资源

- [ToDetect IP 地址查询](https://www.todetect.net/ip/)：需要进一步查看单个 IP 的公开检测信息时，可使用 IP 查询工具。检测结果应结合数据源和更新时间理解。
- [住宅代理 IP 技术知识库](../README.md)：了解住宅 IP、ASN、ISP 与 IP 分类的区别。
