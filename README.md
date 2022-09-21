# Trgn_assignment3

## Extract_phonenum.py

### Usage 

```python3 extract_phonenum.py mytextfile.txt```

### Description

Extract phone numbers from a text file and prints formatted phone numbers.
One-line per phone number formatted as [+][country code] ([AreaCode]) [local phone number]. [+][country code] optional output if number is international. This script will extract phone numbers from text files. 

### Known Issues

This script will work if the phone number is in the following formats: +(country code)- 3 digits - 3 digits- 4 digits. 

## Ensg2hugo.py

### Usage

```python3 ensg2hugo.py [-f][0-9] [file]```

### Description

Create a dictionary, whereby you lookup the Ensembl name and replace it with the HUGO name.

Since the ```Homo_sapiens.GRCh37.75.gtf``` file is too large, you will need to use ```curl``` to save the file.

```curl http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz --output Homo_sapiens.GRCh37.75.gtf.gz```
``` gunzip Homo_sapiens.GRCh37.75.gtf.gz```

The unit test will be: https://github.com/davcraig75/unit/blob/master/expres.anal.csv


### Known Issues

Error found: ```<>:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
<>:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
/var/folders/fk/5gx_9wk104l42yf08jm0x5f40000gp/T/ipykernel_11446/1232127364.py:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
  for text in "Homo_sapiens.GRCh37.75.gtf"("expression_analysis.tsv"):
/var/folders/fk/5gx_9wk104l42yf08jm0x5f40000gp/T/ipykernel_11446/1232127364.py:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
  for text in "Homo_sapiens.GRCh37.75.gtf"("expression_analysis.tsv"):
/var/folders/fk/5gx_9wk104l42yf08jm0x5f40000gp/T/ipykernel_11446/1232127364.py:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
  for text in "Homo_sapiens.GRCh37.75.gtf"("expression_analysis.tsv"):
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In [21], line 1
----> 1 for text in "Homo_sapiens.GRCh37.75.gtf"("expression_analysis.tsv"):
      2     ensembl= re.findall(pattern,text)
      3     if ensemble in find:

TypeError: 'str' object is not callable```

## Histogram.py

### Usage 

``` python3 histogram.py [-f][0-9] [file] ```

### Description

Creates a histogram as a png from a file using the specified column in a tab delimited file. 

### Known Issues 

```bad operand type for unary -: '_io.TextIOWrapper'``` after argparse

```sb.histogram(data= Histogram_example.tsv, x=age) AttributeError: module 'seaborn' has no attribute 'histogram'``` at the end

need to alter argparse to allow for optional -f and ensure output is histogram not bar graph