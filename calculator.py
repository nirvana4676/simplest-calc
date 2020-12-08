what = input("what to do? (+ - / *): " )

a = float (input("first number: ") )

b =  float (input("second number: ") )


if what == "*":
    c = a * b
    print (c)


elif what == "/":
    c = a / b
    print (c)    


elif what == "+":
    c = a + b
    print (c)


elif what == "-":
      c = a - b
      print (c)

else:
    print("wrong symbol,only + * - /")

input()
