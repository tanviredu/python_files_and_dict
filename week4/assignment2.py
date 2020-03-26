
def main():
    fname = input("Enter the file name :")
    if len(fname) <1:
        fname = 'mbox-short.txt'

    handle = open(fname)
    ## we gare going to find how many sender are there
    ## we do it by counting the "From" word how much happend

    count = 0
    for line in handle:
        line = line.rstrip()  ## removing the ending space
        if not line.startswith("From "):
            continue
        else:
            line = line.split()
            ## we take the emil
            print(line[1])
            ## and we increase the count
            count+=1
    print('There were', count, 'lines in the file with From as the first word')




main()
