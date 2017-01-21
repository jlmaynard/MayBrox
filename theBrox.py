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
# Output: A sorted list of strings by count
# Future mods: Sorted list of matching strings by similarity weighting
#
# IDE = Wing Pro, 6.01
#
# Copyright "MayBrox Inc.", 2017
# :-)
#

# from collections import Counter
import counter_class

# GET DATA -------------------------------------------------------------------
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

if __name__ == "__main__":
    # CALCULATE AND PRINT THE RESULTS  ---------------------------------------
    out_file = open('output.txt', 'w')

    # Create a dictionary of strings and counts from the_data
    the_data_dict = my_counter(the_data)
        
    # Print the column headers
    print "{:<20} {:<10}".format('String', 'Count')
    out_file.write("{:<20} {:<10}\n".format('String', 'Count'))
    
    # Print the values
    for item in sorted(the_data_dict, key=the_data_dict.get, reverse=True):
        print "{:<20} {:<10}".format(item, the_data_dict[item])
        out_file.write("{:<20} {:<10}\n".format(item, the_data_dict[item]))

    out_file.close()
