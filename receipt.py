import math
import datetime

class Receipt:
    
    def __init__(self, receiptModel):
        self.receiptModel = receiptModel
        self.itemList = receiptModel.items
        self.points = 0

        self.calculatePoints()
    
    def calculatePoints(self):

        for each in self.receiptModel.retailer:
            if each.isalnum():
                self.points += 1
        
        if float(self.receiptModel.totalAmount).is_integer():
            self.points += 50
        
        if float(self.receiptModel.totalAmount) % 0.25 == 0:
            self.points += 25
        
        self.points += 5 * (len(self.itemList)//2)
        
        point = 0
        for item in self.itemList:
            if len(item.description.strip()) % 3 == 0:
                point += int(math.ceil(float(item.price) * 0.2))
            
            
        self.points += point
        
        dayPurchased = datetime.datetime.strptime(self.receiptModel.purchaseDate, '%Y-%m-%d').day

        if dayPurchased % 2 == 1:
            self.points += 6
        
        timePurchased = datetime.datetime.strptime(self.receiptModel.purchaseTime, '%H:%M').time()

        if timePurchased >  datetime.time(14, 0, 0) and timePurchased < datetime.time(16, 0, 0):
            self.points += 10
        

    def getPoints(self):
        return self.points