class PelotaDeDeporte():
    tipo = "Deporte"

class PelotaDePlastico():
    tipo = "Plástico"

class PelotaDePingPong(PelotaDePlastico, PelotaDeDeporte):
    pass

# Salida: "Deporte" (primera clase heredada)
print(PelotaDePingPong.tipo)