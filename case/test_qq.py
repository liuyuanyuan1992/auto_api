import pytest

from auto_interface.common.function.qq import QQ
from auto_interface.common.util import yaml_driver
import allure

@allure.feature("QQ等级")
class TestQq(object):
    # 初始化QQ接口相关功能
    actions2 = QQ()

    @allure.story("QQ等级查询")
    @pytest.mark.parametrize('qqdata', yaml_driver.load_yaml('/Users/liuyuanyuan/python/auto_interface/data/qq.yaml'))
    def test_qq_level(self, qqdata):
        self.actions2.qq_level(qqdata)

    @allure.story("QQ强制对话")
    @pytest.mark.parametrize('qqtalkdata', yaml_driver.load_yaml('/Users/liuyuanyuan/python/auto_interface/data/qq.yaml'))
    def test_qq_talk(self, qqtalkdata):
        self.actions2.qq_talk(qqtalkdata)