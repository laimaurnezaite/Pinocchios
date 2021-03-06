import sqlite3

menu = {
    "regular_pizza" : [
        {"title":"Cheese","size":"Small", "unit_price":12.70, "item_category":"Regular Pizza"},
        {"title":"1 topping","size":"Small", "unit_price":13.70, "item_category":"Regular Pizza"},
        {"title":"2 toppings","size":"Small", "unit_price":15.20, "item_category":"Regular Pizza"},
        {"title":"3 topping","size":"Small", "unit_price":16.20, "item_category":"Regular Pizza"},
        {"title":"Special","size":"Small", "unit_price":17.75, "item_category":"Regular Pizza"},
        {"title":"Cheese","size":"Large", "unit_price":17.95, "item_category":"Regular Pizza"},
        {"title":"1 topping","size":"Large", "unit_price":19.95, "item_category":"Regular Pizza"},
        {"title":"2 toppings","size":"Large", "unit_price":21.95, "item_category":"Regular Pizza"},
        {"title":"3 topping","size":"Large", "unit_price":23.95, "item_category":"Regular Pizza"},
        {"title":"Special","size":"Large", "unit_price":25.95, "item_category":"Regular Pizza"}],
    "sicilian_pizza": [
        {"title":"Cheese","size":"Small", "unit_price":24.45, "item_category":"Sicilian Pizza"},
        {"title":"1 item","size":"Small", "unit_price":26.45, "item_category":"Sicilian Pizza"},
        {"title":"2 items","size":"Small", "unit_price":28.45, "item_category":"Sicilian Pizza"},
        {"title":"3 items","size":"Small", "unit_price":29.45, "item_category":"Sicilian Pizza"},
        {"title":"Special","size":"Small", "unit_price":30.45, "item_category":"Sicilian Pizza"},
        {"title":"Cheese","size":"Large", "unit_price":38.70, "item_category":"Sicilian Pizza"},
        {"title":"1 item","size":"Large", "unit_price":40.70, "item_category":"Sicilian Pizza"},
        {"title":"2 items","size":"Large", "unit_price":42.70, "item_category":"Sicilian Pizza"},
        {"title":"3 items","size":"Large", "unit_price":44.70, "item_category":"Sicilian Pizza"},
        {"title":"Special","size":"Large", "unit_price":45.70, "item_category":"Sicilian Pizza"}],
    "subs" : [
        {"title":"Cheese","size":"Small", "unit_price":6.50, "item_category":"Subs"},
        {"title":"Italian","size":"Small", "unit_price":6.50, "item_category":"Subs"},
        {"title":"Ham + Cheese","size":"Small", "unit_price":6.50, "item_category":"Subs"},
        {"title":"Meatball","size":"Small", "unit_price":6.50, "item_category":"Subs"},
        {"title":"Tuna","size":"Small", "unit_price":6.50, "item_category":"Subs"},
        {"title":"Turkey","size":"Small", "unit_price":7.50, "item_category":"Subs"},
        {"title":"Chicken Parmigiana","size":"Small", "unit_price":7.50, "item_category":"Subs"},
        {"title":"Eggplant Parmigiana","size":"Small", "unit_price":6.50, "item_category":"Subs"},
        {"title":"Steak","size":"Small", "unit_price":6.50, "item_category":"Subs"},
        {"title":"Steak + Cheese","size":"Small", "unit_price":6.95, "item_category":"Subs"},
        {"title":"Hamburger","size":"Small", "unit_price":4.60, "item_category":"Subs"},
        {"title":"Cheeseburger","size":"Small", "unit_price":5.10, "item_category":"Subs"},
        {"title":"Fried Chicken","size":"Small", "unit_price":6.95, "item_category":"Subs"},
        {"title":"Veggie","size":"Small", "unit_price":6.95, "item_category":"Subs"},
        {"title":"Cheese","size":"Large", "unit_price":7.95, "item_category":"Subs"},
        {"title":"Italian","size":"Large", "unit_price":7.95, "item_category":"Subs"},
        {"title":"Ham + Cheese","size":"Large", "unit_price":7.95, "item_category":"Subs"},
        {"title":"Meatball","size":"Large", "unit_price":7.95, "item_category":"Subs"},
        {"title":"Tuna","size":"Large", "unit_price":7.95, "item_category":"Subs"},
        {"title":"Turkey","size":"Large", "unit_price":8.50, "item_category":"Subs"},
        {"title":"Chicken Parmigiana","size":"Large", "unit_price":8.50, "item_category":"Subs"},
        {"title":"Eggplant Parmigiana","size":"Large", "unit_price":7.95, "item_category":"Subs"},
        {"title":"Steak","size":"Large", "unit_price":7.95, "item_category":"Subs"},
        {"title":"Steak + Cheese","size":"Large", "unit_price":8.50, "item_category":"Subs"},
        {"title":"Hamburger","size":"Large", "unit_price":6.95, "item_category":"Subs"},
        {"title":"Cheeseburger","size":"Large", "unit_price":7.45, "item_category":"Subs"},
        {"title":"Fried Chicken","size":"Large", "unit_price":8.50, "item_category":"Subs"},
        {"title":"Veggie","size":"Large", "unit_price":8.50, "item_category":"Subs"}],
    "pasta" : [
        {"title":"Baked Ziti w/Mozzarella","size":"", "unit_price":6.50, "item_category":"Pasta"},
        {"title":"Baked Ziti w/Meatballs","size":"", "unit_price":8.75, "item_category":"Pasta"},
        {"title":"Baked Ziti w/Chicken","size":"", "unit_price":9.75, "item_category":"Pasta"}],
    "salads": [
        {"title":"Garden Salad","size":"", "unit_price":6.25, "item_category":"Salads"},
        {"title":"Greek Salad","size":"", "unit_price":8.25, "item_category":"Salads"},
        {"title":"Antipasto","size":"", "unit_price":8.25, "item_category":"Salads"},
        {"title":"Salad w/Tuna","size":"", "unit_price":8.25, "item_category":"Salads"}],
    "dinner_platters" : [
        {"title":"Garden Salad","size":"Small", "unit_price":40.00, "item_category":"Dinner Platters"},
        {"title":"Greek Salad","size":"Small", "unit_price":50.00, "item_category":"Dinner Platters"},
        {"title":"Antipasto","size":"Small", "unit_price":50.00, "item_category":"Dinner Platters"},
        {"title":"Baked Ziti","size":"Small", "unit_price":40.00, "item_category":"Dinner Platters"},
        {"title":"Meatball Parm","size":"Small", "unit_price":50.00, "item_category":"Dinner Platters"},
        {"title":"Chicken Parm","size":"Small", "unit_price":55.00, "item_category":"Dinner Platters"},
        {"title":"Garden Salad","size":"Large", "unit_price":65.00, "item_category":"Dinner Platters"},
        {"title":"Greek Salad","size":"Large", "unit_price":75.00, "item_category":"Dinner Platters"},
        {"title":"Antipasto","size":"Large", "unit_price":75.00, "item_category":"Dinner Platters"},
        {"title":"Baked Ziti","size":"Large", "unit_price":65.00, "item_category":"Dinner Platters"},
        {"title":"Meatball Parm","size":"Large", "unit_price":75.00, "item_category":"Dinner Platters"},
        {"title":"Chicken Parm","size":"Large", "unit_price":85.00, "item_category":"Dinner Platters"}]
}

