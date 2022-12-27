import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(snakemake.input[0])
# df = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

fig, ax = plt.subplots()
df.hist("sepal.length", by='variety', bins=30,ax=ax)
# fig.savefig('tmp.png')
fig.savefig(snakemake.output.plot)