import numpy as np 
import numpy.random as rand 
import matplotlib.pyplot as plt

def generate_probblem(n):
	"""Generate problem of length n."""
	return rand.randint(100, size=n)

def plot_problem(prob):
	plt.plot(prob)
	plt.xlabel('day')
	plt.ylabel('price')
	plt.title('virtual stock market')
	plt.show()

def brute_force(prob):
	"""Brute force to find the best buy/sell pair."""
	max_profit = -1
	for ind in range(len(prob)):
		buy = prob[ind]
		for s in range(ind, len(prob)):
			sell = prob[s]
			prof = sell - buy
			if prof > max_profit:
				max_profit = prof
				best_buy = buy 
				best_sell = sell  
	return max_profit, best_buy, best_sell  

def change_in_price(prob):
	"""Transform the problem into maximum subarray problem."""
	cip = np.zeros(len(prob)-1)
	for ind in range(len(prob)-1):
		cip[ind] = prob[ind+1] - prob[ind]
	return cip 

def find_crossing_subarray(cip, low, mid, high):
	left_Maxsum = -1000
	right_Maxsum = -1000
	right_sum = 0
	left_sum = 0
	max_left = 0
	max_right = 0
	for i in reversed(range(low, mid)):
		# lower half
		 left_sum = left_sum + cip[i]
		 if left_sum > left_Maxsum:
		 	left_Maxsum = left_sum
		 	max_left = i
	for j in range(mid, high):
		# right half
		right_sum += cip[j]
		if right_sum > right_Maxsum:
			right_Maxsum = right_sum
			max_right = j
	return (max_left, max_right, left_Maxsum + right_Maxsum)

def max_subarray(cip, low, high):
	# print(cip, low, high)
	if high == low:
		# print(">", cip[low])
		return (low, high, cip[low])
	else:
		mid = int((low + high) / 2)
		(left_low, left_high, left_sum) = max_subarray(cip, low, mid)
		(right_low, right_high, right_sum) = max_subarray(cip, mid+1, high)
		(cross_low, cross_high, cross_sum) = find_crossing_subarray(cip, low, mid, high)
		if left_sum >= right_sum and left_sum >= cross_sum:
			return (left_low, left_high, left_sum)
		elif right_sum >= left_sum and right_sum >= cross_sum:
			return (right_low, right_high, right_sum)
		else: 
			return (cross_low, cross_high, cross_sum)


problem = generate_probblem(10)
print('problem:', problem)
max_pro, buy, sell = brute_force(problem)
print('max_prof:{}, buy:{}, sell:{}'.format(max_pro, buy, sell))
cip = change_in_price(problem)
print('cip', cip)
(low, high, Sum) = max_subarray(cip, 0, len(cip)-1)
print(low, high, Sum)
