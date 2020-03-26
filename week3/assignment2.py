
def main():
    fname = input("Enter file name: ")
    if len(fname) < 1:
        fname = "mbox-short.txt"
    fh = open(fname)
    
    ## putting the mal that starts with X-DSPAM-Confidence
    ## consider they are spam
    ## and it also show the probability
    ## so we take that and store this probability
    ## in array
    spam_prob = []
    for line in fh:
        if line.startswith("X-DSPAM-Confidence:"):
            spam_prob.append(float(line[-6:])) ### this are the portion of  the  line where the propbility 

    #print(spam_prob)
    ## easy way to do it
    #total = sum(spam_prob)
    #print(total)

    total = 0

    for i in spam_prob:
        total = total+i
    print(total)

    mean = total/len(spam_prob)
    print("Average spam confidence:",mean)

    


main()
