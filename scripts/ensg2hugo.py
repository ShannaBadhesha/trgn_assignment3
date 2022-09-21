import re 
import fileinput
import pandas as pd
import csv
pattern= re.findall('.*gene_id "(.*?)"[\s].*gene_name "(.*?)"[\s];',text)
with open ("Homo_sapiens.GRCh37.75.gtf", 'r') as file:
    for text in file:
        find= re.findall('.*gene_id "(.*?)"[\s].*gene_name "(.*?)"[\s];',text)
    if find:
        print(find)
Enname= re.findall('(E.*)',text)
for text in "Homo_sapiens.GRCh37.75.gtf"("expression_analysis.tsv"):
    ensembl= re.findall(pattern,text)
    if ensemble in find:
        print(line)
