import allure
import requests

# 定义一个关键字类
class RequestMethod():
    # 将get请求行为进行封装
    def get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    # 将post请求行为进行封装
    def post(self, url, data=None, **kwargs):
        return requests.post(url=url, data=data, **kwargs)