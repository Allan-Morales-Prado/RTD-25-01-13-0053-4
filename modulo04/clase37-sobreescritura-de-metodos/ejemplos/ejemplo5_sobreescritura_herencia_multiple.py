class A:
    def metodo(self):
        return "Método de A"

class B(A):
    def metodo(self):
        return "Método de B"

class C(A):
    def metodo(self):
        return "Método de C"

class D(B, C):  # Hereda de B primero
    pass

d = D()
print(d.metodo())  # "Método de B" (primera clase heredada)