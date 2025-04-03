class Restaurant:
    def __init__(self,restaurant_name,cusine_type):
        self.restaurant_name=restaurant_name
        self.cusine_type=cusine_type
    
    def describe_resturant(self):
        print(f"Name: {self.restaurant_name}\nType:{self.cusine_type}")

    def open_restaurant(self):
        print("Open")

    


data_restaurant=Restaurant("Data_pizza","Asiatico")


        