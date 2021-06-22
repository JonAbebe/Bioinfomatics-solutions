"""
Title: Inferring mRNA from Protein
ID: MRNA

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_text import read_text
import pandas as pd
if __name__ == '__main__':
    input_file, output_file = parser()
    file = open(input_file,'r')
    contents = file.read().strip()
    AA_table = pd.read_csv('/Users/mac/Desktop/Bioinfomatics-solutions/Bioinformatics-Stronghold/temp/AA_table.txt',sep = '\t')
    value_count = AA_table[AA_table['AA'] == 'O'].shape[0]
    for i in contents:
        value_count = value_count * AA_table[AA_table['AA'] == i].shape[0] % 1000000
    write_to_file(output_file,str(value_count))