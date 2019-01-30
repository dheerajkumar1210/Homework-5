# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:25:24 2019

@author: dheeraj_kumar
"""

def isPrime(i):
    '''
    Check for a number if it's prime
    '''
    if i == 1:
        return True    
    for x in range(2,int(i/2)+1):
        if i%x == 0:
            return True
    return False

def FizzBizz():
    '''
     This method will print "Fizz" for multiples of three p instead of the number and for the multiples of five print "Buzz".

     For numbers which are multiples of both three and five print "FizzBuzz".
    '''
    for i in range(1,101):
        if not isPrime(i):
            print("{} is prime number".format(i))
        else:
            if i%3 == 0 and i%5 == 0:
                print("FizzBuzz")            
            elif i%3 == 0 or i%5 == 0:            
                if i%3 == 0:
                    print("Fizz")
                else:
                    print("Buzz")
            else:
                print(i)
            

def main():
    FizzBizz()    

if __name__ == "__main__":
    main()