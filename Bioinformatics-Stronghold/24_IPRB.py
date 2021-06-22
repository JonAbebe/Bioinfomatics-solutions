"""
Title: Mendel's First Law
ID: IPRB

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

from helper_scripts.argument_parsing import parser
from helper_scripts.output_text import write_to_file
from helper_scripts.read_text import read_text
import itertools

def Calculation_probablity(k,m,n):
    """ Using complementary probability of getting zero dominate alleles subtract this total from from overall total
    """
    N = float(k+m+n)
    return(1 - 1/N/(N-1)*(n*(n-1) + n*m + m*(m-1)/4.))

        
if __name__ == '__main__':
    input_file, output_file = parser()
    file = open(input_file,'r')
    contents = list(map(int,file.read().strip().split(' ')))
    k,m,n = contents
    probablity = Calculation_probablity(k,m,n)
    write_to_file(output_file,str(probablity))
