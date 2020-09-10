import matplotlib.pyplot as plt #the general plotting framework
import matplotlib.ticker as ticks #used to put the pi symbol on the x-axis
import numpy as np #contains sine and cosine functions

#generate a plot of sine and cosine waves
def printWaves(start = 0, #start of the wave
               end = np.pi * 2, #end of the wave
               pointsPerFullWavelength = 100): #points to plot per full wavelength (higher = smoother)
    #generate datapoints to plot
    resolution = (np.pi * 2) / pointsPerFullWavelength
    inputs = np.arange(start, end, resolution)
    sinOutputs = np.sin(inputs)
    cosOutputs = np.cos(inputs)
    tanOutputs = np.tan(inputs)

    #generate plot
    plt.ylim(-1,1)
    plt.xlabel("Input")
    plt.ylabel("Amplitude")
    plt.title("Trig Waves")
    plt.grid(True, which = 'both')
    plt.axhline(y=0, color='k')
    ax = plt.gca()
    ax.plot(inputs / np.pi, sinOutputs, label = "sine")
    ax.plot(inputs / np.pi, cosOutputs, label = "cosine")
    ax.plot(inputs / np.pi, tanOutputs, label = "tangent")
    ax.xaxis.set_major_formatter(ticks.FormatStrFormatter('%g $\pi$'))
    ax.xaxis.set_major_locator(ticks.MultipleLocator(base=0.5))
    ax.legend(loc = "upper right")
    plt.show()

#functions to run when file is called
def main():
    printWaves()

#runs the main function when file is called
if __name__ == "__main__":
    main()
