print ("Hello world")
number = int(input("Input number :"))
for i in range (1,number+1):
    print (' '*(number-i),'*'*(2*i-1))

print ("segitiga dari kanan")
Y=input("Input number :")
Y = int(Y)
i=0
while i<=Y:
    print ("*"*i)
    i= i + 1

print("segitiga dari kiri")
number = int(input("Input number :"))
for i in range(1,number+1):
    print (" "*(number-i),"*" *i)

print("segitiga kebalik dari kanan ke kiri")
number = int(input("Input number :"))
for i in range (1,number+1):
    print("*" * (number-i+1))

print ("Segitiga kebalik dari kiri ke kanan")
X = input("Input number :")
X = int(X)
i = 0
j = X
while i<=X:
    print(" " * i,"*"*j)
    i = i +1
    j = j-1

print ("Diamond")
number = int(input("Input number :"))
A = 1
B = number
C = 1
D = number
E = ((number*2)-1)
F = 1
while D >=0:
    while C<number:
        print (" "*B,"*"*A)
        B = B-1
        A = A+2
        C = C+1
    print (" "*F, "*"*E)
    F = F + 1
    E = E-2
    D = D-1