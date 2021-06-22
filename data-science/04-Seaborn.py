"""
BASIC CONCEPTS:
-Seaborn is a library built on top of matplotlib.
-It allow you to create beautiful plots easily.
-We can combine different types of plots in one figure to improve representation

DISTRIBUTION PLOTS:
-Displot: plot the distribution of a univariate set of observations.
-Jointplot: plot a match up of two distplots for bivariate data.
-Pairplot: plot pairwise relationships across an entire dataframe (for the numerical columns) and supports
a color hue argument (for categorical columns).
-Rugplot: plot a dash mark for every point on a univariate distribution. They are the building block of a KDE plot.
-Kdeplots: or Kernel Density Estimation plots, they replace every single observation with a Gaussian (Normal)
distribution centered around that value.

CATEGORICAL PLOTS:
-Bartplot and counterplot: get aggregate data of a categorical feature in your data.
    -Barplot -> or box-and-whisker plot, allow you to aggregate the categorical data based of some function.
    -Counterplot -> same as barplot except the estimator is explicitly counting the number of occurrences.
-Boxplot and violinplot: show the distribution of categorical data.
    -Boxplot -> boxes show the quartiles of the dataset, while the whiskers extend to show the rest of the distribution,
    except for points that are determined to be “outliers”.
    -Violinplot -> features a kernel density estimation of the underlying distribution of data.
-Stripplot and swarmplot: draw a scatterplot where one variable is categorical
    -Stripplot -> in stripplot points are overlapped
    -Swarmplot -> in swarmplot points are adjusted (only along the categorical axis) so that they don’t overlap
-Factorplot: take in a kind parameter to adjust the plot

MATRIX PLOTS:
-Heatmap: plot data as color-encoded matrices and can also be used to indicate clusters within the data. In order to
work properly, your data should already be in a matrix form.
-Clustermap: uses hierarchal clustering to produce a clustered version of the heatmap

GRIDS:
-Grids are general types of plots that allow you to map plot types to rows and columns of a grid.
-This helps you create similar plots separated by features.
-Types of grids:
    -PairGrid  -> subplot grid for plotting pairwise relationships in a dataset.
    -FacetGrid -> general way to create grids of plots based off of a feature.
    -JointGrid -> general version for jointplot() type grids.

REGRESSION PLOTS:
-lmplot allows you to display linear models and to split up those plots based off of features, as well as coloring
the hue based off of features.
"""

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats



# DATA
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
iris = sns.load_dataset('iris')



# -----------------DISPLOT-----------------

# Create default displot
sns.displot(tips['total_bill'])
plt.show()

# Displot arguments
# kde  -> set True(display) or False(hide) kde layer
# bins -> set the division of the entire range of values into a series of intervals
sns.displot(tips['total_bill'], kde=False, bins=30)
plt.show()




# -----------------JOINTPLOT-----------------

# Create default jointplot
sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter')
plt.show()

# Jointplot arguments
# x, y -> set -x and -y axes.
# data -> choose your datasource
# kind -> select visual representation (scatter by default, reg, resid, kde, hex)
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
plt.show()




# -----------------PAIRPLOT-----------------

# Create default pairplot
sns.pairplot(tips)
plt.show()

# Pairplot arguments
# hue     -> set color representation based on categorical argument (for example, sex)
# palette -> set color palette
sns.pairplot(tips, hue='sex', palette='coolwarm')
plt.show()




# -----------------RUGPLOT-----------------

# Create default rugplot
sns.rugplot(tips['total_bill'])




# -----------------KDEPLOT-----------------

# Create a basic kde plot with seaborn
sns.kdeplot(tips['total_bill'])

# Explanation of what kdeplot function does

# We choose a dataset and create a rugplot
dataset = np.random.randn(25)
sns.rugplot(dataset)

# We set up the parameters x-axis, x_min, x_max and bandwidth
x_min = dataset.min() - 2
x_max = dataset.max() + 2
x_axis = np.linspace(x_min, x_max, 100)
bandwidth = ((4 * dataset.std() ** 5) / (3 * len(dataset))) ** .2

# We create an empty kernel list and plot each basis function
kernel_list = []
for data_point in dataset:
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point, bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    # Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    # Plot x_axis and kernel
    plt.plot(x_axis, kernel, color='grey', alpha=0.5)

# We set -y limits
plt.ylim(0, 1)

# Now, we can get the kde plot by summing these basis functions and plot the figure
sum_of_kde = np.sum(kernel_list, axis=0)
fig = plt.plot(x_axis, sum_of_kde, color='indianred')
plt.suptitle("Sum of the Basis Functions")  # set title
plt.yticks([])  # get rid of y-tick marks
sns.rugplot(dataset, c='indianred')  # add the initial rugplot
plt.show()




# -----------------BARPLOT AND COUNTPLOT-----------------

# Create basic bartplot
sns.barplot(x='sex', y='total_bill', data=tips)
plt.show()

# Bartplot arguments
# x, y      -> set -x and -y axes.
# data      -> choose your datasource
# estimator -> set estimator function (mean by the default)
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
plt.show()

# Create basic counterplot
sns.countplot(x='sex', data=tips)
plt.show()




# -----------------BOXPLOT AND VIOLINPLOT-----------------

# Create basic boxplot
sns.boxplot(x="day", y="total_bill", data=tips, palette='rainbow')
plt.show()

# Create basic violinplot
sns.violinplot(x="day", y="total_bill", data=tips, palette='rainbow')
plt.show()

