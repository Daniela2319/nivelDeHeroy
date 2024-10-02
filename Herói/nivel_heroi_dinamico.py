import time
import sys


# Função para exibir texto com efeito de digitação
def efeito_digitar(texto, delay=0.05):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Quebra de linha após a exibição do texto


# Função para exibir cores no terminal
def cor_texto(texto, cor):
    cores = {
        "vermelho": "\033[91m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "azul": "\033[94m",
        "ciano": "\033[96m",
        "fim": "\033[0m",
        "negrito": "\033[1m",
    }
    return f"{cores.get(cor, '')}{texto}{cores['fim']}"


# Função principal com laço e animações
while True:
    # Saída inicial com animação
    efeito_digitar("Bem-vindo ao sistema de categorias de Heróis!\n", 0.04)

    nome = input("Coloque o nome do seu Herói: ")
    while True:
        try:
            xp = int(input("Qual valor do XP do seu Herói (número inteiro): "))
            break
        except ValueError:
            print(
                cor_texto(
                    "XP inválido! Por favor, insira um número inteiro.", "vermelho"
                )
            )

    # Definindo a categoria com base no XP
    if xp < 1000:
        categoria = cor_texto("Ferro", "ciano")
    elif 1001 <= xp <= 2000:
        categoria = cor_texto("Bronze", "amarelo")
    elif 2001 <= xp <= 5000:
        categoria = cor_texto("Prata", "cinza")
    elif 5001 <= xp <= 7000:
        categoria = cor_texto("Ouro", "amarelo")
    elif 7001 <= xp <= 8000:
        categoria = cor_texto("Platina", "azul")
    elif 8001 <= xp <= 9000:
        categoria = cor_texto("Ascendente", "verde")
    elif 9001 <= xp <= 10000:
        categoria = cor_texto("Imortal", "vermelho")
    elif xp >= 10001:
        categoria = cor_texto("Radiante", "negrito")
    else:
        cor_texto("XP inválido! Por favor, insira um número inteiro.", "vermelho")

    # Exibindo a categoria com efeito de digitação
    efeito_digitar(f"Avaliando o herói {nome}...\n", 0.06)
    time.sleep(1)
    efeito_digitar(f"Herói {nome} pertence à categoria: {categoria}!", 0.05)
    time.sleep(0.5)
    print(cor_texto(f"{nome} é um herói com {xp} de experiência.\n", "verde"))

    # Pergunta ao usuário se deseja continuar
    continuar = input(
        cor_texto("Deseja adicionar outro herói? (s/n): ", "azul")
    ).lower()

    if continuar != "s":
        efeito_digitar("Encerrando o programa... Obrigado por jogar!", 0.06)
        break
