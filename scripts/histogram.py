import pandas as pd
import matplotlib.pyplot as plt
import argparse
import seaborn as sns
parser = argparse.ArgumentParser(description="Optional column choice from file")
parser.add_argument("-f", type= int, help= "column number", default= 2, dest= "column", choices= [1,3], required=True)
parser.add_argument(-file, help= "file.tsv")
args= parser.parse_args()
file = open("Histogram_example.tsv")
pd.read_table("Histogram_example.tsv")
sns.histogram(data= "Histogram_example.tsv", x="age")
