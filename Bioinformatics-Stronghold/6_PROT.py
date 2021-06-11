"""
Title: Translating RNA into Protein
ID: PROT

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""


from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_text import read_text
from Bio.Seq import Seq





if __name__ == '__main__':
    input_file, output_file = parser()
    sequence = read_text(input_file)
    #print(Seq(sequence).translate(to_stop=True))
    write_to_file(output_file,str(Seq(sequence).translate(to_stop=True)))