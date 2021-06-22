import matplotlib.pylab as plt
import numpy as np

# Data
x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Exercise 1
# Create a figure object called fig using plt.figure()
# Use add_axes to add an axis to the figure canvas at [0.1,0.1,0.8,0.8]
# Plot (x,y) on that axes and set the labels and titles to match the plot below.
fig1 = plt.figure()
ax = fig1.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set(xlabel='x', ylabel='y', title='Title', xlim=([0, 100]), ylim=([0, 200]))
ax.plot(x, y, color='blue')
plt.show()


# Exercise 2
# Create a figure object and put two axes on it, ax1 and ax2. Located at [0.1,0.1,0.8,0.8] and [0.2,0.5,.2,.2]
# Now plot (x,y) on both axes. And call your figure object to show it.
fig2 = plt.figure()
ax2_1 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
ax2_2 = fig2.add_axes([0.2, 0.5, 0.2, 0.2])
ax2_1.set(xlabel='x', ylabel='y', title='Title', xlim=([0, 100]), ylim=([0, 200]))
ax2_2.set(xlabel='x', ylabel='y', title='Title', xlim=([0, 100]), ylim=([0, 200]))
ax2_1.plot(x, y, 'red')
ax2_2.plot(x, y, 'red')
plt.show()


# Exercise 3
# Create the plot below by adding two axes to a figure object at [0.1,0.1,0.8,0.8] and [0.2,0.5,.4,.4]
# Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot
fig3 = plt.figure()
ax3_1 = fig3.add_axes([0.1, 0.1, 0.8, 0.8])
ax3_2 = fig3.add_axes([0.2, 0.5, 0.3, 0.3])
ax3_1.set(xlabel='x', ylabel='z', xlim=([0, 100]), ylim=([0, 10000]))
ax3_2.set(xlabel='x', ylabel='y', title='Zoom', xlim=([20, 22]), ylim=([30, 50]))
ax3_1.plot(x, z, 'blue')
ax3_2.plot(x, y, 'blue')
plt.show()


# Exercise 4
# Use plt.subplots(nrows=1, ncols=2) to create the plot below
# Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style
# See if you can resize the plot by adding the figsize()
fig4, ax4 = plt.subplots(nrows=1, ncols=2)
ax4[0].set(xlim=([0, 100]), ylim=([0, 200]))
ax4[1].set(xlim=([0, 100]), ylim=([0, 10000]))
ax4[0].plot(x, y, color='blue', lw=3, ls='--')
ax4[1].plot(x, z, color='red', lw=3)
plt.show()


# Exercise 5
# List the causes of death and percentile in Ohio state in the year 2012
# Now draw a pie chart using the two data points
death_causes = ['Chronic Disease', 'Unintetional Injuries', 'Alzheimers', 'Infuenza and Pneumonia', 'Sepsis', 'Others']
death_data = ['62', '5', '4', '2', '1', '26']
explode = (0.05, 0, 0, 0, 0, 0)
fig5, ax5 = plt.subplots(figsize=(10, 10))
ax5.set_title('Causes of death')
ax5.pie(x=death_data, labels=death_causes, explode=explode, shadow=True, autopct='%1.1f%%', startangle=70)
ax5.axis('equal')
plt.show()
