#%%
import markdown
from IPython.core.display import display, HTML
def md(str):
    display(HTML(markdown.markdown(str + "<br />")))

#%%
md("""
# Exploration: Multi-order analysis of [time-stamped social network data](https://github.com/IngoScholtes/eurocss2019-tutorial/tree/master/data)

**Ingo Scholtes**  
Data Analytics Group  
Faculty of Mathematics and Natural Sciences  
University of Wuppertal, DE  


**September 2 2019**

In the last (open-ended) exploration, you get the chance to apply multi-order representation in the analysis of real data. In addition to the data from session 1, we will consider data that we provide in the SQLite database `temporal_networks.db`. You can check which tables it contains by checking the `metadata` table:
""")

#%% In [None]
import pathpy as pp
import sqlite3

con = sqlite3.connect('data/temporal_networks.db',)
con.row_factory = sqlite3.Row

for row in con.execute('SELECT * from metadata'):
    print('{0} \t\t {1}'.format(row['tag'], row['name']))

#%%
md("""
Details on the origin of these data can be found [here](https://github.com/IngoScholtes/kdd2018-tutorial/tree/master/data). Below, we include boilerplate code to load these data sets into the `TemporalNetwork` class in `pathpy`:
""")

#%% In [None]
table = 'manufacturing_email'

# Check whether network is directed or not
directed_network = bool(con.execute("SELECT directed FROM metadata WHERE tag='{0}'".format(table)).fetchone()['directed'])
t = pp.TemporalNetwork.from_sqlite(con.execute('SELECT source, target, time FROM ' + table), 
                                   directed=directed_network)
print(t)

#%%
md("""
Using these data and the methods introduced in our tutorial, you could study the following problems (in ascending order of difficulty):

- Use the `MultiOrderModel` class to learn the optimal order of a temporal network. How does the detected optimal order change with the time scale $\delta$ that you use in the extraction of causal paths?
- Study the change in the algebraic connectivity between the second-order model and the second-order null model fora temporal network data set. Who can you interpret your findings?
- Perform a spectral clustering of a temporal network based on the Laplacian of higher-order networks at different orders. How does the clustering differ from a first-order clustering?

Again, these are only suggestions and you are welcome to use the time to study other data sets or questions that come to your mind. We'll be happy to assist with the analysis.
""")

#%% In [None]


