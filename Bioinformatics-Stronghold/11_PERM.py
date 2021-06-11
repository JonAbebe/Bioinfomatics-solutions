"""
Title: Enumerating Gene Orders
ID: PERM

Given: A positive integer n <= 7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order)."""

import itertools
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_text import read_text



if __name__ == '__main__':
    input_file, output_file = parser()
    file = open(input_file,'r')
    seq = read_text(file)
#     n = 3
#     x = list(range(1,n+1))
# 
#     s = str(len(list(itertools.permutations(x)))) +'\n'
#     for i in list(itertools.permutations(x)):
#         s += ' '.join(list(map(str,list(i))))  + '\n'
#     print(s)