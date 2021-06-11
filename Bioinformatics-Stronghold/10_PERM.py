"""
Title: Enumerating Gene Orders
ID: PERM

Given: A positive integer n <= 7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order)."""

import itertools
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_text import read_text

def return_permutations(val:int) -> str:
    """Returns the length of permutations, and the list of all permutations
    """
    lst_of_vals = list(range(1,val+1))
    s = str(len(list(itertools.permutations(lst_of_vals)))) +'\n' #Init string with length of list
    for i in list(itertools.permutations(lst_of_vals)):
        s += ' '.join(list(map(str,list(i))))  + '\n'
    return s 
    
if __name__ == '__main__':
    input_file, output_file = parser()
    seq = read_text(input_file)
    return_perm =return_permutations(int(seq))
    write_to_file(output_file,return_perm)
