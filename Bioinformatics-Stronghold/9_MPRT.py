"""
Title: Finding a Protein Motif
ID: MPRT

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_fasta import read_fasta
from Bio.Seq import Seq
import requests
from Bio import SeqIO

def find_locations(s):
    lst = []
    for i in range(len(s)-4+1):
        current_nucleotides = s[i:i+4]
        if current_nucleotides[0] == 'N' and current_nucleotides[1] != 'P' and current_nucleotides[2] in ['S','T'] and current_nucleotides[3] != 'P':
            lst.append(i+1)
    return lst
    
def read_in_fasta(location):
    with open(location) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            sequence = record.seq
            return sequence


if __name__ == '__main__':
    input_file, output_file = parser()
    file = open(input_file,'r')
    content = [i.strip() for i in file.readlines()]
    output_string = ''
    fasta_path = 'http://www.uniprot.org/uniprot/'

    for uniprot_id in content:
        fasta_full_path = fasta_path + uniprot_id +'.fasta'
        r = requests.get(fasta_full_path)
        temp_path = '/Users/mac/Desktop/Bioinfomatics-solutions/Bioinformatics-Stronghold/temp/' + uniprot_id + '.fasta'
        with open(temp_path, 'wb') as f:
            f.write(r.content)
        seq_locations = list(map(str,find_locations(read_in_fasta(temp_path))))
        if len(seq_locations) > 0:
            out_locations = ' '.join(seq_locations)
            output_string += uniprot_id + '\n' + out_locations + '\n'

    write_to_file(output_file,output_string)