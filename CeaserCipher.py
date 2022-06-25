#Ceaser cypher algorithm

def encryption():
    ct = ''
    alp = 'abcdefghijklmnopqrstuvwxyz'
    print("")
    pt = input(">>Please Enter Plain Text_:")
    pt = pt.lower()
    key = int(input(">>Please Enter A Key_:"))
    for a in pt:
        ind = alp.index(a)
        if (ind+key)>25:
            mainct = (ind+key)%26
        else:
            mainct = ind+key
        ct = ct+alp[mainct] 
    print("")
    print("Encryption:")
    print("Plain text: ",pt)
    print("Cipher text: ",ct)
    print("Key used: ",key)
    print("")

def decryption():
    pt = ''
    alp = 'abcdefghijklmnopqrstuvwxyz'
    print("")
    ct = input(">>Please Enter Cipher Text_:")
    ct = ct.lower()
    key = int(input(">>Please Enter A Key_:"))
    for a in ct:
        ind = alp.index(a)
        if (ind+key)>25:
            mainct = (ind-key)%26
        else:
            mainct = ind-key
        pt = pt+alp[mainct] 
    print("")
    print("Decryption:")
    print("Cipher text: ",ct)
    print("Plain text: ",pt)
    print("Key used: ",key)
    print("")

def ceaserCipher():
    print("______________________________")
    print("")
    print("Ceaser Cipher Algorithm. (by TK)")
    print("______________________________")
    print("Please Choose Encryption or Decryption__")
   
    try:
        print("")
        rv = int(input(">>Enter 1 for encryption or 2 for Decryption__:"))
        if(rv == 1):
            encryption()
        elif(rv == 2):
            decryption()
        else:
            print("Enter 1 or 2 ONLY...")
            print("Programme is restarting now...")
            print("______________________________")
            ceaserCipher()

    except(ValueError):
        print("______________________________")
        print("You have entered something wrong, Now Programme is going to close, you have to restart it")
        print("Sorry! BYE...")
        print("______________________________")

ceaserCipher()