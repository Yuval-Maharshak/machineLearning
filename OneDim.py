import random


def train(D, depth=10):
	T = [random.randint(1, 100),random.randint(1, 100)]

	for i in range(depth):
		T = create_next(D, T)
	return T

def apply_T(T, x):
	return T[0] * x + T[1]

def create_next(D, T):
	sqrsum = square_sum(D, T)
	c_derivative = c_diff(D, T)
	b_derivative = b_diff(D, T)
	if c_derivative != 0:
		T[0] = T[0] + (sqrsum / c_derivative)
	if b_derivative != 0:
		T[1] = T[1] + (sqrsum / b_derivative)
	return T

def square_sum(D, T):
	summ = 0
	for x in D:
		summ += (x[1] - apply_T(T, x[0]))**2
	return summ

def c_diff(D, T):
	summ = 0
	for x in D:
		summ += (x[1] - apply_T(T, x[0])) * x[0]
	summ *= 2
	return summ
def b_diff(D, T):
	summ = 0
	for x in D:
		summ += x[1] - apply_T(T, x[0])
	return 2 * summ

Data = [(1, 2), (2, 4), (3, 6)]
func = train(Data)

print(func)
print([apply_T(func, n) for n in range(0, 200)])
