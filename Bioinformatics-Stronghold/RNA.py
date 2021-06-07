"""
Title: Transcribing DNA into RNA
ID: RNA

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

from helper_scripts.read_text import read_text
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file

def main(sequence:str)->str:
    """Takes in a DNA string and replaces all occurrences of 'T' with 'U'
    """
    return sequence.replace('T','U')


if __name__ == '__main__':
    input_file, output_file = parser()
    transcribed_DNA = main(read_text(input_file))
    write_to_file(output_file,transcribed_DNA)