import matplotlib.pyplot as plt
import itertools

fig=plt.figure()
ax=fig.add_subplot(111)
all_data = [[1,10],[2,10],[3,10],[4,10],[5,10],[3,1],[3,2],[3,3],[3,4],[3,5]]
plt.plot(
    *zip(*itertools.chain.from_iterable(itertools.combinations(all_data, 2))),  color = 'brown', marker = 'o')

plt.show()