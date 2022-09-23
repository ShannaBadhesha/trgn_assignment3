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

Script will create a blank new file instead of a file with the replaced Ensembl name. No errors written out. Is potentially matching the Ensemble name and HUGO name, but printing them out on to a new file. 

## Histogram.py

### Usage 

``` python3 histogram.py [-f][0-9] [file] ```

### Description

Creates a histogram as a png from a file using the specified column in a tab delimited file. 

### Known Issues 

Histogram prints out blank when running script. Error occurs from the arg_column when using the optional command. Reads incorrect column causing it to print out blank with skewed x and y axes.