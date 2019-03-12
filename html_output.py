import os
import requests
import time
'''
爬取美图录网站妹子图，然后按照目录命名下载下来
程序没问题,但是再拉取图片时,网站现在做了权限控制,每次都会报403错误被拒绝访问
'''

class HtmlOutput(object):
    def __init__(self):
        # self.save_root_path = r'output'
        self.save_root_path = r'D:\MyPython2\Spider3\photo'

    def download_and_save(self, pic_url, mj_namee):
        print('开始下载图片 url : ' + pic_url + ' name : ' + mj_namee)
        save_path = self.save_root_path + os.path.sep + mj_namee
        # 没有路径则创建目录
        if os.path.exists(save_path) is False:
            os.mkdir(save_path)
        file_path = save_path + os.path.sep + pic_url.split('/')[-1]
        # 判断文件是否存在 存在则不再打印
        if os.path.exists(file_path):
            print('该文件已经存在!', pic_url)
            return
        try:
            content = requests.get(pic_url, timeout=1).content
            with open(file_path, 'wb') as save_file:
                save_file.write(content)
                time.sleep(1000)
        except Exception as e:
            print('HtmlOutput.download_and_save error',str(e))

