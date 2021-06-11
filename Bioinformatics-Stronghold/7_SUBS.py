"""
Title: Finding a Motif in DNA
ID: SUBS

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""


from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file



#test = ' '.join([str(i+1) for i in range(0,len(full)) if full[i:(i+len(sub))] == sub ])
def get_subsequences(full,sub):
    """Takes a full sequence and a subsequnce, and finds the indices of occurence
    """
    return ' '.join([str(i+1) for i in range(0,len(full)) if full[i:(i+len(sub))] == sub ])

if __name__ == '__main__':
    input_file, output_file = parser()
    file = open(input_file,'r')
    sequence = [i.strip() for i in file.readlines()] #first index is the full sequence, 2nd is sub
    final_indices = get_subsequences(sequence[0],sequence[1])
    write_to_file(output_file,final_indices)
