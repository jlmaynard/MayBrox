# This program reads an input file that represents an array of measurement 
# data in the following format:
# 0 1 0 1 0
# 1 0 0 1 1
# 0 0 1 1 0
# 1 0 1 1 1
# 0 0 0 0 1
# 0 0 0 0 0
# 1 1 1 1 1
#
# Output: A sorted list of matching rows
# Future mods: Sorted list of matching rows by closeness weighting
#
# Copyright "MayBrox Inc.", 2017
# :-)
#

# from collections import Counter
import counter_class

# GET DATA -------------------------------------------------------------------

# This gets the input data..................................................
the_data = []
with open('input.txt') as in_file:
    for line in in_file:
        clean_line = line.strip()
        if clean_line and not clean_line.startswith("#"):  # is not empty
            the_data.append(clean_line)


def my_counter(data):
    """Counter function to find the occurrences of the words in the data
     Returns a dictionary of values and counts. """
    return counter_class.Counter(data)

# Run the main() if this is the main file. -----------------------------------
if __name__ == "__main__":
    # CALCULATE AND PRINT THE RESULTS  ---------------------------------------
    out_file = open('output.txt', 'w')

    the_data_dict = my_counter(the_data)
    for keys, values in the_data_dict.items():
        out_file.write(keys + '\n')
        out_file.write(str(values) + '\n')
        
    for item in the_data_dict:
        print item, the_data_dict[item]    

    # Find the max value
    out_file.write('\nThe most common value is:\n')
    out_file.write(max(the_data_dict, key=lambda x: the_data_dict.get(x)))

    # Don't forget to close that output file
    out_file.close()
