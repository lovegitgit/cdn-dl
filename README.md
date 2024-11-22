# CDN 下载器

一键下载文件by cdn

help:

```shell
usage: cdn-dl [-h] -u URL -o OUT [-ua USE_AGENT] [-ts TRUNK_SIZE] [-t TIMEOUT] [-r RETRY] [-d] cdn [cdn ...]

cdn-dl 下载配置

positional arguments:
  cdn                   cdn configs配置,支持ip| ip:port |ip:port:host 字串或文本或host文件

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     文件下载url
  -o OUT, --out OUT     文件下载路径
  -ua USE_AGENT, --use_agent USE_AGENT
                        是否使用user agent
  -ts TRUNK_SIZE, --trunk_size TRUNK_SIZE
                        下载使用的trunk size, 默认8192
  -t TIMEOUT, --timeout TIMEOUT
                        下载请求超时时间, 默认10s
  -r RETRY, --retry RETRY
                        下载请求重试次数, 默认3
  -d, --debug           是否打印调试信息
```

eg:

```shell
cdn-dl -u https://download.docker.com/linux/static/stable/x86_64/docker-27.2.1.tgz -o test.tgz 1.1.1.1:443
```
