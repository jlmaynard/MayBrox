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

# Function defs
def my_counter(data):
    """Counter function to find the occurrences of the words in the data
     Returns a dictionary of values and counts. """
    return counter_class.Counter(data)

def hamming_dist(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

if __name__ == "__main__":
    # GET DATA -----------------------------------------------------------------
    the_data = []
    with open('input.txt') as in_file:
        for line in in_file:
            clean_line = line.strip()
            if clean_line and not clean_line.startswith("#"):
                the_data.append(clean_line)    
    
    # CALCULATE AND PRINT THE RESULTS  -----------------------------------------
    out_file = open('output.txt', 'w')
    out_buff = []

    # Create a dictionary of strings and counts from the_data
    the_data_dict = my_counter(the_data)
        
    # Print the column headers
    out_file.write("{:<20} {:<10}\n".format('String', 'Sorted Count'))
    
    # Print the values
    for item in sorted(the_data_dict, key=the_data_dict.get, reverse=True):
        #print "{:<20} {:<10}".format(item, the_data_dict[item])
        out_file.write("{:<20} {:<10}\n".format(item, the_data_dict[item]))
        out_buff.append(item)
    
    # Find the distances between each string
    out_file.write('\n===========================================\n')
    out_file.write('Hamming distances from string to string:\n')
    out_file.write('Finds all combinations of distance between\n')
    out_file.write('strings starting with the first string\n')
    out_file.write('of highest count.\n')
    out_file.write('===========================================')
    
    for i in range(len(out_buff) - 1):
        out_file.write("\nString {} distance to remaining strings\n".format(i + 1))
        
        for j in range(i + 1, len(out_buff)):
            distance = hamming_dist(out_buff[i], out_buff[j])
            out_file.write(str(distance) + '\n')

    out_file.close()
