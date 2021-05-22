# -*- coding:UTF-8 -*-
import json

import requests


def add_corp_tag(token, tag_name, group_name):
    param = {"access_token": token}
    data = {
            "group_name": group_name,
            "tag": [
                {
                    "name": tag_name,
                }
            ]
        }
    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
        params=param,
        json=data
    )
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    return r
