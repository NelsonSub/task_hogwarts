# -*- coding:UTF-8 -*-
import configparser


def loadConfig(secs,key):
    config = configparser.ConfigParser()
    conf_path = "../config/test.ini"

    config.read(conf_path)
    data = config.get(secs, key)
    return data



