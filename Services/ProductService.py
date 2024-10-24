from Models.products import products
from Database.ProductsDAO import ProductsDAO
from Util.validationError import ValidationError
from bson import ObjectId

class ProductsService():
    def __init__(self, dao: ProductsDAO):
        self.__dao = dao

    def doesProductNameExist(self, name):
        return self.__dao.doesProductNameExist(name)

    def getProductLikeName(self, name):
        return self.__dao.getProductLikeName(name)
    
    def getProductByID(self, productID):
        if not ObjectId.is_valid(productID):
            raise ValidationError("Invalid Product ID")
        
        return self.__dao.getProductByID(productID)
    
    def getAllProducts(self):
        return self.__dao.getAllProducts()
    
    def createProduct(self, name, price, amount):
        int_values = [price, amount]

        if self.__dao.doesProductNameExist(name):
            raise ValidationError('Product name already exists.')

        for value in int_values:
            try:
                int(value)
            except ValueError:
                raise ValidationError("'{0}' value entered is not numeric".format(value))
            
        if int(amount) < 0:
            raise ValidationError('Amount must be greater than 0')
        
        if int(price) < 0:
            raise ValidationError('Price must be greater than 0')
        
        if name.isspace() or name == '':
            raise ValidationError('Item name is required')
        
        product = products('', name, price, amount)

        return self.__dao.createProduct(product)
    
    def updateProduct(self, productID, name, price, amount, old_name):
        if not ObjectId.is_valid(productID):
            raise ValidationError("Improper product ID")
        
        if self.__dao.doesProductNameExist(name) and name != old_name:
            raise ValidationError('Product name already exists.')
    
        int_values = [price, amount]

        for value in int_values:
            try:
                int(value)
            except ValueError:
                raise ValidationError("'{0}' value entered is not numeric".format(value))
            
        if int(amount) < 0:
            raise ValidationError('Amount must be greater than 0')
        
        if int(price) < 0:
            raise ValidationError('Price must be greater than 0')
        
        if name.isspace() or name == '':
            raise ValidationError('Item name is required')
        
        product = products(productID, name, price, amount)

        return self.__dao.updateProduct(product)
    
    def deleteProduct(self, productID):
        if not ObjectId.is_valid(productID):
            raise ValidationError("Improper product ID")
        
        return self.__dao.deleteProduct(productID)

