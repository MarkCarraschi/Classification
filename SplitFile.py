splitLen = 10000         # 10000 lines per file
outputBase = 'output' # output.1.txt, output.2.txt, etc.


########## FILE PATH
variablePathFile = '/home/mark/Documents/Datasets/tweets2009-06.txt'

# This is shorthand and not friendly with memory
# on very large files (Sean Cavanagh), but it works.
input = open(variablePathFile, 'r').read().split('\n')

at = 1
for lines in range(0, len(input), splitLen):
    # First, get the list slice
    outputData = input[lines:lines+splitLen]

    # Now open the output file, join the new slice with newlines
    # and write it out. Then close the file.
    output = open(outputBase + str(at) + '.txt', 'w')
    output.write('\n'.join(outputData))
    output.close()

    # Increment the counter
    at += 1
