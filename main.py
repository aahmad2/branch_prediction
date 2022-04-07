import math
def main():

    try:
        # have the user enter a file name

        #filename = input("Welcome. Enter a filename: ")
        filename = 'gcc.trace.out'


    except IOError:
        # prints invalid file if the file does not exist for reading
        print("Invalid file.")
        filename = input("Enter a filename: ")
        # passes the value of filename to the function num_of_characters so the rest can execute

    # open the file
    outfile = open(filename, 'r')

    # number of bits: 0, 1, 2, or 3
    #num_bits = int(input("Number of bits to use: "))
    num_bits = 0

    # size of branch prediction buffer (assert N  to be a power of 2)
    #N = int(input("Specify size of the branch prediction buffer: "))
    N = 32
    mask = N-1
    # TODO: assert N is math.pow()

    counter = []

    total_predictions = 0
    success = 0

    #static BP
    if (num_bits == 0):
        for i in range (1, N):
            counter.append(0)

        for line in outfile:
            if line != '#eof\n':
                split_line = line.split()
                address = int(split_line[0],16)
                bit = int(split_line[1], 2)
                total_predictions +=1
                if counter[address%mask] == bit:
                    success +=1
        print(success/total_predictions)

    elif (num_bits == 1):
        pass
    elif (num_bits == 2):
        pass
    elif (num_bits == 3):
        pass

       

    # tally results across all branches and report:
        # total number of branches
        # percentage of correct predictions
        # percentage of incorrect predictions





    # close the file
    outfile.close()


main()