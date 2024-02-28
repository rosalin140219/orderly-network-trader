import json

from base58 import b58decode
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from requests import Request, Session

from signer import Signer
from loguru import logger


class OrderlyNetworkClient:
    def __init__(
            self,
            orderly_account_id="",
            orderly_api_secret="",
            orderly_api_key="",
    ):
        self.orderly_account_id = orderly_account_id
        self.orderly_api_secret = orderly_api_secret
        self.orderly_api_key = orderly_api_key
        self.base_url = "https://api-evm.orderly.org"

    '''
    市价下单
    '''
    def create_market_order(self, symbol, quantity, side):
        key = b58decode(self.orderly_api_secret)
        # order api key
        orderly_key = Ed25519PrivateKey.from_private_bytes(key)
        signer = Signer(self.orderly_account_id, orderly_key)
        req = signer.sign_request(
            Request(
                "POST",
                "%s/v1/order" % self.base_url,
                json={
                    "symbol": symbol,
                    "order_type": "MARKET",
                    "order_quantity": quantity,
                    "side": side,
                },
            )
        )
        session = Session()
        res = session.send(req)
        response = json.loads(res.text)
        logger.info(f"市价下单响应结果:{response}")
        return response

    '''
    获取当前用户仓位
    '''
    def get_positions(self):
        key = b58decode(self.orderly_api_secret)
        # order api key
        orderly_key = Ed25519PrivateKey.from_private_bytes(key)
        signer = Signer(self.orderly_account_id, orderly_key)
        req = signer.sign_request(
            Request(
                "GET",
                "%s/v1/positions" % self.base_url
            )
        )
        session = Session()
        res = session.send(req)
        response = json.loads(res.text)
        logger.info(f"获取当前用户的仓位，响应结果:{response}")
        result = response['success']
        if result:
            data = response['data']
            return data['rows']

    '''
    关闭当前账户的仓位
    '''
    def close_positions(self):
        positions = self.get_positions()
        if positions:
            for position in positions:
                symbol = position['symbol']
                quantity = position['position_qty']
                if quantity == 0:
                    continue
                else:
                    side = 'SELL' if quantity > 0 else 'BUY'
                    quantity = -quantity if quantity < 0 else quantity
                    close_info = self.create_market_order(symbol, quantity, side)
                    logger.info(f"关闭仓位，响应结果{close_info}")
        else:
            logger.info(f"当前账户的仓位为空，跳过，不处理")