from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

iris = datasets.load_iris()

data = PCA(n_components=2).fit_transform(iris.data)

_, ax = plt.subplots()
scatter = ax.scatter(data[:, 0], data[:, 1], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
_ = ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)
plt.show()
print(data)
