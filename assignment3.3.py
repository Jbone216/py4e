score = input('Enter Score:') #Enter Score of test (.85)
s = float(score)
try:
    s=float(score)
except:
    print('Error, please enter a valid number.')

if s >=.90:
	print('A')
elif s >= .80:
    print('B')
elif s >= .70:
    print('C')
elif s >= .60:
    print('D')
elif s < .60:
    print('F')
    
