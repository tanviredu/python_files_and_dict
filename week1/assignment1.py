
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
            ## find the date
            d.append(c[0][-2:])
            #d.append(c[0][-2]) ## the first element with 
            ## string indexing to last two element of the string
            ## to find the date
    #print(d)  ## print all the date
    d.sort()   # sorting the date
    #print(d)

    ## so there are some value that comes in 
    ## duplicate that means we got multiple mails in one day
    ## lets count it
    ## we need a dict
    count = {}
    for j in d:
        count[j] = d.count(j)
    #print(count)
    ## now print it
    for k,i in count.items():
        print(k,i)

            
main()
