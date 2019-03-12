import requests
from requests import Timeout


class HtmlDownloader(object):
    def __init__(self):
        self.request_session = requests.session()
        self.request_session.proxies

    def download(self, url, retry_count=3, headers=None, proxies=None, data=None):
        try:
            if url is None:
                return None
            if headers:
                self.request_session.headers.update(headers)
            if data:
                content = self.request_session.post(url, data=data, proxies=proxies).content
            else:
                content = self.request_session.get(url, proxies=proxies).content
        except Timeout as e:
            print('download Timeout! url is '+ url)
            content = None
            if retry_count > 0:
                self.download(url, retry_count-1, headers, proxies, data)
        except Exception as e:
            print('download failed! Exception is ', str(e))
            content = None
        return content


