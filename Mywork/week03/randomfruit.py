# randomfruit.py
# This program prints out a random fruit
# Author: Tatjana Staunton

import random
fruits = ['Apple', 'Orange', 'Banana', 'Pear'] 
index = random.randint (0, len (fruits)-1) # we need a random number between 0 and length -1
fruit = fruits [index]
print ('A Random Fruit: {}' .format (fruit))