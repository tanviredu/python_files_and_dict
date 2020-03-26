

def main():
    ## taking input the file name
    fname = input("Enter the file name: ")
    if len(fname) <1:
        fname = "mbox-short.txt"
    fh = open(fname)
    ## read the file
    a = fh.read()
    ## changing to upper case and removing the
    ## white space
    print(a.upper().rstrip())

main()
