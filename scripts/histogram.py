{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1b931e29-fce8-43bf-8f3a-0c5f101b3df5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9f4d69b8-7c20-4903-b6cf-7b616c0f86e2",
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
       "      <th>Column</th>\n",
       "      <th>header</th>\n",
       "      <th>value</th>\n",
       "      <th>value2</th>\n",
       "      <th>value3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>213</td>\n",
       "      <td>26</td>\n",
       "      <td>435</td>\n",
       "      <td>1234</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>643</td>\n",
       "      <td>87</td>\n",
       "      <td>436</td>\n",
       "      <td>2345</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>686</td>\n",
       "      <td>97</td>\n",
       "      <td>346</td>\n",
       "      <td>3456</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>976</td>\n",
       "      <td>34</td>\n",
       "      <td>745</td>\n",
       "      <td>4567</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>353</td>\n",
       "      <td>65</td>\n",
       "      <td>325</td>\n",
       "      <td>5678</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Column   header  value  value2  value3\n",
       "0        1     213     26     435    1234\n",
       "1        2     643     87     436    2345\n",
       "2        3     686     97     346    3456\n",
       "3        4     976     34     745    4567\n",
       "4        5     353     65     325    5678"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_table(\"histogram_example.tsv\")\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2e8cbfa1-e146-4c89-99df-d82b132f8fbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[<AxesSubplot: title={'center': 'value2'}>]], dtype=object)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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oqKizGeffWaMsb/e1157zdx3333mpZdeMpLMyy+/7HO8Meo7efKkiYmJMdOmTTP79+83zz//vImIiDC/+93v/Jor4aWV6dy5s1mzZo2pqKgwYWFhZsuWLd5j77//vpFkCgsLjTHfbLSQkBBTVlbm7fPkk0+aqKgo43K5mn3uDXXq1CnTr18/k5uba66//npveAnWmhctWmSSkpLqPRaMNd99993mmmuuOetxj8djYmNjzSOPPOJtq6ioME6n0zz//PPGGGP+8Y9/GEnm73//u7fP66+/bhwOhzly5EjTTb6R3Hnnnebiiy82Ho8nKNfYGGPGjRtnbr31Vp+2H/zgB2batGnGmOBb55qaGhMaGmr+/Oc/+7Rffvnl5r777gu6ev89vDRWfU888YTp3Lmzz76+++67Tf/+/f2aHy8btRJnzpzRpk2bVF1drZSUFO3du1dut1upqanePgMGDFDPnj1VWFgoSSosLNSQIUO8f91YktLS0lRZWan33nuv2WtoqNmzZ2vcuHE+tUkK6poPHjyo+Ph49enTR9OmTdPhw4clBWfNf/zjHzVixAjddNNN6t69uy677DI9/fTT3uMlJSUqKyvzqbljx45KTk72qblTp04aMWKEt09qaqpCQkJUVFTUfMUE4PTp0/rDH/6gW2+9VQ6HIyjXWPrmr6fn5eXpn//8pyTp7bff1s6dOzV27FhJwbfOX3/9tc6cOVPnL79HRERo586dQVfvv2us+goLC3Xdddepffv23j5paWk6cOCAvvzyywbPx++PB0Djevfdd5WSkqKvvvpKHTp00Msvv6yBAwequLhY7du3r/Np2TExMSorK5MklZWV+fywqz1ee6w12rRpk9566y2f14lrlZWVBWXNycnJWr9+vfr376/S0lJlZ2fr2muv1f79+4Oy5o8++khPPvmkMjIydO+99+rvf/+7fvGLX6h9+/aaMWOGd8711fTtmrt37+5zvF27durSpUurrPnbtm7dqoqKCs2cOVNS8O7re+65R5WVlRowYIBCQ0N15swZPfTQQ5o2bZokBd06X3jhhUpJSdHixYt16aWXKiYmRs8//7wKCwvVt2/foKv33zVWfWVlZUpMTKwzRu2xzp07N2g+hJcW1r9/fxUXF+vkyZN68cUXNWPGDBUUFLT0tJrEp59+qjvvvFO5ublt6nOrav9PVJKGDh2q5ORk9erVSy+88IIiIiJacGZNw+PxaMSIEXr44YclSZdddpn279+v1atXa8aMGS08u6a3du1ajR07VvHx8S09lSb1wgsv6LnnntPGjRs1aNAgFRcXa+7cuYqPjw/adf7973+vW2+9VT169FBoaKguv/xyTZ06VXv37m3pqbU5vGzUwtq3b6++fftq+PDhWrJkiZKSkrRy5UrFxsbq9OnTqqio8OlfXl6u2NhYSVJsbGyddyzU3q/t05rs3btXx44d0+WXX6527dqpXbt2Kigo0OOPP6527dopJiYm6GquT6dOnXTJJZfo0KFDQbnOcXFxGjhwoE/bpZde6n2prHbO9dX07ZqPHTvmc/zrr7/WF1980SprrvXJJ5/oL3/5i26//XZvWzCusSTNmzdP99xzj6ZMmaIhQ4bolltu0S9/+UstWbJEUnCu88UXX6yCggJVVVXp008/1e7du+V2u9WnT5+grPfbGqu+xtrrhJdWxuPxyOVyafjw4QoLC1NeXp732IEDB3T48GGlpKRIklJSUvTuu+/6bJbc3FxFRUXV+eXRGtx444169913VVxc7L2NGDFC06ZN8/53sNVcn6qqKn344YeKi4sLynW++uqrdeDAAZ+2f/7zn+rVq5ckKTExUbGxsT41V1ZWqqioyKfmiooKn/+jfeONN+TxeJScnNwMVQTmmWeeUffu3TVu3DhvWzCusSTV1NQoJMT3V0hoaKg8Ho+k4F7nCy64QHFxcfryyy+1bds2TZgwIajrlRpvPVNSUrRjxw653W5vn9zcXPXv37/BLxlJ4q3SLemee+4xBQUFpqSkxLzzzjvmnnvuMQ6Hw2zfvt0Y883bK3v27GneeOMNs2fPHpOSkmJSUlK859e+vXL06NGmuLjY5OTkmG7durXqt1f+u2+/28iY4Kz5rrvuMvn5+aakpMT87W9/M6mpqSY6OtocO3bMGBN8Ne/evdu0a9fOPPTQQ+bgwYPmueeeM5GRkeYPf/iDt8/SpUtNp06dzCuvvGLeeecdM2HChHrfcnnZZZeZoqIis3PnTtOvX79W85bS+pw5c8b07NnT3H333XWOBdsaG2PMjBkzTI8ePbxvlX7ppZdMdHS0mT9/vrdPsK1zTk6Oef31181HH31ktm/fbpKSkkxycrI5ffq0Mcb+ek+dOmX27dtn9u3bZySZ5cuXm3379plPPvnEGNM49VVUVJiYmBhzyy23mP3795tNmzaZyMhI3iptk1tvvdX06tXLtG/f3nTr1s3ceOON3uBijDH/+te/zB133GE6d+5sIiMjzfe//31TWlrqM8bHH39sxo4dayIiIkx0dLS56667jNvtbu5SAvbv4SUYa548ebKJi4sz7du3Nz169DCTJ0/2+ZsnwVjzn/70JzN48GDjdDrNgAEDzFNPPeVz3OPxmAULFpiYmBjjdDrNjTfeaA4cOODT58SJE2bq1KmmQ4cOJioqyqSnp5tTp041Zxl+2bZtm5FUpw5jgnONKysrzZ133ml69uxpwsPDTZ8+fcx9993n8xbYYFvnzZs3mz59+pj27dub2NhYM3v2bFNRUeE9bnu9f/3rX42kOrcZM2YYYxqvvrfffttcc801xul0mh49epilS5f6PVeHMd/6c4gAAACtHNe8AAAAqxBeAACAVQgvAADAKoQXAABgFcILAACwCuEFAABYhfACAACsQngBAABWIbwAAACrEF4AAIBVCC8AAMAq/x9dZvrEE+WlRQAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.hist(column=\"value2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "852c754a-d21e-444f-92a6-3153e7cad468",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'histogram_example' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [7], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m plt\u001b[38;5;241m.\u001b[39msavefig(\u001b[43mhistogram_example\u001b[49m\u001b[38;5;241m.\u001b[39mpng)\n",
      "\u001b[0;31mNameError\u001b[0m: name 'histogram_example' is not defined"
     ]
    }
   ],
   "source": [
    "plt.savefig(histogram_example.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8ac0be2-6e4f-463d-be26-13c13994a0ab",
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
