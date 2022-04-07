import math
def main():
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
    # read the file
    #data = outfile.read()

    # convert data into a string
    #data = str(data)

    # number of bits: 0, 1, 2, or 3
    num_bits = int(input("Number of bits to use: "))

    # size of branch prediction buffer (assert N  to be a power of 2)
    N = int(input("Specify size of the branch prediction buffer: "))
    #assert N is math.pow()

    array = []

    #static BP
    if (num_bits == 0):
        for i in range (0, N):
            array.append(0)
            address = outfile.readline(i)







    # tally results across all branches and report:
    # total number of branches
    # percentage of correct predictions
    # percentage of incorrect predictions





    # close the file
    outfile.close()


main()