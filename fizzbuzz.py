def fizz(n):
  	if n % 3 == 0:
  		return(" fizz")
	else:
		return("")

def buzz(n):
	if n % 5 == 0:
		return(" buzz")
	else:
		return(" ")

def fizzbuzz(end):
	num = 1
	while num < end+1:
	  	n=str(num)
	  	print(n + fizz(num) + buzz(num))
	  	num += 1

max=100
fizzbuzz(max)
