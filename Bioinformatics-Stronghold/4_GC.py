"""
Title: Computing GC Content
ID: GC

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. \
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""

from helper_scripts.read_fasta import read_fasta
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file

from Bio.Seq import Seq

def count_GC(sequence:str)->int:
    """Takes in a sequence, returns the GC percentage
    """
    G_count = sequence.count('G')
    C_count = sequence.count('C')
    return ((G_count+C_count)/len(sequence))*100
    
def main(fasta_dict:'dict')->str:
    """Takes in a sequence and returns the reverse complement
    """
    calculated_dict = {}
    for IDs,sequences in fasta_dict.items():
        calculated_dict[IDs] = count_GC(sequences)
    max_ID = max(calculated_dict, key=calculated_dict.get)
    max_val = calculated_dict[max_ID]
    return f"{max_ID}\n{max_val}"
    
if __name__ == '__main__':
    input_file, output_file = parser()
    GC_dictionary = main(read_fasta(input_file))
    write_to_file(output_file,GC_dictionary)