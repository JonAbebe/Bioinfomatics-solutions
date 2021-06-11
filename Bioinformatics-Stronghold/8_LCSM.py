"""
Title: Finding a Shared Motif
ID: LCSM

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta
from Bio.Seq import Seq

def get_splits(seq:str,split_val:int)-> list:
    """Takes in a sequence, returns overlapping split according to split_val:
    i.e. 'ABCD',2 -> [AB,BC,CD]
    """
    adjust_end = len(seq)-(split_val-1) #Account for all values < split_val
    return [seq[i:(i+split_val)] for i in range(0,adjust_end)]
    
def return_longest_overlap(min_length:int,all_seqs:list) -> str:
    """Takes in all input sequences and the minimum length, returns longest substring occurring across all
    """
    s = ''
    for i in range(2,min_length+1):
        current_splits = [get_splits(j,i) for j in all_seqs] #Splits each sequence using a specific value
        overlaps = list(set.intersection(*map(set,current_splits))) #Finds intersection of overlaps, grabs first index
        if len(overlaps) > 0 :
            s = overlaps[0]
    return s

if __name__ == '__main__':
    input_file, output_file = parser()
#     file = open(input_file,'r')
    file = read_fasta(input_file)
    sequences = list(map(str,file.values()))
    minimum_length = min(list(map(lambda x: len(x),sequences)))
    return_string = return_longest_overlap(minimum_length,sequences)
    write_to_file(output_file,return_string)
