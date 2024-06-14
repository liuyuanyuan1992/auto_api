

from auto_interface.common.key_word.request_method import RequestMethod
from auto_interface.common.util.ini_driver import load_ini
import allure


class QQ(object):
    # 测试QQ等级的接口

    def qq_level(self, qqdata):
        # 初始化，api常见的请求
        ql = RequestMethod()
        url = load_ini('/Users/liuyuanyuan/python/auto_interface/conf/api_url.ini', 'Api')
        url_qq = url[1][1]
        params_qq = {
            'qq': qqdata['Params']['qq'],
            'skey': qqdata['Params']['skey']
        }
        result_qq = {
            'Status': qqdata['Params']['Status']
        }

        with allure.step("get请求响应信息"):
            res_qq_get = ql.get(url=url_qq, params=params_qq)
            assert res_qq_get.status_code == result_qq['Status']
            # print(res_qq_get.status_code, result_qq['Status'])
            # print(type(res_qq_get.status_code), type(result_qq['Status']))


        with allure.step("post请求响应信息"):
            res_qq_post = ql.post(url=url_qq, data=params_qq)
            assert res_qq_post.status_code == result_qq['Status']
            # print(res_qq_post.status_code)


    def qq_talk(self, qqtalkdata):
        # 初始化，api常见的请求
        qt = RequestMethod()
        url = load_ini('/Users/liuyuanyuan/python/auto_interface/conf/api_url.ini', 'Api')
        url_qqtalk = url[5][1]
        params_qqtalk = {
            'qq': qqtalkdata['Params']['qq']
        }
        result_qqtalk = {
            'Status': qqtalkdata['Params']['Status']
        }

        with allure.step("get请求响应信息"):
            res_qqtalk_get = qt.get(url=url_qqtalk, params=params_qqtalk)
            assert res_qqtalk_get.status_code == result_qqtalk['Status']
            # print(res_qq_get.status_code, result_qq['Status'])
            # print(type(res_qq_get.status_code), type(result_qq['Status']))


        with allure.step("post请求响应信息"):
            res_qqtalk_post = qt.post(url=url_qqtalk, data=params_qqtalk)
            assert res_qqtalk_post.status_code == result_qqtalk['Status']
            # print(res_qq_post.status_code)