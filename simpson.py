import numpy as np

def solve(func, a, b, eps, n):
	S0 = func(a) + func(b)
	h = (b - a) / n
	S1 = sum([func(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1)])
	S2 = sum([func(a + 2 * i  * h) for i in range(1, n // 2)])
	I2 = (h / 3) * (S0 + 4 * S1 + 2 * S2)
	ans = [I2]
	while True:
		I1 = I2
		n *= 2
		h = (b - a) / n
		S2 = S1 + S2
		S1 = sum([func(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1)])
		I2 = (h / 3) * (S0 + 4 * S1 + 2 * S2)
		ans.append(I2)
		if np.abs(I2 - I1) < (15. / 16.) * eps:
			break
	return ans, n