toppings = {
    "free toppings" : [
        {"title":"Pepperoni","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Sausage","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Mushrooms","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Onions","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Ham","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Canadian Bacon","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Pineapple","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Eggplant","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Tomato & Basil","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Green Peppers","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Hamburger","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Spinach","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Artichoke","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Buffalo Chicken","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Barbecue Chicken","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Anchovies","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Black Olives","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Fresh Garlic","size":"", "unit_price":0.00, "item_category":"Free Toppings"},
        {"title":"Zucchini","size":"", "unit_price":0.00, "item_category":"Free Toppings"}],
    "toppings" : [
        {"title":"+ Mushrooms", "size":"", "unit_price":0.50, "item_category":"Toppings"},
        {"title":"+ Green Peppers", "size":"", "unit_price":0.50, "item_category":"Toppings"},
        {"title":"+ Onions", "size":"", "unit_price":0.50, "item_category":"Toppings"},
        {"title":"Extra Cheese on any sub", "size":"", "unit_price":0.50, "item_category":"Toppings"}],
}

db = sqlite3.connect("db.sqlite3")

for category in toppings:
    for item in range(len(toppings[category])):
            db.execute("INSERT INTO menu_toppings (title, unit_price, item_category) VALUES (:title, :unit_price, :item_category);",
            {"title":toppings[category][item]['title'], "unit_price":toppings[category][item]['unit_price'], "item_category":toppings[category][item]['item_category']})
            db.commit()