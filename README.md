# CDN 下载器

一键下载文件by cdn

help:

```shell
cdn-dl -h
usage: cdn-dl [-h] -u URL -o OUT [-ua USE_AGENT] cdn

cdn-dl 下载配置

positional arguments:
  cdn                   cdn config配置, eg: 1.2.3.4:443

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     文件下载url
  -o OUT, --out OUT     文件下载路径
  -ua USE_AGENT, --use_agent USE_AGENT
                        是否使用user agent
```

eg:

```shell
cdn-dl -u https://download.docker.com/linux/static/stable/x86_64/docker-27.2.1.tgz -o test.tgz 1.1.1.1:443
```
