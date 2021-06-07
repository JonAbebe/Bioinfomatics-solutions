
"""
Title: Counting DNA Nucleotides
ID: DNA

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

from collections import Counter
from helper_scripts.argument_parsing import parser


def read_text(file_location:str)-> str:
    """Takes in a file location, opens/parses the file and returns the string contained
    ***Note This is different from handling fasta files which contain headers*** 
    """
    file = open(file_location,'r')
    sequence = file.read().replace('\n','')
    return sequence

def main(seq:str)->str:
    """Takes in sequence of nucleotides, returns count of each nucleotide in 'A','C','G','T' order along with their counts.
    """
    output_order = ['A','C','G','T']
    counted_seq = Counter(seq)
    output_string = ''
    for nucleotide in output_order:
        output_string += str(counted_seq[nucleotide]) + ' '
    return output_string
if __name__ == '__main__':
    input_file, output_file = parser()
    return_val = main(read_text(input_file))
    out = open(output_file,'w')
    out.write(return_val)
    out.close()