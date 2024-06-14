import allure
from auto_interface.common.key_word.request_method import RequestMethod
from auto_interface.common.util.ini_driver import load_ini


class BaiDu(object):
    # 登录逻辑
    def baidu_login(self, baidudata):
        # 动态获取参数生成标题
        # allure.dynamic.title(userdata['title'])
        # 初始化工具类
        bl = RequestMethod()
        # 请求接口
        Baidu_Login_Data = load_ini('/Users/liuyuanyuan/python/auto_interface/conf/api_url.ini', 'Api')
        url = Baidu_Login_Data[0][1]
        # 请求参数
        parama_baidulogin = {
            'method': baidudata['Params']['method'],
            'callback': baidudata['Params']['callback']
        }
        result_qq_baidulogin = {
            'Status': baidudata['Params']['Status']
        }


        with allure.step("get接口请求响应信息"):
            res_baidu_get = bl.get(url=url, json=parama_baidulogin)
            assert res_baidu_get.status_code == result_qq_baidulogin['Status']


        with allure.step("post接口请求响应信息"):
            res_baidu_post = bl.post(url=url, data=parama_baidulogin)
            assert res_baidu_post.status_code == result_qq_baidulogin['Status']
            # print(res_baidu_post.status_code)


