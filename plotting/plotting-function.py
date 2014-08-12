#!/usr/bin/env python

#...for the file handling stuff.
import os, inspect

#...for the time handling stuff.
import time

#...for the plotting.
import matplotlib.pyplot as plt

#...for font handling.
from matplotlib import rc

# The font settings.
font = {'family':'serif', 'weight':'regular', 'size':8 }

# Change the default font settings.
rc('font', **font)

#...for setting global plot constants.
from matplotlib import rcParams

rcParams['axes.linewidth'] = 0.7

#...for the MATH.
import numpy as np

# Get the path of the current directory
path = os.path.dirname(os.path.abspath(      \
    inspect.getfile(inspect.currentframe())) \
    )

if __name__ == "__main__":

    print("")
    print("###########################################")
    print("   CERN@school: Making Plots with Python   ")
    print("###########################################")
    print("*")
    print("*  Time and date     : %s"  \
        % (time.strftime("%H:%M, %A %d %B %Y (%Z)")))
    print("*  Working directory : '%s'" % (path))
    print("*")
    print("###########################################")
    print("")

    # Prepare our working environment.
    plt.close('all')

    ## The figure upon which to display the plot.
    plot = plt.figure(101,                  \
                      figsize = (4.0, 4.0), \
                      dpi=150,              \
                      facecolor="white",    \
                      edgecolor="white"     \
                      )

    # Adjust the axis positions to allow for the labels.
    plot.subplots_adjust(bottom=0.19, left=0.19)

    ## The plot axes.
    plotax = plot.add_subplot(111)

    # Set the x axis label.
    plotax.set_xlabel('The $x$ axis')

    # Set the y axis label.
    plotax.set_ylabel('The $y$ axis')

    # Define the independent variable - energy (E).

    ## Array for the x values.
    x_Energy_keV = np.arange(0.0, 100.1, 0.1)

    # Print out the values to check what you're doing.
    print("* The x values:")
    print x_Energy_keV
    print("*")

    # Define the calibration constants. These examples are
    # taken from TPX0, pixel 0 => (  0,  0).

    ## The calibration constant a.
    a =    2.24852

    ## The calibration constant b.
    b =   80.6086

    ## The calibration constant c.
    c =  252.004

    ## The calibration constant t.
    t =   -0.62902

    ## The surrogate function.
    surrofunc = a * x_Energy_keV + b - (c / (x_Energy_keV - t))

    ## The 2D line plot of the surrogate function.
    surroline, = plotax.plot(x_Energy_keV, surrofunc, 'g')

    # Set the limits of the y axis.
    plotax.set_ylim(ymin=0.0, ymax = 350.0)

    # Set the x axis label.
    plotax.set_xlabel('Energy $E$ / keV', labelpad=10)

    # Set the y axis label.
    plotax.set_ylabel('ToT counts', labelpad=10)

    # Add a legend.
    plotax.legend([surroline],           \
                  ['TPX0, pixel 00000'], \
                  loc='upper left',      \
                  borderpad=0.6,         \
                  borderaxespad=1.0,     \
                  frameon=None,          \
                  fancybox=True,         \
                  fontsize=8             \
                  )

    # Add a grid.
    plotax.grid(1)

    # Save the plot.
    plot.savefig(path + "/myplot.png")

    # Show the plot.
    plot.show()

    # Wait for a user response before closing the matplotlib window
    raw_input('Press any key to continue...')
