import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys
with open("Histogram_example.tsv") as f:
    read_tsv= csv.reader(f, delimiter="\t")
if len(sys.argv) <2:
    print("missing file name")
    exit()
filename= sys.argv[0]
arg_column= sys.argv[1]
column = 2
if arg_column.startswith ('-f'):
    column = arg_column [2:]
elif not arg_column.startswith ('-f'):
    column = 2
df= pd.read_table("Histogram_example.tsv")
datafile= sys.argv[2]
with open(sys.argv[2]) as f:
    plt.hist("Histogram_example.tsv",["arg_column"])
    plt.grid(False)
    plt.show()
plt.savefig('histogram_example.png')
