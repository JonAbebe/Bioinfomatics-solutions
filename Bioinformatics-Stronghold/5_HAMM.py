"""
Title: Counting Point Mutations
ID: HAMM

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file



def read_in_file(file_location:str)->int:
    """Takes in a sequence, returns the GC percentage
    """
    file = open(file_location,'r')
    sequences = file.read().strip('\n').split('\n')
    return sequences[0],sequences[1]
    
def main(seq1:str,seq2:str)->str:
    """Takes in two sequences and compares the number of mismatches
    """
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return str(count)
    
if __name__ == '__main__':
    input_file, output_file = parser()
    sequence1,sequence2 = read_in_file(input_file)
    mismatch_count = main(sequence1,sequence2)
    write_to_file(output_file,mismatch_count)