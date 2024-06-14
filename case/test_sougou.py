import pytest

from auto_interface.common.function.sougou import SouGou
from auto_interface.common.util import yaml_driver
import allure

@allure.feature("搜狗")
class TestSouGou(object):
    # 初始化QQ接口相关功能
    actions5 = SouGou()

    @allure.story("搜狗收录情况")
    @pytest.mark.parametrize('sougoudata', yaml_driver.load_yaml('/Users/liuyuanyuan/python/auto_interface/data/sougou.yaml'))
    def test_qq_level(self, sougoudata):
        self.actions5.sougou_collection(sougoudata)