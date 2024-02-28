# Orderly Network Trader

## Getting Started
It is recommended that you use a virtual environment to install the dependencies. The code has specifically been tested on Python 3.11.4.

```python
virtualenv -p python3 .venv
source .venv/bin/activate
```
Then, install the dependencies for the Python SDK

pip install -r requirements.txt

## 参数获取
以logx为例，进入账户页面，选择API Keys，复制三个值：Account，Orderly API Key和Orderly API Secret。
其中Orderly API KEY和Orderly API Secret需要将冒号前面的值去掉（包括冒号），举个例子：
Orderly API Secret：ed25519:fdajfdfjadjal1e13212123
则，最终需要填入脚本中的值为fdajfdfjadjal1e13212123
Orderly API Key类似。

## NEAR
TODO