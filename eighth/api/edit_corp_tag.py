# -*- coding:UTF-8 -*-
import json

import requests


def edit_corp_tag(token,type_id,name):
    param = {"access_token": token}
    data = {'id': type_id,'name':name}
    print(data)
    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
        params=param,
        json=data
    )
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    return r
