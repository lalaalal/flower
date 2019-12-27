from db import DB
from webcrawling import RankData
from webcrawling import Crawler

class Save:
    def __init__(self):
        self.db = DB()
        self.crawler = Crawler()
    
    def inserttoDB(self):
        for i in self.crawler.rankData:
            self.db.insertRank(i)

save = Save()
save.inserttoDB()