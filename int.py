from random import choice
from numpy import array, dot, random

unit_step = lambda x: 0 if x < 0 else 1
#OR function
training_data = [
    (array([0,0,1]), 0),
    (array([0,1,1]), 1),
    (array([1,0,1]), 1),
    (array([1,1,1]), 1),
]

w = random.rand(3)
errors = []
eta = 0.2
n = 100

for i in xrange(n):
    x, expected = choice(training_data)
    print x
    result = dot(w, x)
    error = expected - unit_step(result)
    errors.append(error)
    w += eta * error * x

for x, _ in training_data:
    #print w
    #print ("_ es: ",_)
    result = dot(x, w)
    #print result
    #print("{} -> {}".format(x[:2], unit_step(result)))

#print(training_data)