{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "1b931e29-fce8-43bf-8f3a-0c5f101b3df5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import argparse\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "9f4d69b8-7c20-4903-b6cf-7b616c0f86e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "_StoreAction(option_strings=['-f'], dest='column', nargs=None, const=None, default=2, type=<class 'int'>, choices=[1, 3], help='column number', metavar=None)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "parser = argparse.ArgumentParser(description=\"Optional column choice from file\")\n",
    "parser.add_argument(\"-f\", type= int, help= \"column number\", default= 2, dest= \"column\", choices= [1,3], required=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "c8b44093-dcbd-48f0-b8a4-e9a656a3213f",
   "metadata": {},
   "outputs": [],
   "source": [
    "file = open(\"Histogram_example.tsv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "2e8cbfa1-e146-4c89-99df-d82b132f8fbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>height</th>\n",
       "      <th>sex</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>12</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>13</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>14</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>15</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>16</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>16</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>18</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>18</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>18</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  height  sex\n",
       "0   12       4    0\n",
       "1   13       4    1\n",
       "2   14       4    0\n",
       "3   15       5    1\n",
       "4   16       5    0\n",
       "5   16       6    1\n",
       "6   18       6    0\n",
       "7   18       6    1\n",
       "8   18       6    0"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_table(\"Histogram_example.tsv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "77824c2b-dd5a-42cb-920f-d16eaf7e2f4b",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'seaborn' has no attribute 'histogram'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [46], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[43msns\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mhistogram\u001b[49m(data\u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHistogram_example.tsv\u001b[39m\u001b[38;5;124m\"\u001b[39m, x\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mage\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[0;31mAttributeError\u001b[0m: module 'seaborn' has no attribute 'histogram'"
     ]
    }
   ],
   "source": [
    "sns.histogram(data= \"Histogram_example.tsv\", x=\"age\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c0354e3-b64d-45c9-ba88-1bfe1045fd11",
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
