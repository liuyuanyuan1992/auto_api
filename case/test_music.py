import allure
import pytest

from auto_interface.common.function.music import Music
from auto_interface.common.util import yaml_driver


@allure.feature("音乐")
@pytest.mark.smoke
@allure.severity("Critical")
class TestMusic(object):
    action3 = Music()

    @allure.story("全民K歌")
    @pytest.mark.parametrize('musicdata',yaml_driver.load_yaml('/Users/liuyuanyuan/python/auto_interface/data/music.yaml'))
    def test_music_play(self, musicdata):
        self.action3.music_play(musicdata)
