import matplotlib.pyplot as plt

plt.figure(figsize=(18 , 18))

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ms--')
plt.axis([0, 6, 0, 20])

plt.grid(True); plt.show()


