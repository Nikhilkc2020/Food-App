#!/usr/bin/env python
# coding: utf-8

# In[6]:


admin_keys = {"Nikhil": "nikhil@1998"}

menu = {1: {'Food Name': 'Masala Dosa', 'Food ID': 1, 'Price': 70, 'Discount': 2, 'Stock': 8},
        2: {'Food Name': 'Pongal', 'Food ID': 2, 'Price': 50, 'Discount': 5, 'Stock': 10}}


def add_new_item():
    foodname = input("Enter the foood name you want: ")
    foodid = int(input("Enter your food id : "))
    price = int(input("Enter the price of the food: "))
    discount = int(input("Enter the discount of food: "))
    stock = int(input("Enter te stock value of food: "))
    menu[foodid] = {
        "Food Name": foodname,
        "Food ID": foodid,
        "Price": price,
        "Discount": discount,
        "Stock": stock
    }
    print(f"The {foodname} is successfully added to cart")
    return menu


def edit_from_item():
    food = int(input("Enter the foodid which you want to edit: "))
    a = input("Enter the food name")
    b = int(input("Enter the price of food"))
    c = int(input("Enter the discount of food"))
    d = int(input("Enter the stock of the food"))
    menu[food]["Food Name"] = a
    menu[food]["Price"] = b
    menu[food]["Discount"] = c
    menu[food]["Stock"] = d
    print("*****You have Edited food item successfully*****")
    return menu

def show_menu():
    print("*****THIS IS THE MENU OF NIKHIL HOTEL*****")
    for i in menu:
        print("Food Name: ",menu[i]["Food Name"])
        print("Price: ",menu[i]["Price"],"INR")
        print("Food ID: ",menu[i]["Food ID"])

def remove_food_item():
    x = int(input("Enter the food id which you want to remove"))
    menu.pop(x)
    print("The food item you entered is removed successfully ")
    return menu


# In[ ]:




