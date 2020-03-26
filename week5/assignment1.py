

def main():
    fname = input("Enter the file name: ")
    if len(fname) <1:
        fname = "mbox-short.txt"
    handle = open(fname)
    emaillist = []
    datadict = {}

    for line in handle:
        line = line.rstrip()
        if not line.startswith("From "):
            continue
        else:
            line = line.split()
            line = line[1]
            emaillist.append(line)
    for email in emaillist:
        datadict[email] = emaillist.count(email)
    email_add = None
    max_email =None
    ## which email is send maximum time
    for email,occur in datadict.items():
        if max_email is None or occur > max_email:
            max_email = occur
            email_add = email

    print(email_add,max_email)
main()
