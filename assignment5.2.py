#Repeatdely prompts user for int until user enters done
#When done, print largest and smallest numbers
#Try and except to catch a non integar numbers
#Enter: 7,2,bob, 10, 4
#output is Invalid input, Maximum is 10, Minimum is 2

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue

    if largest is None:
        largest = fnum
    elif fnum > largest:
        largest = fnum

    if smallest is None:
        smallest = fnum
    elif fnum < smallest:
        smallest = fnum

print('Maximum is', int(largest))
print('Minimum is', int(smallest))
