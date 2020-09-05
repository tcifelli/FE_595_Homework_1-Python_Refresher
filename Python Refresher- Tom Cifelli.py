import matplotlib.pyplot as plt
import matplotlib.ticker as ticks
import numpy as np


def printWaves(start = 0, end = np.pi * 2, pointsPerFullRotation = 100):
    resolution = ((end - start) / pointsPerFullRotation) * ((end - start) / (np.pi * 2))
    inputs = np.arange(start, end, resolution)
    sinOutputs = np.sin(inputs)
    cosOutputs = np.cos(inputs)

    plt.xlabel("Input")
    plt.ylabel("Amplitude")
    plt.title("Trig Waves")
    plt.grid(True, which = 'both')
    plt.axhline(y=0, color='k')
    ax = plt.gca()
    ax.plot(inputs / np.pi, sinOutputs, label = "sine")
    ax.plot(inputs / np.pi, cosOutputs, label = "cosine")
    ax.xaxis.set_major_formatter(ticks.FormatStrFormatter('%g $\pi$'))
    ax.xaxis.set_major_locator(ticks.MultipleLocator(base=0.5))
    ax.legend(loc = "upper right")
    plt.show()


def main():
    printWaves()


if __name__ == "__main__":
    main()
