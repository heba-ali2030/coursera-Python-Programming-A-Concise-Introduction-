# READING AND WRITING TEXT FILES 

def print_file(filename):
    """ Opens file and prints its contents line by line. """
    infile = open(filename)
    
    for line in infile:
        print(line, end="") # the file has "\n" at the end of each line already
    
    infile.close()
print_file()