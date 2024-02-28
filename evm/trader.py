import time

from evm import OrderlyNetworkClient


if __name__ == '__main__':
    # 从logx网站上，右上角钱包地址中的API KEYS获取
    orderly_account_id = "" # Account
    # Orderly API Secret，取冒号后面的值（即，去掉ed25519:）
    orderly_api_secret = ""
    # Orderly API Key 取冒号后面的值（即，去掉ed25519:）
    orderly_api_key = ""
    # order api secret
    client = OrderlyNetworkClient(orderly_account_id, orderly_api_secret)

    # eth合约，做多时，side=BUY，做空时，side=SELL
    # btc合约，symbol=PERP_BTC_USDC
    symbol = 'PERP_ETH_USDC'
    while True:
        client.create_market_order(symbol, quantity=0.05, side='SELL')
        client.close_positions()
        # 休眠3秒
        time.sleep(3)


