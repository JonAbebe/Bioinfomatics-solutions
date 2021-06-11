"""
Title: Locating Restriction Sites
ID: REVP

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta
from Bio.Seq import Seq
from Bio import SeqIO


def return_locations(full_string:'sequence') -> list:
    """Takes in a sequence returns a list containing position and length of every reverse palindrome
    """
    total_list = []
    for string_length in range(4,13):
        for i in range(len(full_string)):
            current_string = full_string[i:(i+string_length)]
            if len(current_string) == string_length:
                reverse_comp = current_string.reverse_complement()
                if current_string == reverse_comp:
                    total_list.append([i+1,string_length])
    return total_list 
if __name__ == '__main__':
    input_file, output_file = parser()
    sequence = list(read_fasta(input_file).values())[0]

    lst_of_seqs = return_locations(sequence)
    sorted_total = sorted(lst_of_seqs, key=lambda x: x[0])
    return_string = ''
    for i in sorted_total:
        add_newline = str(i[1]) +'\n'
        return_string += f'{i[0]} {add_newline}'
    write_to_file(output_file,return_string)