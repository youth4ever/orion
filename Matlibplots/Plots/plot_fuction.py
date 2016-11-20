import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(0.0, 5.0, 100)
    y = np.cos(2 * np.pi * x) * np.exp(-x)

    plt.plot(x, y, 'k')
    plt.title('Damped exponential decay')
    plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$')
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.subplots_adjust(left=0.15); plt.grid(); plt.show()

if __name__ == "__main__":
    main()



