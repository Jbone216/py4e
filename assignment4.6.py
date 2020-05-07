#45 Hours
#10.50
#498.75

hrs = input("Enter Regular Hours:") #Input hours up to 40
h = float(hrs)

rate = input('Enter Regular Pay Rate:') #Straight pay
r = float(rate)

ohrs = input('Enter OT Hours:') #Hours over 40
o = float(ohrs)

otr = input('Enter OT Rate:') #Overtime rate for hours over 40
ovr = float(otr)

totalHours = (h + o) #Total hours worked, straight and OT

def computepay():
    if totalHours > 40:
    	return((h * r) + (ovr * o))

p = computepay()
print('Pay',p)
