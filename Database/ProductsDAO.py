from Util.connectionUtil import connectionUtility
from Models.products import products
from bson import ObjectId
import re
import logging

class ProductsDAO():

    def doesProductNameExist(self, name):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['products']

        logging.info("Accessing Products Collection...")

        result = collection.find_one({"name": {"$regex": name, "$options": "i"}})

        if result:
            product = products(str(result['_id']), result['name'], result['price'], result['amount'])
            client.close()
            return product
        else:
            client.close()
            return False

    def getProductLikeName(self, name):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['products']

        logging.info("Accessing Products Collection...")

        pattern = re.compile(name, re.IGNORECASE)

        results = collection.find({"name": pattern})

        products_arr = []
        for result in results:
            product = products(str(result['_id']), result['name'], result['price'], result['amount'])
            products_arr.append(product)

        client.close()

        return products_arr
    
    def getProductByID(self, productID):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['products']

        logging.info("Accessing Products Collection...")

        result = collection.find_one({"_id": ObjectId(productID)})

        if result:
            product = products(str(result['_id']), result['name'], result['price'], result['amount'])
            client.close()
            return product
        else:
            client.close()
            return None
    
    def getAllProducts(self):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['products']

        logging.info("Accessing Products Collection...")

        results = collection.find()

        products_arr = []
        for result in results:
            product = products(str(result['_id']), result['name'], result['price'], result['amount'])
            products_arr.append(product)

        client.close()

        return products_arr
    
    def createProduct(self, product: products):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['products']

        logging.info("Accessing Products Collection...")

        result = collection.insert_one({"name": product.getName(), "price": int(product.getPrice()), "amount": int(product.getAmount())})
        client.close()
        return self.getProductByID(result.inserted_id)

    def updateProduct(self, product: products):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['products']

        logging.info("Accessing Products Collection...")

        result = collection.update_one({'_id': ObjectId(product.getID())}, 
                        {"$set": {"name": product.getName(), "price": int(product.getPrice()), "amount": int(product.getAmount())}})

        client.close()

        return result.modified_count

    def deleteProduct(self, productID):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['products']

        logging.info("Accessing Products Collection...")

        result = collection.delete_one({"_id": ObjectId(productID)})

        client.close()

        return result.deleted_count



