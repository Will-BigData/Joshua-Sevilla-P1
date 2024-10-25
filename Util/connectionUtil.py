from pymongo import MongoClient
import logging

class connectionUtility():
    @staticmethod
    def get_Connection():
        logging.debug("Connecting to db...")
        client = MongoClient("mongodb://localhost:27017/")

        return client