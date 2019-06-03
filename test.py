# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('hello world')

def hello():
    print('hello world')
    


    
hello()

def echo(inte):
    def echoinner(word):
        innerword = word * inte
        return innerword
    return echoinner

twice = echo(2)

twice('we')

import os
os.getcwd()
os.chdir("/Users/jeangq/Documents/Python programming")

a, b, m = (int(input()), int(input()), int(input()))
print(pow(a,b), pow(a, b, m), sep = '\n')


print('please input the rows you want to output')

for i in range(1, int(input())+1):
    print(int(10** i // 9 * i))
    



import tensorflow as tf

hello = tf.constant('hello tensorflow')

sess = tf.Session()

print(sess.run(hello))




