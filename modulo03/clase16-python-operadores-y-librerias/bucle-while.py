import getpass as gp

password = gp.getpass("Ingrese su clave para continuar: ")

while password != "gpt20cv1":
  print("Clave incorrecta\n")
  password = gp.getpass("Ingrese su clave para continuar: ")

print("Bienvenido/a")