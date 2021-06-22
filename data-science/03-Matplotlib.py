"""
BASIC CONCEPTS:
-Matplotlib allows you to create reproducible figures programmatically.
-Matplotlib has an object oriented API that allow us to instantiate figure objects and then call methods or attributes
from that object.

MATPLOTLIB FIGURE
-Figure keeps track of all the child Axes, a smattering of 'special' artists (title, legends, etc) and the canvas.
-We can create figure in different ways:
  -fig = plt.figure()            - an empty figure with no Axes
  -fig, ax = plt.subplots()      - a figure with a single Axes
  -fig, axs = plt.subplots(n, m) - a figure with a nxm grid of Axes
"""

import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from random import sample



# -----------------BASIC CONCEPTS-----------------

# Create and display plots
# plot(x_axis, y_axis,  *kwargs) -> draw a plot using input values
x = np.linspace(0, 5, 11)
y = x ** 2
plt.plot(x, y, color='r')
plt.show()

# Set labels and title name
plt.xlabel('X Axis Title Here')
plt.ylabel('Y Axis Title Here')
plt.title('String Title Here')

# Create multiple plots
# First, create a subplot, then define the plot
# subplot(nrows, ncols, subplot_number) -> create subplots in the same canvas
# nrows, ncols -> define the number of rows and columns of the subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r--')
plt.subplot(1, 2, 2)
plt.plot(y, x, 'g*-')
plt.show()






# -----------------MATPLOTLIB OOP-----------------

# Create an empty figure
fig = plt.figure()

# Customize your figure
# figsize -> set size of a figure (size must a be a tuple (m, n)
# DPI     -> set dpis of a figure (int value)
fig_modified = plt.figure(figsize=(8, 4), dpi=100)

# Set axes parameters (left, bottom, width, height) in range 0-1 and then plot them
axes = fig.add_axes([0.1, 0.1, 0.5, 0.5])
axes.plot(x, y, 'b')

# Set labels and title. We can use individual methods or just set method
axes.set_xlabel('Set X Label')
axes.set_ylabel('Set y Label')
axes.set_title('Set Title')
axes.set(xlabel='Set X Label', ylabel='Set Y Label', title='Set Title')

# Add a legend to a figure
# legend(loc=n) -> set plot legend. A label argument will be required in plot()
# loc -> optional, specify where in the figure the legend is to be drawn (0 by default, optimal location)
fig_legend = plt.figure()
ax = fig_legend.add_axes([0, 0, 1, 1])
ax.plot(x, x**2, label="x**2")
ax.plot(x, x**3, label="x**3")
ax.legend(loc=0)

# Add a grid to a plot
fig_grid = plt.figure()
ax = fig_legend.add_axes([0, 0, 1, 1])
ax.plot(x, x**2, label="x**2")
ax.grid()

# Save your figure
# savefig(path, dpi=n) -> save figure to the given path using any image format
# dpi -> specify the DPI
fig.savefig("filename.png")
fig.savefig("filename.jpg", dpi=200)

# Multiple axes can be set to a figure
fig2 = plt.figure()
axes1 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])  # main axes
axes2 = fig2.add_axes([0.2, 0.5, 0.4, 0.3])  # inset axes
axes1.plot(x, y, 'b')
axes2.plot(y, x, 'r')
axes1.set(xlabel='X_label_axes1', ylabel='Y_label_axes1', title='Axes 1 Title')
axes2.set(xlabel='X_label_axes2', ylabel='Y_label_axes2', title='Axes 2 Title')

# Avoid overlapping of figures/subplots
# fig.tight_layout() -> automatically adjusts the positions of the axes on the figure
# plt.tight_layout() -> automatically adjusts the positions of the axes on the plot
fig.tight_layout()
plt.tight_layout()






# -----------------MATPLOTLIB OOP - SUBPLOTS-----------------

# Create a figure with defined axes
# Axes parameters are set automatically based on the number rows and columns
fig3, axes3 = plt.subplots()  # single axes
fig4, axes4 = plt.subplots(nrows=1, ncols=2, figsize=(4, 3))  # a grid of axes

