import allure
import pytest
from auto_interface.common.util import yaml_driver
from auto_interface.common.function.baidu import BaiDu


@allure.feature("百度账号")
@pytest.mark.smoke
@allure.severity("Block")
class TestBaidu(object):
    # 初始化用例库
    actions1 = BaiDu()

    @allure.story("登陆")
    @pytest.mark.parametrize('baidu_data', yaml_driver.load_yaml('/Users/liuyuanyuan/python/auto_interface/data/baidu.yaml'))
    def test_baidu_login(self, baidu_data):
        self.actions1.baidu_login(baidu_data)