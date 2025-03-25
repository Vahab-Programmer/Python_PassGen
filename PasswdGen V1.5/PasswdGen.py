
from Modules.DictModule import Dictionary
import random
__author__="Vahab Programmer https://Github.com/Vahab-Programmer"
__version__="0.1.5"
def PasswdGen(Method,Length):
        if not Length < 8:
            PassResult = "".join(random.choices(Method,k=Length))
            print (PassResult)
            input ("Press Enter To ReGenerate")
        elif not Length:
            print("Length cannot be Empty!")
            input ("Press Enter To ReGenerate")
        else:
            print("Password cannot be 7 or Less")
            input ("Press Enter To ReGenerate")
print("wellcome to Password Generator V1.5")
print("This App can Generate so many Password")
while True:
    print("Please select on Option by number")
    print("""
1.All Letters with digits and symbol
2.UpperCase letters with digits and symbol
3.LowerCase letters with digits and symbol
4.All Letters With symbol only
5.UpperCase Letters With symbol only
6.LowerCase Letters With symbol only
7.All Letters With Digits only
8.UpperCase Letters With Digits only
9.LowerCase Letters With Digits only
10.All Letters only
11.UpperCase Letters only
12.LowerCase Letters only
13.Custome
""")
    UserIn = int(input("Option:"))
    if not UserIn == 0:
        Length = int(input("Length:"))
        if UserIn == 1:
            PasswdGen(Dictionary.letters_full, Length)
        elif UserIn == 2:
            PasswdGen(Dictionary.upcase_full, Length)
        elif UserIn == 3:
            PasswdGen(Dictionary.lowcase_full, Length)
        elif UserIn == 4:
            PasswdGen(Dictionary.letters_with_symbol, Length)
        elif UserIn == 5:
            PasswdGen(Dictionary.upcase_with_symbol, Length)
        elif UserIn == 6:
            PasswdGen(Dictionary.lowcase_with_symbol, Length)
        elif UserIn == 7:
            PasswdGen(Dictionary.letters_with_digits, Length)
        elif UserIn == 8:
            PasswdGen(Dictionary.upcase_with_digits, Length)
        elif UserIn == 9:
            PasswdGen(Dictionary.lowcase_with_digis, Length)
        elif UserIn == 10:
            PasswdGen(Dictionary.letters, Length)
        elif UserIn == 11:
            PasswdGen(Dictionary.upcase, Length)
        elif UserIn == 12:
            PasswdGen(Dictionary.lowcase, Length)
        elif UserIn == 13:
            print("Please enter the words, numbers and symbols you want")
            Custome = input("Custome:")
            PasswdGen(Custome, Length)
        elif UserIn > 13 :
            print ("This Option is Not Avaliable")
            print ("Your Entered Option:",UserIn)
            input("Press Enter to Restart")
        else:
            print ("You cannot Enter String")
            input("Press Enter to Restart")
    else:
        print ("You cannot Enter Option zero or Less!")
        input("Press Enter to Restart")
