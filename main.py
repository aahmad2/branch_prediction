import numpy as np
import matplotlib.pyplot as plt

# method prediction that takes in the user input of the filename, # of bits, and size of buffer
def prediction(filename, num_bits, N):

    # open the file
    outfile = open(filename, 'r')
    mask = N

    # create array for predictions
    counter = []

    # counter for total number of predictions
    total_predictions = 0

    # counter for total number of successes
    success = 0

    # counter for total number of fails
    fail = 0

    # set all initial predictions to 0
    for i in range (0, N):
        counter.append(0)

    # static BP for when num_bits = 0
    if (num_bits == 0):

        # go through each line of the file
        for line in outfile:
            # goes until it reaches the end of the file
            if line != '#eof\n':

                # make each line into a list of strings
                split_line = line.split()

                # gets hexadecimal value from the list and convert to an integer
                address = int(split_line[0], 16)

                # get the prediction bit and convert it to an integer
                bit = int(split_line[1], 2)

                # for each line increment total_predictions by one
                total_predictions += 1

                # form index into branch history table by taking address % N
                # increment success when counter[address % mask] and bit = 0,
                # increment fail otherwise
                if counter[address % mask] == bit:

                    success += 1
                else:
                    fail += 1

        # tally results across all branches and report:
            # total number of branches
            # percentage of correct predictions
            # percentage of incorrect predictions
        print("total number of branches:", total_predictions)
        print("fails: ", '{0:.4g}%'.format(fail/total_predictions * 100))
        print("success: ",'{0:.4g}%'.format(success/total_predictions * 100))

    elif (num_bits == 1):

        for line in outfile:
            if line != '#eof\n':

                split_line = line.split()
                address = int(split_line[0], 16)
                bit = int(split_line[1], 2)
                total_predictions += 1

                if counter[address % mask] == bit:
                    success += 1
                else:
                    fail += 1

                counter[address % mask] = bit


        # tally results across all branches and report:
            # total number of branches
            # percentage of correct predictions
            # percentage of incorrect predictions
        print("total number of branches:", total_predictions)
        print("fails: ", '{0:.4g}%'.format(fail/total_predictions * 100))
        print("success: ", '{0:.4g}%'.format(success/total_predictions * 100))

    elif (num_bits == 2):

        for line in outfile:
            if line != '#eof\n':

                split_line = line.split()
                address = int(split_line[0], 16)
                bit = int(split_line[1], 2)
                total_predictions += 1

                if counter[address % mask] == 2 or counter[address % mask] == 3:
                    prediction = 1
                else:
                    prediction = 0

                if bit == 1:
                    counter[address % mask] = min(counter[address % mask] + 1, 3)
                else:
                    counter[address % mask] = max(counter[address % mask] - 1, 0)

                if prediction == bit:
                    success +=1
                else:
                    fail +=1

        # tally results across all branches and report:
            # total number of branches
            # percentage of correct predictions
            # percentage of incorrect predictions
        print("total number of branches:", total_predictions)
        print("fails: ", '{0:.4g}%'.format(fail/total_predictions*100))
        print("success: ",'{0:.4g}%'.format(success/total_predictions*100))

    elif (num_bits == 3):
        for line in outfile:
            if line != '#eof\n':
                split_line = line.split()
                address = int(split_line[0], 16)
                bit = int(split_line[1], 2)
                total_predictions +=1

                if counter[address % mask] == 4 or counter[address % mask] == 5 or counter[address % mask] == 6 or \
                        counter[address % mask] == 7:
                    prediction = 1

                else:
                    prediction = 0

                if bit == 1:
                    counter[address % mask] = min(counter[address % mask] + 1, 7)
                else:
                    counter[address % mask] = max(counter[address % mask] - 1, 0)

                if prediction == bit:
                    success += 1
                else:
                    fail += 1

        # tally results across all branches and report:
            # total number of branches
            # percentage of correct predictions
            # percentage of incorrect predictions
        print("total number of branches:", total_predictions)
        print("fails: ",'{0:.4g}%'.format(fail/total_predictions*100))
        print("success: ",'{0:.4g}%'.format(success/total_predictions*100,'%'))
    outfile.close()
    return success/total_predictions*100

    # close the file

def make_graph(filename, N1, N2):
    # Define Data

    BP_used = ['Static BP', '1-bit BP', '2-bit BP', '3-bit BP']
    successesN1bit = []
    successesN2bit = []



    successesN1bit.append(prediction(filename, 0, N1))
    successesN1bit.append(prediction(filename, 1, N1))
    successesN1bit.append(prediction(filename, 2, N1))
    successesN1bit.append(prediction(filename, 3, N1))

    successesN2bit.append(prediction(filename, 0, N2))
    successesN2bit.append(prediction(filename, 1, N2))
    successesN2bit.append(prediction(filename, 2, N2))
    successesN2bit.append(prediction(filename, 3, N2))

    x_axis = np.arange(len(BP_used))

    # Multi bar Chart
    plt.ylim(0, 100)

    plt.bar(x_axis - 0.2, successesN1bit, width=0.4, label=f'N={N1}')
    plt.bar(x_axis + 0.2, successesN2bit, width=0.4, label=f'N={N2}')

    # Xticks

    plt.xticks(x_axis, BP_used)

    # Add legend
    plt.title(f"{filename}'s Success Percentages for N={N1} and N={N2}")

    plt.legend()

    # Display

    plt.show()

def main():

    #make_graph("gcc.trace.out", 32, 128)
    #make_graph("curl.trace.out", 32, 128)
    #make_graph("cholesky64.trace.out", 32, 128)
    #make_graph("cs201dynalloc.trace.out", 32, 128)


    
    while True:
        try:
            # have the user enter a file name
            filename = input("Please enter a filename: ")

            outfile = open(filename, 'r')
            outfile.close()
            break

        except IOError:
            # prints invalid file if the file does not exist for reading
            print("Invalid filename. Please try again.")




        # input error handling for number of bits
    while True:
        try:
            # number of bits: 0, 1, 2, or 3
            num_bits = int(input("Number of bits to use: "))

            if num_bits < 0 or num_bits > 3:
                raise ValueError
            break

        except ValueError:
            print("This is not a valid number. Please insert a number 0-3")


    # input error handling for size of N
    while True:
        try:
            # The value of N must be a power of 2
            N = int(input("Specify size of the branch prediction buffer: "))
            assert (N & (N - 1) == 0) and N != 0,AssertionError
            break
        except AssertionError:
            print("Size must be power of 2")
        except ValueError:
            print("Must enter a value.")

    prediction(filename,num_bits,N)

main()