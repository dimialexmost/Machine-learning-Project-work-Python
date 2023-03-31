import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_openml

# Load Boston Housing Dataset
boston = fetch_openml(name='boston')
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.Series(boston.target, name='MEDV')
df = pd.concat([X, y], axis=1)

# Create a big plot with many subplots
fig, axs = plt.subplots(nrows=13, ncols=13, figsize=(20, 20))

# Plot scatterplots for all pairs of features
for i, feature1 in enumerate(df.columns[:-1]):
    for j, feature2 in enumerate(df.columns[:-1]):
        if i == j:
            axs[i, j].hist(df[feature1])
        else:
            axs[i, j].scatter(df[feature2], df[feature1])
        if j == 0:
            axs[i, j].set_ylabel(feature1)
        if i == len(df.columns[:-1]) - 1:
            axs[i, j].set_xlabel(feature2)

# Adjust subplot spacing
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95, hspace=0.4, wspace=0.4)

# Show the plot
plt.savefig('boston_housing_plot.png')
plt.show()