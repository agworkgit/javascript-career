infile = open('values.txt', 'rt') # open file
outfile = open('values-totaled.txt', 'wt') # create file if if doesn't exist

print('Processing input')

sum = 0

for line in infile:
    sum += int(line)
    print(line.rstrip(), file=outfile)

print('\nTotal: ' + str(sum), file=outfile)

outfile.close()

print('Output complete')
