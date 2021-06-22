"""
Title: Partial Permutations
ID: PPER

Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_text import read_text
import math


if __name__ == '__main__':
    input_file, output_file = parser()
    file = open(input_file,'r')
    n,k = map(int,file.read().strip().split())
    return_val = int((math.factorial(n)/math.factorial(n-k))%1000000)
    write_to_file(output_file,str(return_val))