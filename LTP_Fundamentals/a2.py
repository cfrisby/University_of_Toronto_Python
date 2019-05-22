def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    nucleotides_count = 0

    for char in dna:
        if char == nucleotide:
            nucleotides_count = nucleotides_count + 1

    return nucleotides_count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """

    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if dna is a valid dna sequence (dna contains no characters
    other than 'A', 'T', 'C', and 'G'.

    >>> is_valid_sequence('ATCGCT')
    True
    >>> is_valid_sequence('ATcGCT')
    False
    >>> is_valid_sequence('CTSAT')
    False
    """

    is_valid = True

    for char in dna:
        if char not in "ATCG":
            is_valid = False

    return is_valid

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Insert DNA sequence dna2 into DNA sequence dna1 at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('ATCC', 'GT', 0)
    'GTATCC'
    >>> insert_sequence('GTAACG', 'TTC', -1)
    'GTAACGTTC'
    >>> insert_sequence('ACTCGAA', 'GCGCT', -3)
    'ACTCGGCGCTAA'
    """

    combined_sequence = ''
    
    if index >= 0:
        combined_sequence = dna1[:index] + dna2 + dna1[index:]
    else:
        combined_sequence = dna1[:len(dna1)+index+1] + dna2 + dna1[len(dna1)+index+1:]

    return combined_sequence

def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide which is complementary to the parameter nucleotide.

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """

    complement = ''
    
    if nucleotide == 'A':
        complement = 'T'
    if nucleotide == 'T':
        complement = 'A'
    if nucleotide == 'C':
        complement = 'G'
    if nucleotide == 'G':
        complement = 'C'

    return complement

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence which is complementary to the dna.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CGGC')
    'GCCG'
    """

    complementary_dna = ''

    for char in dna:
        complementary_dna = complementary_dna + get_complement(char)

    return complementary_dna
