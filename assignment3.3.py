'''Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12'''

 


def string_test():
    s=input('enter text: ')
    d={"U_CASE":0, "L_CASE":0}
    for c in s:
        if c.isupper():
           d["U_CASE"]+=1
        elif c.islower():
           d["L_CASE"]+=1
        else:
           pass

    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["U_CASE"])
    print ("No. of Lower case Characters : ", d["L_CASE"])

string_test()














