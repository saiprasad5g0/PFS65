budget = int(input("Enter budget: "))
if budget > 10000:
    print("Go to TRIP")
elif budget > 5000:
    print("RESORT STAY")
elif budget > 3000:
    print("MOVIE AND DINNER")
elif budget > 1000:
    print("CAFE AND SHOPPOING")
elif budget > 500:
    print("STREET FOOD AND PARK VISIT")
else:
    print("Muskoni intlo kursooo")