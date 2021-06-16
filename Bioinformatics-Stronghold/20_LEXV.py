"""
Title: Ordering Strings of Varying Length Lexicographically
ID: LEXV

Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜 and a positive integer n (n≤4).

Return: All strings of length at most n formed from 𝒜, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_text import read_text
import itertools

def get_permutations(alphabet:'str',some_int:'int') -> list:
    """Takes a sting of characters, returns all combinations up to length some_int
    """
    all_kmers = []
    for n in range(1,some_int+1):
        for strings in itertools.product(alphabet,repeat=n):
            kmers = ''.join(strings)
            all_kmers.append(kmers)
    return all_kmers

if __name__ == '__main__':
    input_file, output_file = parser()
    file = open(input_file,'r')
    contents = file.read().strip().split('\n')
    val = int(contents[-1])
    alpha = contents[0].replace(' ','')
    unsorted_kmers = get_permutations(alpha,val)
    sorted_lst = sorted(unsorted_kmers,key = lambda x:[alpha.index(idx) for idx in x])
    final_output = '\n'.join(sorted_lst)
    write_to_file(output_file,final_output)