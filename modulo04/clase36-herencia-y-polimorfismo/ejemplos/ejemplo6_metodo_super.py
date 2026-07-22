class PelotaDePlastico():
    def __init__(self):
        self.rebotes = []
    
    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes += [int(altura), 0]
            altura //= 1.1

class PelotaDeJuguete(PelotaDePlastico):
    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes += [altura, 0]
            altura //= 2

# Uso
pdj = PelotaDeJuguete()
pdj.rebotar(5)
print(pdj.rebotes)  # [5, 0, 1, 0]

# Se hace llamado al método del padre
super(type(pdj), pdj).rebotar(5)
print(pdj.rebotes)  # [5, 0, 2, 0, 1, 0]