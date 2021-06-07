from Bio import SeqIO
def read_fasta(input_location:str)->dict:
    """Takes in a fasta file and returns the header IDs as keys, and sequences as values
    """
    fasta_dict = {}
    with open(input_location) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            fasta_dict[record.id] = record.seq
    return fasta_dict