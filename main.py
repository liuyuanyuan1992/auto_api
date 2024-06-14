import os
import sys

import allure
import pytest

import requests


def run():
    case_path = os.path.join("/Users/liuyuanyuan/python/auto_interface/case")
    # print(case_path)
    # pytest.main([case_path, '-v'])
    pytest.main([case_path, '-v',
                 '--alluredir=results', '--clean-alluredir'])
    os.system('allure serve results')
    os.system('allure generate ./results/ -o ./report_allure/ --clean')



if __name__ == '__main__':
    run()
