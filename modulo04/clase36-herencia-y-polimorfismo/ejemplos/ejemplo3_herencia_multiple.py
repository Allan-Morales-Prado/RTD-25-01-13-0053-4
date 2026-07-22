class PelotaDeDeporte():
    tipo = "Deporte"

class PelotaDePlastico():
    tipo = "Plástico"

class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    pass

# Salida: "Deporte" (primera clase heredada)
print(PelotaDePingPong.tipo)