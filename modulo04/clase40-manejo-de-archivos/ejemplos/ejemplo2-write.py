import time

try:
    edad = int(input("Ingrese su edad: \n"))
except Exception as e:
    with open(f"{round(time.time())}.log", "w") as log:
        log.write(f"Error: {e}")