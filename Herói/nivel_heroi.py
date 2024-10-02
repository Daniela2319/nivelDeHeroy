while True:
    print("Bem vindo ao sistema de categorias de heróis!")
    nome = input("Coloque o nome do seu Herói: ")
    xp = int(input("Qual valor do XP do seu Herói: "))

    if xp < 1000:
        print(f"Herói {nome} categoria: Ferro")
    elif xp >= 1001 and xp <= 2000:
        print(f"Herói {nome} categoria: Bronze")
    elif xp >= 2001 and xp <= 5000:
        print(f"Herói {nome} categoria: Prata")
    elif xp >= 5001 and xp <= 7000:
        print(f"Herói {nome} categoria: Ouro")
    elif xp >= 7001 and xp <= 8000:
        print(f"Herói {nome} categoria: Platina")
    elif xp >= 8001 and xp <= 9000:
        print(f"Herói {nome} categoria: Ascendente")
    elif xp >= 9001 and xp <= 10000:
        print(f"Herói {nome} categoria: Imortal")
    elif xp >= 10001:
        print(f"Herói {nome} categoria: Radiante")
    else:
        print("Você não tem categoria")

    print(f"{nome} é um herói com {xp} de experiência")

    continuar = input("Deseja adicionar outro herói? (s/n): ").lower()
    if continuar != "s":
        print("Encerrando o programa.")
        break
