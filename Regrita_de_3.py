print ("   NILSON SOFTWARE")
print ("####################")
print ("# Regrita de Triês #")
print ("####################")
print()
o=input("Diretamente (1) ou Inversamente proporcional (2)? ")
print()
a=input ("Insira a variável A:")
b=input ("Insira a variável B:")
c=input ("Insira a variável C:")
d=input ("Insira a variável D:")
if a=="x" or a=="X" and o=="1":
    resultado=(int(b)*int(c)/int(d))
if a == "x" or a=="X" and o == "2":
    resultado = (int(c) * int(d) / int(b))

if b=="x"  or b=="X" and  o=="1":
    resultado=(int(a)*int(d)/int(c))
if b=="x" or b=="X" and o=="2":
    resultado = (int(d) * int(c) / int(a))

if c=="x" or c=="X" and o=="1":
    resultado=(int(a)*int(d)/int(b))
if c=="x" or c=="X" and o=="2":
    resultado = (int(a) * int(b) / int(d))

if d=="x" or d=="X" and o=="1":
    resultado=(int(c)*int(b)/int(a))
if d=="x" or d=="X" and o=="2":
    resultado = (int(a) * int(b) / int(c))

print()
print (a+ "            "+ b)
print ("------"+"        "+"------")
print (c+ "              "+ d)
print ()
print ("X="+str(int(resultado)))






