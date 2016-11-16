import fileinput
import sys
import itertools
import random
from random import choice
from numpy import dot, array,random

if __name__ == '__main__':
    input = []
    train_set = []
    eta = 0.1
    n = 10
    w = random.rand(2)
    lamb = lambda x: 0 if x < 0 else 1
    
    def train():
        global w
        for i in xrange(n):
            #get the first 2 values
            x, val = choice(train_set)
            result = dot(w,x)
            #get the val
            error = int(val) - lamb(result)
            w += eta * error * x
            
    def query(x):
        global w
        result = dot(x, w)
        return lamb(result)
    
    # Read each input line
    for line in sys.stdin:
        if line[0] != "#":
            line = line.strip("\n")
            if line != "":
                input.append(line)
        
    usr_query=[]
    for line in input:
        if line.startswith("Q"):
            arr_query = line.split("=")
            values = arr_query[1].split(",")
            usr_query.append(int(values[0]))
            usr_query.append(int(values[1]))
        else:
            arr_line = line.split(',')
            line_set = (array([int(arr_line[0]), int(arr_line[1])]), int(arr_line[2]))
            train_set.append(line_set)
    train()
    print(query(array(usr_query)))