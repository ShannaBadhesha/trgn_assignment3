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


### Description


### Known Issues

## Histogram.py

### Usage 

``` python3 histogram.py [-f][0-9] [file] ```

### Description

Creates a histogram as a png from a file using the specified column in a tab delimited file. 

### Known Issues 

```bad operand type for unary -: '_io.TextIOWrapper'``` after argparse

```sb.histogram(data= Histogram_example.tsv, x=age) AttributeError: module 'seaborn' has no attribute 'histogram'``` at the end

need to alter argparse to allow for optional -f and ensure output is histogram not bar graph