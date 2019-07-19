"""An example library for converting temperatures."""
from pynverse import inversefunc

def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c

def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    return temperature_c *(9/5)+32

def convert_c_to_k(temperature_c):
    '''Convert Celsius to Kelvin'''
    return temperature_c+273.15

def convert_k_to_c(temperature_k):
    return temperature_k-273.15

def convert_k_to_f(temperature_k):
    return convert_k_to_c(convert_c_to_f(temperature_k))

def convert_f_to_k(temperature_f):
    return convert_f_to_c(convert_c_to_k(temperature_f))

def displaying(temp):
    while True:
        temp_type=input("Did you type in C, F or K")
        temp_type=temp_type.lower()
        if temp_type=="f":
            kfc=[convert_f_to_k(temp), temp, convert_f_to_c(temp)]
            break
        elif temp_type=="c":
            kfc=[convert_c_to_k(temp), convert_c_to_f(temp), temp]
            break
        elif temp_type=="k":
            kfc=[temp, convert_k_to_f(temp), convert_k_to_c(temp)]
            break
        else:
            print("retype!!!")
            continue
    print("- The temperature in K is : {} \n \
        - The temperature in F is : {} \n \
        - The temperature in C is : {} \ ".format(kfc[0],kfc[1],kfc[2]))