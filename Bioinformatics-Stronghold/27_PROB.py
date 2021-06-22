"""
Title: Consensus and Profile
ID: CONS

Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta
from collections import defaultdict
import math

def main(sequence,gc_content):
    """Takes in a sequence and the gc content returns the probability of a random string
    """
    AT_count = sequence.count('A') + sequence.count('T')
    GC_count = sequence.count('G') + sequence.count('C')
    gc_prob = ''
    for gc_value in gc_content:
        log_prob = GC_count*math.log10(0.5*gc_value) + AT_count*math.log10(0.5*(1-gc_value))
        gc_prob += str(log_prob) + ' '
    return gc_prob    
if __name__ == '__main__':
    input_file, output_file = parser()
    file = open(input_file,'r')
    contents = file.read().split('\n')
    sequence = contents[0]
    gc_content = list(map(float,contents[1].split(' ')))
    output_string = main(sequence,gc_content)
    write_to_file(output_file,output_string)