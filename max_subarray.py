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
	



problem = generate_probblem(5)
print(problem)
# max_pro, buy, sell = brute_force(problem)
# print('max_prof:{}, buy:{}, sell:{}'.format(max_pro, buy, sell))
cip = change_in_price(problem)
print(cip)
