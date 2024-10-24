from Services.ProductService import ProductsService

class productController():
    def __init__(self, service: ProductsService):
        self.__service = service

    def getProductLikeName(self, name):
        return self.__service.getProductLikeName(name)
    
    def doesProductNameExist(self, name):
        return self.__service.doesProductNameExist(name)
    
    def getProductById(self, productID):
        return self.__service.getProductByID(productID)
    
    def getAllProducts(self):
        return self.__service.getAllProducts()
    
    def createProduct(self, name, price, amount):
        return self.__service.createProduct(name, price, amount)
    
    def updateProduct(self, productID, name, price, amount, old_name):
        return self.__service.updateProduct(productID, name, price, amount, old_name)
    
    def deleteProduct(self, productID):
        return self.__service.deleteProduct(productID)
    
