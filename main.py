import numpy as np
import matplotlib.pyplot as plt


def prediction(filename, num_bits, N):
    # open the file
    outfile = open(filename, 'r')
    mask = N
    counter = []

    total_predictions = 0
    success = 0
    fail = 0

    for i in range (0, N):
        counter.append(0)

    #static BP
    if (num_bits == 0):

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
    return success






    # close the file

def main():

    # Define Data

    BP_used = ['Static BP','1-bit BP','2-bit BP','3-bit BP']
    successes32bit = []
    successes128bit = []


    successes32bit.append(prediction("gcc.trace.out",0,32))
    successes32bit.append(prediction("gcc.trace.out",1,32))
    successes32bit.append(prediction("gcc.trace.out",2,32))
    successes32bit.append(prediction("gcc.trace.out",3,32))


    successes128bit.append(prediction("gcc.trace.out",0,128))
    successes128bit.append(prediction("gcc.trace.out",1,128))
    successes128bit.append(prediction("gcc.trace.out",2,128))
    successes128bit.append(prediction("gcc.trace.out",3,128))


    x_axis = np.arange(len(BP_used))

    # Multi bar Chart

    plt.bar(x_axis -0.2, successes32bit, width=0.4, label = 'N=32')
    plt.bar(x_axis +0.2, successes128bit, width=0.4, label = 'N=128')

    # Xticks

    plt.xticks(x_axis, BP_used)

    # Add legend

    plt.legend()

    # Display

    plt.show()
    
    while True:
        try:
            # have the user enter a file name
            filename = input("Please enter a filename: ")


            break

        except IOError:
            # prints invalid file if the file does not exist for reading
            print("Invalid filename. Please try again.")
            filename = input("Enter a filename: ")



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