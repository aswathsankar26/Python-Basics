total_person =  int (input("The Total Members : ")) #total members
total_bill = int (input("The Total Bill Amount  : ")) #total amount
service_charge = total_bill * 5 / 100

total = total_bill / total_person 
print ("The total amount is : " , total_bill)
print ("Service Charge : " , service_charge)

print ("The Split amount is : " ,total  )

print ("The final Amount is : " ,total_bill + service_charge )

print ("Thanks for visiting ")
 
