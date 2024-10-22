from Util.connectionUtil import connectionUtility
from Models.products import products
import re
import logging

class ProductsDAO():

    def getProduct(self, name):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['products']

        pattern = re.compile(name, re.IGNORECASE)

        results = collection.find({"name": pattern})

        products_arr = []
        for result in results:
            products_arr.append(result)

        return products_arr


test = ProductsDAO()

print(test.getProduct('app'))