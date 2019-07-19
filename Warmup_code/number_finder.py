import numpy as np

def prime_finder(array):
    prime=[]
    for i in array:
        division_array=np.array(range(2,i))
        remainder=np.divmod(i, division_array)[1]
        if 0 in remainder:
            continue
        else:
            prime.append(i)
    return np.array(prime)

def fibo_gen(num):
    fibo_array=np.array([0,1])
    while fibo_array[-1]<num:
        fibo_array= np.insert(fibo_array, len(fibo_array), fibo_array[-1]+fibo_array[-2])
    return fibo_array
    
def fibonacci_finder(array):
    max_in_array=np.max(array)
    fibo_array= fibo_gen(max_in_array)
    return np.intersect1d(array, fibo_array)

def tribo_gen(max_num, min_num):
    tribo_array=np.array([1,0, 1])
    while tribo_array[-1]<max_num:
        tribo_array=np.insert(tribo_array, len(tribo_array),tribo_array[-1]+tribo_array[-2])
    while tribo_array[0]>min_num:
        tribo_array= np.insert(tribo_array,0, tribo_array[1]-tribo_array[0])
    return tribo_array

def tribonacci_finder(array):
    max_in_array=np.max(array)
    min_in_array=np.min(array)
    tribo_array=tribo_gen(max_in_array, min_in_array)
    return np.intersect1d(array, tribo_array)
