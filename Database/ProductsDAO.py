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

        result = collection.find_one({"name": name})

        if result:
            return True
        else:
            return False

    def getProductLikeName(self, name):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['products']

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

        result = collection.insert_one({"name": product.getName(), "price": int(product.getPrice()), "amount": int(product.getAmount())})
        client.close()
        return self.getProductByID(result.inserted_id)

    def updateProduct(self, product: products):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['products']

        result = collection.update_one({'_id': ObjectId(product.getID())}, 
                        {"$set": {"name": product.getName(), "price": int(product.getPrice()), "amount": int(product.getAmount())}})

        client.close()

        return result.modified_count

    def deleteProduct(self, productID):
        client = connectionUtility.get_Connection()
        db = client['Project1']
        collection = db['products']

        result = collection.delete_one({"_id": ObjectId(productID)})

        client.close()

        return result.deleted_count



