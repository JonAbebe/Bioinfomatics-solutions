"""
Title: Perfect Matchings and RNA Secondary Structures
ID: PMCH

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta
from math import factorial




if __name__ == '__main__':
    input_file, output_file = parser()
    file = str(list(read_fasta(input_file).values())[0])
    perfect_matches = factorial(file.count('G')) * factorial(file.count('A'))
    write_to_file(output_file,str(perfect_matches))
    