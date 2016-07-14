#!/usr/bin/env python

import sys 

startNum=1
endNum=100
aNum=910
test=[]
f=[]

def primeUp(startNum,endNum):
	for i in range(startNum,endNum):
		if i==1:
			continue
		j=2
		x="Prime"
		counter=0
		while j<i:
			if i%j==0:
				counter=1
				j=j+1
			else:
				j=j+1
		if counter == 0:
			print(str(x) + ": " + str(i))
			test.append(i)
		else:
			counter=0

def countUp(startNum,endNum):
	counter = startNum
	s=endNum
	while counter:
		if counter == s+1:
				break
		elif counter<0:
				continue
		else:
			pass
		print(counter)
		counter=counter+1

def testThing(aNum):
	a=aNum
	n=2
	while(n<=int(a)):
	    b=1
	    while(a%n==0):
	        b=0   
	        a=a/n
	    if(b==0):
	        f.append(n)
	    n=n+1
	print max(f)

def arrayDump():
	#print "\n" + str(min(test))
	print "\n" + str(test)
	#print "\n" + str(max(test))

def main():
	countUp(startNum,endNum)
	primeUp(startNum,endNum)
	#testThing(aNum)
	arrayDump()

if __name__ == "__main__":
    main()