# Since axes is an array, we iterate it to set labels and titles for all the plots
for ax in axes4:
    ax.plot(x, y, 'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

# We can plot indivual axis
axes4[0].plot(x, y)
axes4[0].set_title('First Plot')
axes4[1].plot(y, x)
axes4[1].set_title('Second Plot')
plt.tight_layout()

# Tune subplot layout using subplot_adjust()
# left   -> left side of the subplots of the figure
# rigth  -> right side of the subplots of the figure
# bottom -> bottom of the subplots of the figure
# top    -> top of the subplots of the figure
# wspace -> amount of width reserved for space between subplots, expressed as a fraction of the average axis width
# hspace -> amount of height reserved for space between subplots, expressed as a fraction of the average axis height
plt.subplots_adjust(left=0.2, bottom=0.1, right=0.8, top=0.8, wspace=0.2, hspace=0.2)






# -----------------CUSTOMIZATION-----------------

# Parameters to customize plots by adding them to plot() or subplot()
# grid=True/False -> display or hide grid
# color, c        -> set color for plots, using names or RGB hex codes
# cmap            -> map from data values to color space
# alpha           -> set line transparency
# linewidth, lw   -> set linewidth to a multiple of the default value
# linestyle, ls   -> set linestyle to one of the posible values ('-', '--', '–', '-.', ':', 'steps')
# linecolor       -> set color of the lines that divides the cells
# marker          -> add markers ('+', 'o', '*', 's', ',', '.', '1', '2', '3', ...) to the plot
# markersize      -> set size to added markers
# markerfacecolor -> set color to added markers
fig5, axes5 = plt.subplots(figsize=(12, 6))
axes5.plot(x, x+2, color="red", alpha=0.5, linewidth=0.50, linestyle='-', marker='o', markersize=5)
axes5.plot(x, x+5, color="blue", lw=1, ls='-.', marker='*', markersize=2, markerfacecolor='red')

# set_dashes() -> set dash to a plot
line, = axes5.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10])  # format: line length, space length, ...

# set_ylim()    -> set y range for a plot
# set_xlim()    -> set x range for a plot
# axis('tight') -> get axes automatically getting tight
fig6, axes6 = plt.subplots(1, 3, figsize=(12, 4))
axes6[0].plot(x, x**2, x, x**3)
axes6[0].set_title("default axes ranges")
axes6[1].plot(x, x**2, x, x**3)
axes6[1].axis('tight')
axes6[1].set_title("tight axes")
axes6[2].plot(x, x**2, x, x**3)
axes6[2].set_ylim([0, 60])
axes6[2].set_xlim([2, 5])
axes6[2].set_title("custom axes range")

# Use stylesheets create a set of style rules that your plots follow
# plt.style.use('stylesheet') -> set a stylesheet to use in your plots
plt.style.use('ggplot')
plt.style.use('bmh')
plt.style.use('dark_background')
plt.style.use('fivethirtyeight')






# -----------------SPECIAL PLOT TYPES-----------------

# Scatter plots
# s -> indicate size based off another column (s must be a string, scalar or array_like)
df_csv1 = pd.read_csv(r'C:\Users\ponce\Documents\Education\Software Engineering\Python\Course - Python For Data '
                      r'Science\07- Data Visualization with Pandas\df1')
plt.scatter(x, y)
plt.scatter(x='A', y='B', s=df_csv1['C']*200)
plt.scatter(x='A', y='B', s=50)

# Histograms
# bins -> set the number of intervals
data = sample(range(1, 1000), 100)
plt.hist(data, bins=20)

# Pie chart
# explode -> specify the fraction of the radius with which to offset each wedge
# autopct -> display the percent value using Python string formatting.
data = ['40', '20', '17', '8', '5', '10']
labels = ['IT', 'Finance', 'Marketing', 'Admin', 'HR', 'Operations']
plt.pie(x=data, labels=labels, explode=(0.05, 0, 0, 0, 0, 0), autopct='%1.1f%%', startangle=70)
plt.axis('equal')  # ensure pie chart is displayed as a circle

# Rectangular box plot
plt.boxplot(data, vert=True, patch_artist=True)
