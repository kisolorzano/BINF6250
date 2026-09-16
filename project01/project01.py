#!/usr/bin/env python
from pprint import pprint

def parse_line(line):
    """
    Takes a string representing a line from a VCF file, extracts the 
    AF_EXAC and CLNDN values, and returns a list of valid diseases 
    if the variant is rare.
    """
    # Skip Meta-information lines that start with ## and header lines that start with #
    if line.startswith('#'):
        return []

    # Split the line into columns based on tabs (\t)
    columns = line.strip().split('\t')

    # Check to ensure there are at least 8 columns
    if len (columns) < 8:
        return []

    # Identify and split INFO column by semi-colon to get individual key-value pairs
    info_column = columns[7]
    info_pairs = info_column.split(';')

    # Build dictionary of these key-value pairs
    info_dict = {}
    for pair in info_pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            info_dict[key] = value

    # Extract the AF_EXAC data to determine the rarity of the variant
    # Check if AF_EXAC is present, return an empty list if not
    if 'AF_EXAC' not in info_dict:
        return []

    # Convert AF_EXAC to a float
    af_exac = float(info_dict['AF_EXAC'])

    # If variant is rare
    if af_exac < 0.0001:
        # Associated diseases in CLNDN:
        if 'CLNDN' in info_dict:
            # Split the diseases into list, they are pipe (|) separated
            disease_list = info_dict['CLNDN'].split('|')
            # Loop though the above list and filter out invalid disease names,
            # append the valid ones.
            valid_diseases = []
            for disease in disease_list:
                if disease != 'not_specified' and disease != 'not_provided':
                    valid_diseases.append(disease)
            return valid_diseases

    # If variant is not rare, return empty list
    return []

def read_file(file_name):
    """
    Opens a VCF file, reads it line by line, and counts the occurrences
    of rare diseases using parse_line.
    """
    disease_counts = {}

    # Open and read the file line by line
    with open(file_name) as vcf_file:
        for line in vcf_file:
            diseases_found = parse_line(line)

            # Loop though 'disease_found', if a disease is already in 'disease_counts', add 1.
            # if not, set it to 1
            for disease in diseases_found:
                if disease in disease_counts:
                    #add 1 to the value
                    disease_counts[disease] += 1
                else:
                    #create a new key with value = 1
                    disease_counts[disease] = 1


    # Return the final tally dictionary
    return disease_counts


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
