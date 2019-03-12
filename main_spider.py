import url_manager
import html_downloader
import html_parser
import html_output


class MainSpider3(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()
        self.headers = {
            "User_Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"
        }


    def run(self):
        main_seed_url = self.urls.get_main_seed_url()
        content = self.downloader.download(main_seed_url, retry_count=3, headers=self.headers).decode('utf8')
        subject_urls = self.parser.parse_subject_urls(content)
        for subject_url in subject_urls:
            self._run_subject_url(subject_url)

    def _run_subject_url(self, subject_url):
        print('subject_url is ', subject_url)
        content = self.downloader.download(subject_url, retry_count=2, headers=self.headers).decode('utf8')
        mj_info = self.parser.parse_subject_mj_info(content)
        if mj_info is None:
            return
        mj_max_count = int(mj_info['count'])
        mj_namee = str(mj_info['mj_name'])
        curr_count = 1
        index = 1
        while curr_count <= mj_max_count:
            if index > 1:
                subject_url = subject_url[0 : len(subject_url - 5)] + '_' + str(index) + '.html'
            index = index + 1
            #每个页面图片个数为4
            curr_count = curr_count + 4
            print('curreent url is ', subject_url)
            content = self.downloader.download(subject_url, retry_count=2, headers=self.headers).decode('utf8')
            pic_urls = self.parser.parse_page_pics(content)
            for  pic_url in pic_urls:
                self.output.download_and_save(pic_url, mj_namee)


if __name__ == '__main__':
    MainSpider3().run()

