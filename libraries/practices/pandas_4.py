import pandas as pd
import matplotlib.pyplot as plt

# Data
df_csv3 = pd.read_csv("resources/df3")
print(df_csv3.head())
print(df_csv3.info())


# Exercises: recreate the different required plots
df_csv3.plot.scatter(x='a', y='b', c='red', s=50, figsize=(12, 3))
plt.show()

df_csv3['a'].plot.hist()
plt.show()

plt.style.use('ggplot')
df_csv3['a'].plot.hist(bins=25, alpha=0.5)
plt.show()

df_csv3[['a', 'b']].plot.box()
plt.show()

df_csv3['d'].plot.kde()
plt.show()

df_csv3['d'].plot.density(lw=5, ls='--')
plt.show()

df_csv3.iloc[0:30].plot.area(alpha=0.4)
plt.show()

f = plt.figure()  # create a figure to use for the legend
df_csv3.iloc[0:30].plot.area(alpha=0.4, ax=f.gca())
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()
