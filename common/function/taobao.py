

from auto_interface.common.key_word.request_method import RequestMethod
from auto_interface.common.util.ini_driver import load_ini
import allure


class Taobao(object):
    # 测试QQ等级的接口

    def taobao_picture(self, taobaodata):
        # 初始化，api常见的请求
        tp = RequestMethod()
        url = load_ini('/Users/liuyuanyuan/python/auto_interface/conf/api_url.ini', 'Api')
        url_taobao_picture = url[3][1]
        params_taobao_picture = {
            'sort': taobaodata['Params']['sort'],
            'format': taobaodata['Params']['format']
        }
        result_taobao = {
            'Status': taobaodata['Params']['Status']
        }

        with allure.step("get请求响应信息"):
            res_taobao_get = tp.get(url=url_taobao_picture, params=params_taobao_picture)
            assert res_taobao_get.status_code == result_taobao['Status']


        with allure.step("post请求响应信息"):
            res_taobao_post = tp.post(url=url_taobao_picture, data=params_taobao_picture)
            assert res_taobao_post.status_code == result_taobao['Status']
