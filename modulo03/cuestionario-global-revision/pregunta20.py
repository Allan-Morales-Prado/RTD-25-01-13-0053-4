usuarios = ["Allan", "Pamela", "Johnatan", "Josefa", "Sebastian"] # 5
playlist = ["Numb", "Beat it", "BYOB", "Rollin'", "Bring me to life"] # 5

for usuario in range(len(usuarios)):
    for cancion in range(len(playlist)):
        print(usuarios[usuario], "está escuchando: ", playlist[cancion])