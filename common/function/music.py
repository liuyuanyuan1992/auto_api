import allure

from auto_interface.common.key_word.request_method import RequestMethod
from auto_interface.common.util.ini_driver import load_ini


class Music(object):

    def music_play(self, musicdata):
        mp = RequestMethod()
        url = load_ini('/Users/liuyuanyuan/python/auto_interface/conf/api_url.ini','Api')
        url_music_play = url[2][1]

        params_music_play = {
            'songurl': musicdata['Params']['songurl'],
            'format': musicdata['Params']['format']
        }

        result_music_play = {
            'Status': musicdata['Params']['Status']
        }

        with allure.step("get请求的响应信息"):
            res_music_play_get = mp.get(url=url_music_play, params= params_music_play)
            assert res_music_play_get.status_code == result_music_play['Status']

        with allure.step("post请求的响应信息"):
            res_music_play_post = mp.post(url=url_music_play, data= params_music_play)
            assert  res_music_play_post.status_code == result_music_play['Status']