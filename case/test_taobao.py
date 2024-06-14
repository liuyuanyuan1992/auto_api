import pytest

from auto_interface.common.function.taobao import Taobao
from auto_interface.common.util import yaml_driver
import allure

@allure.feature("淘宝")
class TestTaobao(object):
    # 初始化QQ接口相关功能
    actions4 = Taobao()

    @allure.story("淘宝买家秀图片")
    @pytest.mark.parametrize('taobaodata', yaml_driver.load_yaml('/Users/liuyuanyuan/python/auto_interface/data/taobao.yaml'))
    def test_qq_level(self, taobaodata):
        self.actions4.taobao_picture(taobaodata)