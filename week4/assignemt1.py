def main():
    fname = input("Enter the file name :")
    if len(fname) < 1:
        fname = 'romeo.txt'
    handle = open(fname)

    t = []  ### for storing every line in the text
    for line in handle:
        line  = line.rstrip() ### removing the right space
        line = line.split()  ### splitting based on space
        ## every word is going get splitted
        ## loop through every word
        for word in line:
            if word in t:
                continue  ## if the word in the list then dont append to the list just loop again

            else:
                t.append(word)


    ## sort it
    t.sort()
    print(t)




main()
