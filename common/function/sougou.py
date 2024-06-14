from auto_interface.common.key_word.request_method import RequestMethod
from auto_interface.common.util.ini_driver import load_ini
import allure


class SouGou(object):
    # 测试QQ等级的接口

    def sougou_collection(self, sougoudata):
        # 初始化，api常见的请求
        tp = RequestMethod()
        url = load_ini('/Users/liuyuanyuan/python/auto_interface/conf/api_url.ini', 'Api')
        url_sougou_collection = url[4][1]
        params_sougou_collection = {
            'url': sougoudata['Params']['url']
        }
        result_sougou = {
            'Status': sougoudata['Params']['Status']
        }

        with allure.step("get请求响应信息"):
            res_sougou_get = tp.get(url=url_sougou_collection, params=params_sougou_collection)
            assert res_sougou_get.status_code == result_sougou['Status']


        with allure.step("post请求响应信息"):
            res_sougou_post = tp.post(url=url_sougou_collection, data=params_sougou_collection)
            assert res_sougou_post.status_code == result_sougou['Status']