
# Hourly pay 

#Hours = int(input("Please enter the number of hours: "))
#RPH   = int(input("Please enter the rate per hour: "))

def computepay (Hours, RPH): 
	float(RPH)
	float(Hours)	
	if Hours < 40 : 
		payout = Hours * RPH
	else: 
		payout = (40 * RPH ) + ((Hours - 40) * RPH * 1.50)

	print("Total Number of Hours: " +str(Hours))
	print ("Your Payout is: " +str(payout))

computepay (41,10)
