# -*- coding:UTF-8 -*-
import json
import configparser

import requests as requests


def get_token():
    config = configparser.ConfigParser()
    conf_path = "../test.ini"

    config.read(conf_path)
    corpid = config.get('corp', 'corpid')
    corpsecret = config.get('corp', 'corpsecret')
    r = requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        params={
            "corpid": corpid,
            "corpsecret": corpsecret
        }
    )
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.status_code == 200
    return r


