"""
Title: Rabbits and Recurrence Relations
ID: FIB

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_text import read_text
import itertools

def Fibonacci(n,k):
    if n==0:
        return 0
    # Second Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1,k)+k*Fibonacci(n-2,k)
        
if __name__ == '__main__':
    input_file, output_file = parser()
    file = open(input_file,'r')
    contents = file.read().strip().split(' ')
    n = int(contents[0])
    k = int(contents[1])
    output_val = Fibonacci(n,k)
    write_to_file(output_file,str(output_val))
