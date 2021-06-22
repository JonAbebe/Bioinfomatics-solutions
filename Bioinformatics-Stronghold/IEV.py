"""
Title: Calculating Expected Offspring
ID: IEV

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
"""

from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta

genotype_pairs = ["AA-AA","AA-Aa","AA-aa","Aa-Aa","Aa-aa","aa-aa"]
offspring_count = [2.0,2.0,2.0,1.5,1.0,0.0]
pair_dict = dict(zip(genotype_pairs,offspring_count))

def return_dominate_total(count_of_pairs:'list')->int:
    """Takes in a list of pairs, maps to dictionary and returns the count
    """
    total = [int(float(count_of_pairs[i]) * pair_dict[genotype_pairs[i]]) for i in range(len(count_of_pairs)) if count_of_pairs[i] != 0]
    return str(sum(total))

if __name__ == '__main__':
    input_file, output_file = parser()
    file = open(input_file,'r')
    #print(file)
    contents = file.read().split(' ')
    final_count = return_dominate_total(contents)
    write_to_file(output_file,final_count)
    