{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b6af6782-5a2d-4b75-bea2-423a205ea5d6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<_io.TextIOWrapper name='mytextfile.txt' mode='r' encoding='UTF-8'>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import re\n",
    "file = open(\"mytextfile.txt\" ,'r')\n",
    "file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6113bfd4-d194-4559-981e-da24c0d4fdec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'This is a sample file that I will be using to extract the random phone numbers 1-559-435-2422 and +45-924-242-5242. '"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "text = file.read()\n",
    "text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0fa51634-f8d7-4aa5-b640-6a33e605c5da",
   "metadata": {},
   "outputs": [],
   "source": [
    "pattern = r\"\\+?[0-9]\\d{0,2}[-]\\d{3}[-]\\d{3}[-]\\d{4}\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "873052c2-f450-4b12-9dfc-1e54926a6bf4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['1-559-435-2422', '+45-924-242-5242']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "phonum = re.findall(pattern,text)\n",
    "phonum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "afdf185e-0fb0-4e90-b5c5-fd2b22a04ef4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1-559-435-2422\n",
      "+45-924-242-5242\n"
     ]
    }
   ],
   "source": [
    "for match in re.findall(pattern,text):\n",
    "    print(match)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17c1b8b9-06d3-4097-abb9-20c73969aac9",
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
