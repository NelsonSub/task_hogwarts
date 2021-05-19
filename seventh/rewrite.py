# -*- coding:UTF-8 -*-
import json

import mitmproxy.http

from mitmproxy import ctx
class Events:

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if 'stock.xueqiu.com/v5/stock/batch/quote.json' in flow.request.url and \
                '_s' in flow.request.url:
            response_data = json.loads(flow.response.text)
            response_data['data']['items'][0]['quote']['percent'] = 0
            response_data['data']['items'][1]['quote']['percent'] = -0.01
            response_data['data']['items'][2]['quote']['percent'] = 0.01
            flow.response.text = json.dumps(response_data)


addons = [
    Events()
]

if __name__ == '__main__':

    from mitmproxy.tools.main import mitmdump

    mitmdump(['-p', '8080', "-s", __file__])
