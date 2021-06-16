"""
Title: Enumerating Oriented Gene Orderings
ID: SIGN

Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_text import read_text
import itertools

def return_signed_permutations(lst,val):
    """Takes in a list and a positive interger, returns signed permutation
    """
    s = ''
    count = 0
    for i in list(itertools.permutations(full_lst,val)):
        test_dup = set(map(abs,i))
        if len(test_dup) == val:
            count +=1
            convert = list(map(str,i))
            s += ' '.join(convert) + '\n'
    final_s = str(count)+'\n' + s
    return final_s
    
if __name__ == '__main__':
    input_file, output_file = parser()
    val = int(read_text(input_file))
    lst = list(range(1,val+1))
    negative_lst = list(map(lambda x:x*-1,lst))
    full_lst = lst+negative_lst
    Sign_return = return_signed_permutations(full_lst,val)
    write_to_file(output_file,Sign_return)