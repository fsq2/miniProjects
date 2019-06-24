import random 
x = input('prese any button  to rolle the dice or q quit:')


while x!="q" :
 print(random.randint(1, 7))
 x = input('rolle the dice agin ?  press enteror to  quit press q ')

print('thx for playing ')