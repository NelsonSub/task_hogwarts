# -*- coding:UTF-8 -*-
import json

import requests


def get_corp_tag_list(token):
    param = {"access_token": token}
    data = {}
    print(data)
    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        params=param,
        json=data
    )
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    return r
