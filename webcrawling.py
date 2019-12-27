import requests
from bs4 import BeautifulSoup

class RankData:
    def __init__(self, rank, data):
        self.data = data
        self.rank = rank
    
class Crawler:
    def __init__(self):
        req = requests.get('https://naver.com/')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        my_titles = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > .ah_item > .ah_a > .ah_k')
        cnt = 0
        self.rankData = []
        for i in my_titles:
            print(i.text)
            self.rankData.append(RankData(cnt + 1, i.text))
            cnt += 1
    