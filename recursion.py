"""Recursion exercise"""
def factorial(n):
	print('factorial being called:{}'.format(n))
	if n == 1:
		res = n
	else:
		res = n * factorial(n-1)
		print('immediate result is:{}'.format(res))
	return res

def fibonacci_sequence(n):
	print('fib being called:{}'.format(n))
	if n == 0 or n == 1:
		fib = n
	else:
		fib = fibonacci_sequence(n-1) + fibonacci_sequence(n-2)
		print ('immediate result is:{}'.format(fib))
	return fib

def fib_memo(n, memo={0:0, 1:1}):
	if n not in memo:
		print('fib_memo being called:{}'.format(n))
		memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
		print('immediate resutl is:{}'.format(memo[n]))
	return memo[n]

def multiples_3(n):
	"""compute n*3 recursively"""
	print('multitples being called:{}'.format(n))
	if n == 1:
		res = 3
	else:
		res = multiples_3(n-1) + 3
		print('immediate result:{}'.format(res))
	return res

def sum(n):
	if n == 1:
		res = n
	else:
		res = sum(n-1) + n
	return res

def Pascal_triangle(n, memo={ }):
	if n == 1:
		memo[n] = [1]
	else:
		p_line, memo = Pascal_triangle(n-1, memo)
		memo[n] = [1]
		for ind in range(len(p_line)-1):
			memo[n].append(p_line[ind]+p_line[ind+1])
		memo[n].append(1)
	return memo[n], memo

def seive(n):
	"""Find all prime numbers up to n."""
	L = [i for i in range(2, n+1)]
	pointer = 0
	val = L[pointer]
	while pointer <= len(L)**0.5: 
		mul = 2*val
		while mul <= n:
			try:
				L.remove(mul)
			except ValueError:
				mul += val 
		pointer += 1
		val = L[pointer]
	return L


print(seive(100))





