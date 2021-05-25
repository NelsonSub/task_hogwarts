# -*- coding:UTF-8 -*-
from tenth_work.api.wework_api import WeWork


class User(WeWork):

    def create(self, userid, name, department, mobile=None, email=None):
        body = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile,
            "email": email
        }
        data = {
            "url": "/cgi-bin/user/create",
            "method": "post",
            "params": {"access_token": self.token},
            "json": body
        }
        return self.request(data)

    def get(self, userid):
        data = {
            "url": "/cgi-bin/user/get",
            "method": "get",
            "params": {"access_token": self.token, "userid": userid},
            "json": {
            }
        }
        return self.request(data)
    def delete(self,userid):
        data = {
            "url": "/cgi-bin/user/delete",
            "method": "get",
            "params": {"access_token": self.token, "userid": userid},
            "json": {
            }
        }
        return self.request(data)