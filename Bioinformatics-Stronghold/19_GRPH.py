"""
Title: Overlap Graphs
ID: GRPH

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
"""
from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from Bio import SeqIO

def read_fasta(input_location:str)->dict:
    """Takes in a fasta file and returns the header IDs as keys, and sequences as values
    """
    fasta_lst = []
    with open(input_location) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            fasta_lst.append([record.id,str(record.seq)])
    return fasta_lst

def getting_graphs(file:'list_of_lists')-> str:
    """Compares first three nucleotides and last three nucleotides to find connections, then filters equivalent ids
    """
    overlapping_ids = []
    for i in range(len(file)):
        for j in range(len(file)):
            if file[i][1][-3:] == file[j][1][:3]:
                overlapping_ids.append([file[i][0],file[j][0]])
    combined_ids = [f'{i} {j}' for i,j in overlapping_ids if i!= j]
    return '\n'.join(combined_ids)



if __name__ == '__main__':
    input_file, output_file = parser()
    list_of_lists_seqs = read_fasta(input_file)
    return_overlaps = getting_graphs(list_of_lists_seqs)
    write_to_file(output_file,return_overlaps)
    