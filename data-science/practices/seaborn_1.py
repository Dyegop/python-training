import seaborn as sns
import matplotlib.pyplot as plt

# Data
titanic = sns.load_dataset('titanic')
# titanic.to_csv('C:\\Users\\ponce\\Downloads\\new_csv.csv')
# print(titanic.head())

# Style
sns.set_style('whitegrid')


# Exercises: recreate the different required plots

sns.jointplot(x='fare', y='age', data=titanic, kind='scatter')
plt.show()

sns.displot(titanic['fare'], bins=30, kde=False, color='red')
plt.show()

sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')
plt.show()

sns.swarmplot(x='class', y='age', data=titanic, palette='Set2')
plt.show()

sns.factorplot(x='sex', y='survived', data=titanic, kind='bar')
plt.show()

titanic['count'] = titanic.value_counts('survived')
sns.catplot(x='sex', y="count", data=titanic, kind='bar', palette='deep')
plt.show()
# alternative: sns.countplot(x='sex', data=titanic, palette='deep')

sns.heatmap(titanic)
plt.show()

sns.heatmap(titanic.corr(), cmap='coolwarm')
plt.show()

g = sns.FacetGrid(titanic, row="sex")
g = g.map(plt.hist, 'age')
plt.show()
