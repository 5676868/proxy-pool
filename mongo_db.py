import pymongo

class Mymongo:
    def __init__(self, dbname, colname):
        myclient = pymongo.MongoClient('127.0.0.1:27017')
        mydb = myclient[dbname]
        self.mycol = mydb[colname]

    def insert_one(self, ip):
        self.mycol.insert_one(ip)

    def removeall(self):
        self.mycol.delete_many({})

    def count_ip(self, ip):
        return self.mycol.count({"ip":ip})


ipmongo = Mymongo("proxy_db", "ip_list")
