"""
Title: Finding a Spliced Motif
ID: SSEQ

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
"""

from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta
from collections import defaultdict
import re
keep_dic = defaultdict(list)

def find_indices(sequence:str,substring:str) -> dict:
    """Takes in sequence and substring, returns indices of every position in sequences
    i.e. sequence = 'ABCAD', substring = 'A' returns {'A':[0,3]}
    """
    keep_dic = defaultdict(list)
    for i in range(len(substring)):
        all_locals = [match.start()+1 for match in re.finditer(substring[i], sequence)]
        keep_dic[i] = all_locals
    return keep_dic
    
def return_none_consecutive(dic_occur:'dict_of_lists',substring:str) -> list:
    final_lst = []
    for i in range(len(substring)):
        if len(final_lst) == 0:
            final_lst.append(dic_occur[i][0])
        else:
            prev_local = final_lst[i-1]
            filted_vals = [idx for idx in dic_occur[i] if idx > prev_local+1]
            final_lst.append(filted_vals[0])
    return map(str,final_lst)
    
if __name__ == '__main__':
    input_file, output_file = parser()
    s = read_fasta(input_file).values()
    
    lst_of_seqs = list(map(str,s))
    full_string = lst_of_seqs.pop(0)
    
    dict_of_occurences = find_indices(full_string,lst_of_seqs[0])
    return_lst = return_none_consecutive(dict_of_occurences,lst_of_seqs[0])
    final_return = ' '.join(return_lst)
    write_to_file(output_file,final_return)
