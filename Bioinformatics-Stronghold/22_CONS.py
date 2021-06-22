"""
Title: Consensus and Profile
ID: CONS

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta
from collections import defaultdict

def counting_indices(lst_of_seqs:list) -> 'dict':
    """Takes in a list of sequences, goes through the matrix and returns a dictionary of 
    with the keys as column position, and values of nucleotides at that column position
    """
    counting = defaultdict(list)
    for i in range(len(file)):
        for j in range(len(file[i])):
            counting[j].append(file[i][j])
    return counting
    
if __name__ == '__main__':
    input_file, output_file = parser()
    file = list(map(lambda x: list(x),read_fasta(input_file).values()))
    counted_dict = counting_indices(file)
    consensus = ''.join([max(set(idx), key=idx.count) for idx in counted_dict.values()]) +'\n'
    A = 'A: '
    C = 'C: '
    G = 'G: '
    T = 'T: '
    for k,v in counted_dict.items():
        A += str(v.count('A')) + ' '
        C += str(v.count('C')) + ' '
        G += str(v.count('G')) + ' '
        T += str(v.count('T')) + ' '
    final_counts = consensus+'\n'.join([A,C,G,T])
    write_to_file(output_file,final_counts)