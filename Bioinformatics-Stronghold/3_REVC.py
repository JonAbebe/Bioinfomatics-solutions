"""
Title: Complementing a Strand of DNA
ID: REVC

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

from helper_scripts.read_text import read_text
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file

from Bio.Seq import Seq

def main(sequence:str)->str:
    """Takes in a sequence and returns the reverse complement
    """
    my_seq = Seq(sequence)
    return str(my_seq.reverse_complement())

if __name__ == '__main__':
    input_file, output_file = parser()
    reverse_complement = main(read_text(input_file))
    write_to_file(output_file,reverse_complement)