import matplotlib.pyplot as plt
import numpy as np


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(100000)
print(len(x) ,x )

# the histogram of the data
# n = x
# bins = 100
n, bins, patches = plt.hist(x, 100 ,normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
