{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "c924e9bd-d112-49cd-92d6-9602994a6895",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<_io.TextIOWrapper name='mytextfile.txt' mode='r' encoding='UTF-8'>"
      ]
     },
     "execution_count": 23,
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
   "execution_count": 24,
   "id": "d677b8b0-302c-4033-acd0-227775e82bbc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'This is a sample file that I will be using to extract the random phone numbers 1-559-435-2422 and +45-924-242-5242. '"
      ]
     },
     "execution_count": 24,
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
   "execution_count": 25,
   "id": "aa83f9b4-478c-4a5f-b086-655d4b17119a",
   "metadata": {},
   "outputs": [],
   "source": [
    "pattern = r\"\\+?[0-9]\\d{0,2}[-]\\d{3}[-]\\d{3}[-]\\d{4}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "3fde4859-c848-4e4f-baa9-48e7953d49f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['1-559-435-2422', '+45-924-242-5242']"
      ]
     },
     "execution_count": 26,
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
   "execution_count": 27,
   "id": "ef452195-f12f-452c-9a90-45d3fdcd815d",
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
   "id": "cfa6c3b8-7676-44d2-93a0-fad3b90d667a",
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
