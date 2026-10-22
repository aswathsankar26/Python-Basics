
sub1 = int(input("Enter the Tamil Mark: "))
sub2 = int(input("Enter the English Mark: "))
sub3 = int(input("Enter the Maths Mark: "))
sub4 = int(input("Enter the Science Mark: "))
sub5 = int(input("Enter the Social Science Mark: "))

add_subs = sub1 + sub2 + sub3 + sub4 + sub5
average = add_subs / 5

print("Total Marks:", add_subs)
print("Average:", average)

if any(mark < 0 or mark > 100 for mark in [sub1, sub2, sub3, sub4, sub5]):
    print("Invalid marks")
elif average >= 86:
    print("A Grade")
elif average >= 71:
    print("B Grade")
elif average >= 51:
    print("C Grade")
elif average >= 35:
    print("D Grade")
else:
    print("F Grade")
