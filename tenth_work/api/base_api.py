# -*- coding:UTF-8 -*-
import logging

import requests
import json
from tenth_work.common.config import loadConfig

class BaseApi:

    def request(self, request: dict):
        protocol = request.get("protocol")

        if protocol is None or protocol == 'http':
            return self.http_request(request)
        else:
            logging.info(f"目前不支持{protocol}协议类型接口测试")
            return

    def http_request(self, data):
        if 'http' not in data.get('url'):

            base_url = data.get('base_url')
            if base_url:
                url = base_url + data.get('url')
                data["url"] = url
                data.pop('base_url')
            else:
                base_url = loadConfig('common','base_url')
                url = base_url + data.get('url')
                data["url"] = url
        print(data)
        r = requests.request(**data)
        request_data = {
            "url": r.request.url,
            "header": dict(r.request.headers),
            "method": r.request.method,
        }
        if r.request.body:
            request_data['data'] = json.dumps(r.request.body.decode('unicode_escape'))
        response_data = {
            "status_code": r.status_code,
            "header": dict(r.request.headers),
            "data": r.json()
        }
        logging.info(f'接口请求为： {json.dumps(request_data, indent=2, ensure_ascii=False)}')
        logging.info(f'接口响应为： {json.dumps(response_data, indent=2, ensure_ascii=False)}')
        return response_data
