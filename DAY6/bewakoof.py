# BEWAKOOF CLOTHING APP

print("Welcome to Bewakoof")

# Login
name = input("Enter your name: ")          # str ( is used to store text) 
age = int(input("Enter your age: "))       # int (is used to store whole numbers) 

# Products
products = ["T-Shirt", "Jeans", "Hoodie"]  # list (used do store multiple values and we can change the values)

print("\nProducts:", products)
product = input("Choose product: ")         # str

price = float(input("Enter price: "))       # float( used to store decimal points)
quantity = int(input("Enter quantity: "))   # int

# Membership
member = input("Are you a member? yes/no: ")
is_member = member == "yes"                 # bool (true or false)

# Sizes
sizes = ("S", "M", "L", "XL")               # tuple (multiple values that cannot be changed)

# Categories
categories = {"Men", "Women", "Kids"}       # set (used to store unique values it automatically removes duplicates)

# Address
city = input("Enter city: ")                # str

# Order details
order = {
    "Name": name,
    "Product": product,
    "Quantity": quantity,
    "City": city
}                                           # dict( used to  store key and values )

# Payment
payment = input("Enter payment method: ")   # str

# Total
total = price * quantity                    # float

# Delivery
tracking_id = None                          # NoneType (no values)

print("\n----- ORDER DETAILS -----")
print("Name:", name)
print("Age:", age)
print("Product:", product)
print("Price:", price)
print("Quantity:", quantity)
print("Member:", is_member)
print("Size Options:", sizes)
print("Categories:", categories)
print("City:", city)
print("Payment:", payment)
print("Total:", total)
print("Order:", order)
print("Tracking ID:", tracking_id)

print("\nOrder Confirmed!")
print("Out for Delivery!")
print("Delivered!")
