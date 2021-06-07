
def write_to_file(output_loc:str,string:str)-> None:
    """Writes to an output_location with the contents contained in string
    """
    out = open(output_loc,'w')
    out.write(string)
    out.close()