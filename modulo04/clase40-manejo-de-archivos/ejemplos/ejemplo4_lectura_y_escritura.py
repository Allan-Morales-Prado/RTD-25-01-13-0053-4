try:
  edad = int(input("Ingrese su edad:\n"))
except Exception as e:
  with open("ultimo_error.log", "r+") as log:
    # print(log.read())
    log.write(f"ERROR: {e}")