# Boxplot and violinplot arguments
# x, y    -> set -x and -y axes.
# data    -> choose your datasource
# orient  -> set plot orientation
# palette -> set color palette
# hue     -> set color representation based on categorical argument (for example, sex)
sns.boxplot(data=tips, palette='rainbow', orient='h')
sns.boxplot(x="day", y="total_bill", data=tips, hue="smoker", palette="coolwarm")
sns.violinplot(x="day", y="total_bill", data=tips, hue='sex', palette='Set1')
sns.violinplot(x="day", y="total_bill", data=tips, hue='sex', split=True, palette='Set1')




# -----------------STRIPPLOT AND SWARMPLOT-----------------

# Create basic stripplot
sns.stripplot(x="day", y="total_bill", data=tips)
plt.show()

# Create basic swarmplot
sns.swarmplot(x="day", y="total_bill", data=tips)
plt.show()

# Stripplot and swarmplot arguments
# x, y                     -> set -x and -y axes.
# data                     -> choose your datasource
# jitter=True/float_number -> set amount of jitter along the categorical axis. Use True for good default
# hue                      -> set color representation based on categorical argument (for example, sex)
# palette                  -> set color palette
# split                    -> split categorical data in different color representations
# size                     -> set size of the plot
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, hue='sex', palette='Set1')
sns.swarmplot(x="day", y="total_bill", data=tips)
sns.swarmplot(x="day", y="total_bill", hue='sex', data=tips, palette="Set1", split=True, size=5)

# Swarmplots combines really well with violinplots
sns.violinplot(x="tip", y="day", data=tips, palette='rainbow')
sns.swarmplot(x="tip", y="day", data=tips, color='black', size=3)
plt.show()




# -----------------FACTORPLOT-----------------

# Create a basic factorplot
sns.catplot(x='sex', y='total_bill', data=tips, kind='bar')




# -----------------HEATMAP-----------------

# Create basic heatmap
# We use corr() to organize our data in matrix form
sns.heatmap(tips.corr())

# Heatmap arguments
# cmap             -> map from data values to color space
# annot=True/False -> write the data value in each cell
# linewidths       -> set width of the lines that divides the cells
# linecolor        -> set color of the lines that divides the cells
sns.heatmap(tips.corr(), cmap='coolwarm', annot=True)

# Example of heatmap. We need to organize data first
flights.pivot_table(values='passengers', index='month', columns='year')
pvflights = flights.pivot_table(values='passengers', index='month', columns='year')
sns.heatmap(pvflights, cmap='magma', linecolor='white', linewidths=1)




# -----------------CLUSTERMAP-----------------

# Create basic clustermap
sns.clustermap(pvflights)

# Clustermap arguments
# cmap           -> mapping from data values to color space
# standard_scale -> standardize rows (0) or columns (1), meaning for each row or column, subtract the minimum and
# divide each by its maximum
sns.clustermap(pvflights, cmap='coolwarm', standard_scale=1)






# -----------------GRIDS-----------------

# PairGid
# We create the PairGrid and then we map to the grid
g = sns.PairGrid(iris)
g.map(plt.scatter)

# We can map to upper,lower, and diagonal
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# FacetGrid
# We create the FacetGrid and set columns/rows from the dataset
# Then we map to the grid and set x value ("total_bill" in this case)
g = sns.FacetGrid(tips, col="time", row="smoker")
g.map(plt.hist, "total_bill")
g = sns.FacetGrid(tips, col="time")
g.map(plt.hist, "total_bill")
g = sns.FacetGrid(tips, row="time")
g.map(plt.hist, "total_bill")

# We can set a hue parameter in a FacetGrid
g = sns.FacetGrid(tips, col="time", row="smoker", hue='sex')
g.map(plt.scatter, "total_bill", "tip")


# JointGrid
g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = g.plot(sns.regplot, sns.distplot)






# -----------------REGRESSION PLOTS-----------------

# Display a linear model using lmplot():
sns.lmplot(x='total_bill', y='tip', data=tips)

# lmplot() arguments
# x, y    -> set -x and -y axes.
# data    -> choose your datasource
# hue     -> set color representation based on categorical argument (for example, sex)
# palette -> set color palette
# aspect  -> set aspect ratio
# size    -> set size of the plot
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm', aspect=0.6, size=8)

# Adding markers
# Use scatter_kws argument to modify 's' that references to size
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm',
           markers=['o', 'v'], scatter_kws={'s': 100})






# -----------------STYLE AND COLOR-----------------

# Set style to your plot
# Style examples: whitegrid, drakgrid, ticks
sns.set_style('whitegrid')
sns.countplot(x='sex', data=tips)
sns.set_style('ticks')
sns.countplot(x='sex', data=tips, palette='deep')

# Remove spine
# despine(left=, bottom=) -> remove top and right spine
# left=True/False   -> remove also left spine
# bottom=True/False -> remove also bottom spine
sns.countplot(x='sex', data=tips)
sns.despine()
sns.countplot(x='sex', data=tips)
sns.despine(left=True, bottom=True)

# Modify size and aspect for non grid type plot
plt.figure(figsize=(12, 3))
sns.countplot(x='sex', data=tips)
sns.lmplot(x='total_bill', y='tip', size=2, aspect=4, data=tips)

# Scale and context
sns.set_context('poster', font_scale=4)
sns.countplot(x='sex', data=tips, palette='coolwarm')
