import mysql.connector
from mysql.connector import errorcode
from webcrawling import RankData
from webcrawling import Crawler

class DB:
    DB_NAME = 'datadb'
    def __init__(self):
        self.cnx = mysql.connector.connect(user='lalaalal', password='qhsxlsEndEl^3^',
                                    host='127.0.0.1',
                                    use_pure=False)
        self.cursor = self.cnx.cursor()

        TABLES = {}
        TABLES['ranktbl'] = "CREATE TABLE ranktbl ( `no` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, `date` DATETIME DEFAULT NOW(), `rank` INT NOT NULL, `data` VARCHAR(20) NOT NULL);"

        try:
            self.cursor.execute("USE {}".format(self.DB_NAME))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(self.DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database()
                print("Database {} created successfully.".format(self.DB_NAME))
                self.cnx.database = self.DB_NAME
                self.create_tables(TABLES)
            else:
                print(err)
                exit(1)

    def create_database(self):
        try:
            self.cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        
    def create_tables(self, TABLES):
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                self.cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

    def insertRank(self, rankData):
        rank = rankData.rank
        data = rankData.data
        try:
            self.cursor.execute("INSERT INTO ranktbl VALUES (DEFAULT, DEFAULT, {}, '{}')".format(rank, data))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def __del__(self):
        self.cnx.close()