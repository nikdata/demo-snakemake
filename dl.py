import pandas as pd

# input/output from snakemake
# in_file = snakemake.input["sample"]
# out_file = output[0]

# read in csv file from URL
df = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

# write out file
df.to_csv(snakemake.output.raw_data, index=False)