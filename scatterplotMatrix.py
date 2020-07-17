import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import is_numeric_dtype
from scipy.stats import pearsonr


# Bring dataset into memory
iris = pd.read_csv(r"G:\My Drive\iris.csv")

# Verify the structure of the data
iris.head(10)
iris.info()

# Make any necessary datatype changes
iris["Sepal.Length"] = iris["Sepal.Length"].astype(float)

# Isolate only those columns which are numeric/continuous
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
#iris = iris.select_dtypes(include=numerics)

# Output Scatterplot Version 1
def reg_coef(x,y,label=None,color=None,**kwargs):
    ax = plt.gca()
    r,p = pearsonr(x,y)
    ax.annotate('r = {:.2f}'.format(r), xy=(0.5,0.5), \
                xycoords='axes fraction', ha='center')
    ax.set_axis_off()

g = sns.PairGrid(iris, hue="Species")
g.map_diag(sns.distplot)
g.map_lower(sns.regplot)
g.map_upper(reg_coef)


# Output Scatterplot Version 2
g = sns.PairGrid(iris, hue="Species")
g = g.map_diag(plt.hist)
g = g.map_offdiag(plt.scatter)
g = g.add_legend()
