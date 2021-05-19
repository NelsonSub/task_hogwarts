# -*- coding:UTF-8 -*-

import json

import mitmproxy.http
from mitmproxy import http
from mitmproxy import ctx


class Events:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if 'stock.xueqiu.com/v5/stock/batch/quote.json' in flow.request.url and \
                '_s' in flow.request.url:
            flow.response = http.HTTPResponse.make(
                200,
                open('quote.json', encoding='utf-8').read()
            )


addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    mitmdump(['-p', '8080', "-s", __file__])
