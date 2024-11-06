class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        print("Method in B")

class C(A):
    def method(self):
        print("Method in C")

class D(B, C):
    pass

print(A.mro())
# Check the MRO of class C
print(C.mro())
# Check the MRO of class D
print(D.mro())

c = C()
c.method()
d = D()
d.method()