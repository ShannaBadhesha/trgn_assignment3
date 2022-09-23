import re 
import fileinput
import sys
if len(sys.argv) <3:
    print("missing file name")
    exit()
filename= sys.argv[0]
arg_column= sys.argv[1]
column = 2
if arg_column.startswith ('-f'):
    column = arg_column [2:]
elif not arg_column.startswith ('-f'):
    column = 2
dict={}
with open("Homo_sapiens.GRCh37.75.gtf") as file:
    for text in file:
        find_gene_id= re.findall('gene_id "(ENSG.*?)"[;]', text)
        find_gene_name= re.findall('gene_name "(.*?)"[;]', text)
        if find_gene_id:
            if find_gene_name:
                dict[find_gene_id[0]] = [find_gene_name[0]]
replace_file= sys.argv[2]
with open(sys.argv[2]) as f:
    contents= f.readlines()
    for text in f:
        replace_engene= re.findall('"(ENSG.*?)"', text)
        if replace_engene in dict:
            replace_engene= re.match(replace_engene,dict)
