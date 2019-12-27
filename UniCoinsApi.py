import requests


class UniApi(object):
    def __init__(self, token, key, merchant_id):
        self.token = token
        self.key = key
        self.id = merchant_id

    def get_balance(self):
        return requests.post('https://uc.simbrex.com/api/merchant/getBalance.php',
                             {'merchant_id': self.id,
                              'key': self.key}).json()['balance']

    def link_pay(self, coins=0):
        return f'vk.com/app7037638#pay_{self.id}_{coins}_{22222222}'

    def send_pay(self, to, coins, code=22222222):
        return requests.post('https://uc.simbrex.com/api/merchant/transfer.php',
                             {'merchant_id': self.id,
                              'key': self.key,
                              'to': to,
                              'sum': coins,
                              'code': code}).text

    def get_history(self, count=100, offset=10):
        return requests.post('https://uc.simbrex.com/api/merchant/getHistory.php',
                             {'merchant_id': self.id,
                              'key': self.key,
                              'count': count,
                              'offset': offset}).json()['history']


