{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a050c05-eebb-42f4-a74a-d9790657a7da",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re \n",
    "import fileinput\n",
    "import pandas as pd\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e76a9991-0f35-4e7c-b991-2dd69f8b058d",
   "metadata": {},
   "outputs": [],
   "source": [
    "pattern= re.findall('.*gene_id \"(.*?)\"[\\s].*gene_name \"(.*?)\"[\\s];',text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3a95737e-aa1c-4ba8-bd12-f015f3a04826",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open (\"Homo_sapiens.GRCh37.75.gtf\", 'r') as file:\n",
    "    for text in file:\n",
    "        find= re.findall('.*gene_id \"(.*?)\"[\\s].*gene_name \"(.*?)\"[\\s];',text)\n",
    "    if find:\n",
    "        print(find)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "0aca8aac-acba-4c0e-8b48-28ba01e99ae4",
   "metadata": {},
   "outputs": [],
   "source": [
    "Enname= re.findall('(E.*)',text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "3659f38a-a1b4-4827-b1b4-31a9b790e87a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<>:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?\n",
      "<>:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?\n",
      "/var/folders/fk/5gx_9wk104l42yf08jm0x5f40000gp/T/ipykernel_11446/1232127364.py:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?\n",
      "  for text in \"Homo_sapiens.GRCh37.75.gtf\"(\"expression_analysis.tsv\"):\n",
      "/var/folders/fk/5gx_9wk104l42yf08jm0x5f40000gp/T/ipykernel_11446/1232127364.py:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?\n",
      "  for text in \"Homo_sapiens.GRCh37.75.gtf\"(\"expression_analysis.tsv\"):\n",
      "/var/folders/fk/5gx_9wk104l42yf08jm0x5f40000gp/T/ipykernel_11446/1232127364.py:1: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?\n",
      "  for text in \"Homo_sapiens.GRCh37.75.gtf\"(\"expression_analysis.tsv\"):\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'str' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [21], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m text \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mHomo_sapiens.GRCh37.75.gtf\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mexpression_analysis.tsv\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m:\n\u001b[1;32m      2\u001b[0m     ensembl\u001b[38;5;241m=\u001b[39m re\u001b[38;5;241m.\u001b[39mfindall(pattern,text)\n\u001b[1;32m      3\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m ensemble \u001b[38;5;129;01min\u001b[39;00m find:\n",
      "\u001b[0;31mTypeError\u001b[0m: 'str' object is not callable"
     ]
    }
   ],
   "source": [
    "for text in \"Homo_sapiens.GRCh37.75.gtf\"(\"expression_analysis.tsv\"):\n",
    "    ensembl= re.findall(pattern,text)\n",
    "    if ensemble in find:\n",
    "        print(line)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "183e0166-b7f0-4efe-ba6a-4d2803708cd5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
