"""
Title: Calculating Protein Mass
ID: PRTM

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_text import read_text
import pandas as pd

def clean_AA_table(path):
    weight = pd.read_csv(path,sep = '\t',header = None)
    weight[['AA','weight']] = list(map(lambda x:x.split('   '),list(weight[0])))
    weight = weight.drop([0],axis =1)
    return weight

if __name__ == '__main__':
    AA_table = clean_AA_table('/Users/mac/Desktop/Bioinfomatics-solutions/Bioinformatics-Stronghold/temp/AA_weights.txt')
    input_file, output_file = parser()
    seq = read_text(input_file)
    calc = 0
    for i in seq:
        calc += float(list(AA_table[AA_table['AA'] ==i]['weight'])[0])
    write_to_file(output_file,str(calc))
    