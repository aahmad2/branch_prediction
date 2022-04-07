import math
def main():

    address = int('7ff3b56ee932', 16)
    print(address)
    # print("address % 32 :")
    # print(address % 32)
    #
    # print()
    # address = int('7ff3b56ee8e8', 16)
    # print(address)
    # print("address % 32 :")
    # print(address % 32)

    # user specifies:
        # input trace file

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
    # TODO: assert N is math.pow()

    coutner = []
    line = outfile.readline()
    split_line = line.split()

    #static BP
    if (num_bits == 0):
        for i in range (1, N):
            coutner.append(0)
            address = int(split_line[0],16)
            bit = int(split_line[1], 2)

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