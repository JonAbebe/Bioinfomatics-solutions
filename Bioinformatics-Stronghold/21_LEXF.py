"""
Title: Enumerating k-mers Lexicographically
ID: LEXF

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_text import read_text
import itertools


if __name__ == '__main__':
    input_file, output_file = parser()
    file = open(input_file,'r')
    contents = file.read().strip().split('\n')
    val = int(contents[-1])
    alpha = contents[0].replace(' ','')
    final_string = ''
    for p in itertools.product(alpha,repeat=val):
        final_string += f"{''.join(p)}"
        final_string += '\n'
    write_to_file(output_file,final_string)
