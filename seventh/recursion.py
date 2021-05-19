# -*- coding:UTF-8 -*-
import json

import mitmproxy.http
from mitmproxy import http
from mitmproxy import ctx


class Events:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if 'stock.xueqiu.com/v5/stock/batch/quote.json' in flow.request.url and \
                '_s' in flow.request.url:
            base_data = json.loads(flow.response.text)
            new_data = self.recursion(base_data, 2)
            # 这步返回给客户端
            flow.response.text = json.dumps(new_data)

    def recursion(self, data, init_data=1):
        '''
        :param data 原始数据
        :param init_data: 数据翻倍的倍数，默认1倍
        :return: 在原始数据中的float类型翻倍后的数据
        '''

        if isinstance(data, dict):
            for k, v in data.items():
                data[k] = self.recursion(v, init_data)

        elif isinstance(data, list):
            new_data = []
            # for i in data:
            #     new_data.append(self.recursion(i,init_data))
            # data = new_data
            data = [self.recursion(i, init_data) for i in data]
        elif isinstance(data, float):
            data = data * init_data
        else:
            data = data

        return data


addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    mitmdump(['-p', '8080', "-s", __file__])
