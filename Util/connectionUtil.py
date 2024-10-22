from pymongo import MongoClient

class connectionUtility():
    @staticmethod
    def get_Connection():
        client = MongoClient("mongodb://localhost:27017/")

        return client