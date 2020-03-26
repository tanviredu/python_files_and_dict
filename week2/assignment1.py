

def main():
    ## give a text and then find the position
    ## and number pursing from the text
    text = "X-DSPAM-Confidence:    0.8475";
    a = text[-6:]
    b = float(a)
    print(b)
    print(text.find(":"))


main()
