"""
Title: Open Reading Frames
ID: ORF

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta
from Bio.Seq import Seq
from Bio import SeqIO
import re
def return_dna_list(dna:'Seq') -> list:
    """Takes in sequence and returns all dna the begin with ATG, forward and reverse
    """
    dna_reverse = str(dna.reverse_complement())
    dna = str(dna)
    all_starts = []
    all_starts = [dna[m.start():] for m in re.finditer('ATG', dna)]
    all_starts_rev = [all_starts.append(dna_reverse[m.start():]) for m in re.finditer('ATG', dna_reverse)]
    return all_starts


if __name__ == '__main__':
    input_file, output_file = parser()
    fasta_seqs = list(read_fasta(input_file).values())[0]
    dna_list = return_dna_list(fasta_seqs)
    translated_list =list(map(lambda x: str(Seq(x).translate()), dna_list)) #Translate starting with each start codon across frames
    filted_list = set([i[:i.find('*')] for i in translated_list if '*' in i]) #Finds reading frame that contains stop codon
    output_proteins = '\n'.join(filted_list)
    write_to_file(output_file,output_proteins)
