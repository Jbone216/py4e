hrs = input("Enter Hours:")
h = float(hrs)

rate = input('Enter Rate:')
r = float(rate)

ohrs = input('Enter OT Hours:')
o = float(ohrs)

otr = (r * 1.5)

totalHours = (h + o)

if totalHours > 40:
    print((h * r) + (otr * o))
