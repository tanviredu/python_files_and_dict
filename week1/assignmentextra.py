
def main():
    ## taking the file input name
    name = input("Enter Filename: ")
    if len(name) < 1:
        name = 'mbox-short.txt'

    ## create a file handler
    handle = open(name);
    f = handle.read()  ## this return the whole file content
    #print(f)
    b = f.split("\n") ### create a list in every line as a element
    ### loop through it
    d = []
    for item in b:
        if item.startswith("From "):  ## checking the sender in email
            ## splittingthe From : with the sender
            c = item.split(":")

            ## find the company domain
            d.append(c[0])

    email = []
    for item in d:
        email.append(item.split()[1])
    
    domain=[]
    for item in email:
        domain.append(item.split('@')[1])


    domain.sort()
    counts = {}
    for j in domain:
        counts[j] = domain.count(j)

    for x,y in counts.items():
        print("{} Company send {} email ".format(x,y))
    
main()
