"""
Title: k-Mer Composition
ID: KMER

Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s."""

from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta
import itertools
from collections import Counter

def get_all_4mers(sequence:'sequence') -> 'dict':
    """Takes in a sequence returns all 4mers and their counts occurring in sequence
    """
    all_4mers = [sequence[i:i+4] for i in range(0,len(sequence)-3)]
    return Counter(all_4mers)
    
if __name__ == '__main__':
    input_file, output_file = parser()
    file = str(list(read_fasta(input_file).values())[0])
    kmers_lexi = sorted(list(map(lambda y: ''.join(y),itertools.product('ATGC',repeat=4))))
    count_in_sequence = get_all_4mers(file)
    return_val = [str(count_in_sequence[seq]) for seq in kmers_lexi]
    to_string = ' '.join(return_val)
    write_to_file(output_file,str(to_string))