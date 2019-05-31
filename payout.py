
# Hourly pay 

Hours = int(input("Please enter the number of hours: "))
RPH   = int(input("Please enter the rate per hour: "))

if Hours < 40 : 
	payout = Hours * RPH
else: 
	payout = (40 * RPH ) + ((Hours - 40) * RPH * 1.50)

print ("Your Payout is: " +str(payout))
