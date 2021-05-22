# -*- coding:UTF-8 -*-
import json

import requests


def del_corp_tag(token, tag_id):
    r = requests.post(
        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
        params={"access_token": token},
        json={
            "tag_id": tag_id
        }
    )
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    return r
