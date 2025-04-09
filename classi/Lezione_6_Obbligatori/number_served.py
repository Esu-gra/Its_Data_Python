class Restaurant:
    def __init__(self,restaurant_name,cusine_type,number_served=0):
        self.restaurant_name=restaurant_name
        self.cusine_type=cusine_type
        self.number_served=number_served
    
    def describe_resturant(self):
        print(f"Name: {self.restaurant_name}\nType:{self.cusine_type}\n clienti serviti: {self.number_served}")

    def open_restaurant(self):
        print("Open")
    
    def set_number_served(self,n):
        nuber_served=self.number_served
        return nuber_served 
    
    def increment_number_served(self):
        increment=self.number_served
        increment+=self.number_served
        return increment
        
    





    
    



restaurent=Restaurant("Da Paolo" ,"egizio",number_served=32)

restaurent.describe_resturant()
restaurent.set_number_served()
restaurent.increment_number_served()
