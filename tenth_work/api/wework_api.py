# -*- coding:UTF-8 -*-



from tenth_work.api.base_api import BaseApi
from tenth_work.common.config import loadConfig


class WeWork(BaseApi):
    token = None

    def get_token(self,key):
        corpid = loadConfig(key, 'corpid')
        corpsecret = loadConfig(key, 'corpsecret')

        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            'method': 'get',
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }

        result = self.request(data)
        assert result['status_code'] == 200
        self.token = result['data']['access_token']



