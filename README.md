# Project 3

Web Programming with Python and JavaScript

# Install packages
- Django==2.0.3
- django-jsonfield 1.4.0

# Export
- export EMAIL_HOST_PASSWORD

# How to run app?
- python manage.py runserver


# About
 - This is web application that is online order system for restourant. Client can create his profile, add products to shopping cart (with toppings if applicable), confirm order and check previoulsy confirmed orders. Also, user can change password or reset if needed. 
 Restourant administration can log in through admin page, manage products, toppings, customers and orders.
 - My personal touch - ability to change/reser passwords and send confirmation email to customer after order was confirmed.

 # Files:
 -  Menu - app for Menu. This app contains models, views, urls and tests that are related to restaurant menu: customer can see all menu or specifit item that he chose.
 - Orders - app for Orders. This app contains models, views, urls and tests that are related to orders: customer can add products to shopping cart, confirm order, see previoulsy confirmed orders.
 - Users - app for Users. This app contains models, views, urls and tests that are related to restaurant users: customer can create account, log in/log out to his account, change or reset password.
 - Menu file - menu_from_pinocchios.py - data file with menu from restaurant. Using this file, restaurant admins can load new products to system. Also it can be done manualy through admin site.