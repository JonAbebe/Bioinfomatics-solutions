
def read_text(file_location:str)-> str:
    """Takes in a file location, opens/parses the file and returns the string contained
    ***Note This is different from handling fasta files which contain headers nor does it hand \
    multiple lines of text (assumes one line)*** 
    """
    file = open(file_location,'r')
    sequence = file.read().replace('\n','')
    return sequence