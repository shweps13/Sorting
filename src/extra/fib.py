print('FACTORIAL')
# 0! = 1
# 1! = 1
# 2! = 1*2     = 1! * 2
# 3! = 1*2*3   = 2! * 3
# 4! = 1*2*3*4 = 3! * 4
def factorial(n):
    print('CALL:', n)
    # if < 2 return 1
    if n < 2:
        return 1
    #  find previous factorial (recursively)
    prev_factorial = factorial(n-1)
	result = n * next_factorial
    print('N:', n, 'PREV:', prev_factorial, 'RES:', result)
    return result
​
factorial(10)
​
​
print('\n=======\n')
​
​
print('FIBONACCI')
# 0, 1, 1+0=1, 1+1=2, 1+2= 3, 2+3=5...
# return arr of all numbers up to that point
cache = {1: 0, 2: 1}
def fibonacci(n):
    print('CALL:', n)
    # if arr[n] exists, return it
    if n not in cache:
    	# sum up two previous numbers
    	prev1 = fibonacci(n-1)
		print('CALLED:', n, 'P1:', prev1)
    	prev2 = fibonacci(n-2)
		print('CALLED:', n, 'P2:', prev2)
    	result = prev1 + prev2
		# cache the result for future calls
    	cache[n] = result
    	print('N:', n, 'P1:', prev1, 'P2:', prev2, 'RES:', result)
    return cache[n]
​
fibonacci(10)
print('\n-------\n')
fibonacci(20)