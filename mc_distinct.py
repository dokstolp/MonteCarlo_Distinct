import random as rd

def choose(choices):
    location = rd.randint(0,len(choices)-1)
    choice = choices[location]
    sumval = sum([x[1] for x in choices])
    probs = [float(x[1])/sumval for x in choices]
    maxval = max(probs)
    rand2 = rd.random()*maxval
    if probs[location]>rand2:
        return choice[0]
    else:
        return choose(choices)

dicter = {'a':0,'b':0,'c':0}
for i in range(0,10000):
	dicter[choose([('a',1),('b',2),('c',3)])]+=1
print dicter
