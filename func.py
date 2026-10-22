
def food():
    sapadu = "Briyani"
    print("The food is:", sapadu)

def card():
    stud = input("Do you have a student card? (Yes/No): ")

    if stud.strip().lower() == "yes":
        print("10% offer")
    else:
        print("No offer")

def checkout():
    print("Billing is ready")

food()
card()
checkout()
