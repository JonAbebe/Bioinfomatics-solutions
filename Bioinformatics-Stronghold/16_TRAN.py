"""
Title: Transitions and Transversions
ID: TRAN

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta
from collections import Counter

dict_conv = {'AG':'transition','CT':'transition','AC':'transversion','GT':'transversion','AT':'transversion','CG':'transversion'}

def get_trans_count(seq1:str,seq2:str)->dict:
    """Takes in two sequences, combines similar indices and references dict_conv
    """
    final_lst = []
    for i in range(len(seq1)):
        event = seq1[i]+seq2[i]
        if event[0] != event[1]:
            event = seq1[i]+seq2[i]
            event = ''.join(sorted(event))
            final_lst.append(dict_conv[event])
    return Counter(final_lst)
if __name__ == '__main__':
    input_file, output_file = parser()
    s = list(map(str,read_fasta(input_file).values()))
    trans_count = get_trans_count(s[0],s[1])
    return_ratio = str(trans_count['transition']/trans_count['transversion'])
    write_to_file(output_file,return_ratio)
    
