def food():
    name = input("Enter the food name: ")
    return name


def price():
    amt = float(input("Enter the price: "))
    return amt


def card(amt):
    stud = input("Are you a student card holder? (Yes/No): ")

    if stud.strip().lower() == "yes":
        discount = amt * 10 / 100
        print("You got a 10% offer!")
    else:
        discount = 0
        print("No offer")

    final_amount = amt - discount

    print("Original price: ₹", amt)
    print("Discount amount: ₹", discount)
    print("Final amount: ₹", final_amount)


food_name = food()
amt = price()

print("Food name:", food_name)
card(amt)