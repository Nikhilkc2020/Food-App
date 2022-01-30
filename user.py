#!/usr/bin/env python
# coding: utf-8

# In[1]:


import admin as ad

class User:
    login_info = {}

    def __init__(self, name, phoneno, email, address, password):
        self.name = name
        self.number = phoneno
        self.email = email
        self.address = address
        self.password = password
        User.login_info[self.name] = self.password
        self.profile = {}
        self.order_history = {}

    @classmethod
    def login(cls, username, password):
        if cls.login_info.get(username) == password:
            print("****You're are successfully logged in!!!****")
            return True
        else:
            print("SORRY! You have Entered Wrong Credentials!! Please enter the correct details")
            return False

    def see_profile(self):
        self.profile[self.name] = {
            "Full Name": self.name,
            "Phone Number": self.number,
            "E-Mail": self.email,
            "Address": self.address,
            "Password": self.password
        }
        return self.profile

    def update_profile(self):
        x = input("What do you want to update in your profile..")
        y = input("And what is the changes to the new one: ")
        self.profile[x] = y
        print("Your Profile is Successfully Updated Your Profile")
        return self.profile

    def place_order(self):
        print("What item do you want to order from the menu")
        print(ad.show_menu())
        print("Enter the food ID of the food you wanted to order")
        user_choice = int(input("If you want to order the above entered food then select 1.YES 2.NO"))
        if user_choice == 1:
            foodid = int(input("Enter the food id here: "))
            quan = int(input("Enter the number of quantity of the food you want: "))
            x = ad.menu[foodid]["Price"] * quan
            again_ask = input("If you still want to order the same food again then select YES or NO")
            if again_ask == "YES":
                print(f'''Your food name is {ad.menu[foodid]["Food Name"]}''')
                print(f'''Price of your food is {ad.menu[foodid]["Price"]}''')
                print(f"This is your quantity {quan}")
                print(f"It costs you {x}INR in total")
                print("Now You're all set to order this food")
                self.order_history[foodid] = {
                    "Food Name": ad.menu[foodid]["Food Name"],
                    "Price": ad.menu[foodid]["Price"],
                    "Quantity": quan
                }
                final_stock = ad.menu[foodid]["Stock"] - quan
                ad.menu[foodid]["Stock"] = final_stock
                print("You're order is successfully placed Thank you for ordering!!! Please do order the food from our hotel again")

            elif again_ask == "NO":
                print("This Order is successfully cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You have selected the option 2 so we have cancelled this order")
        else:
            print("The choice you have entered is wrong..Please choose the valid choice")

    def watch_profile(self):
        print(self.profile)



Nikhil = User("Nikhil K C", "7829864973", "nikhilkc1998@gmail.com", "Raghavendra nagar", "nikhil@123")
Hardin = User("Hardin Roy", "7645678978", "hardin@gmail.com", "Nagarbhavi", "hardin@123")
Nikhil.see_profile()
Hardin.see_profile()


# In[ ]:




