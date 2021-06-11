"""
Title: RNA Splicing
ID: SPLC

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
"""

from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta
from Bio.Seq import Seq
from Bio import SeqIO





if __name__ == '__main__':
    input_file, output_file = parser()
    s = read_fasta(input_file).values()
    
    lst_of_seqs = list(map(str,s))
    full_string = lst_of_seqs.pop(0)
    for i in lst_of_seqs:
        full_string = full_string.replace(i,'')
    return_string = Seq(full_string).translate(to_stop=True)
    
    write_to_file(output_file,str(return_string))
