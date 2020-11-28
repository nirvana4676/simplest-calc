#calculator for IT lesson

what = input("what to do? (+ -): " )
#write,what operation u want to do
a = float (input("first number: ") )
b =  float (input("second number: ") )
#write numbers,to do operations with them
if what == "+":
    c = a + b
    print (c)
#prints if plus wroted
elif what == "-":
      c = a - b
      print (c)
#prints if minus wroted
else:
    print("wrong symbol,only =,-")
#prints if wrong symbol wroted

input()
