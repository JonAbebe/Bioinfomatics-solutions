import argparse

def parser():
    """Simply takes in an input file and returns the output location to write to.
    """
    ap = argparse.ArgumentParser(description = 'Takes in input dataset and returns answer...')

    requiredGrp = ap.add_argument_group('required arguments')
    requiredGrp.add_argument("-i",'--input_file', required=True, help="input file location")
    requiredGrp.add_argument("-o",'--output_location', required=True, help="output file location")
    args = vars(ap.parse_args())
    input_file = args['input_file']
    output_file = args['output_location'] +'.txt'
    return input_file, output_file