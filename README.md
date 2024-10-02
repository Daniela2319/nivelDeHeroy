# Sistema de Categorias de Heróis 🛸
Este é um simples programa de Python que permite ao usuário inserir o nome e o XP (experiência) de um herói e, com base no valor do XP, determina a categoria desse herói. O programa usa animações simples de texto e cores para tornar a interação mais dinâmica e divertida.

## Funcionalidades 
* Entrada de dados: O usuário pode inserir o nome e o XP de seu herói.
* Avaliação de Categoria: O programa determina a categoria do herói com base no valor do XP.
* Cores e Animação: O texto é colorido e exibido com efeitos de digitação para uma experiência mais visual e imersiva.
* Validação de entrada: O programa verifica se o XP inserido é um número inteiro, evitando erros.
* Interatividade contínua: O programa permite inserir vários heróis em um loop, até que o usuário deseje encerrar.

## Categorias de Heróis
As categorias são determinadas com base na pontuação de XP do herói:

* Ferro: XP menor que 1000
* Bronze: XP entre 1001 e 2000
* Prata: XP entre 2001 e 5000
* Ouro: XP entre 5001 e 7000
* Platina: XP entre 7001 e 8000
* Ascendente: XP entre 8001 e 9000
* Imortal: XP entre 9001 e 10000
* Radiante: XP maior que 10001
  
### Pré-requisitos
Antes de executar o código, você precisa:

* Ter o Python instalado na versão 3.6 ou superior.
* O módulo time e o módulo sys são usados, que já vêm com a instalação padrão do Python.
  
## Como Executar
* Clone este repositório ou copie o código em seu ambiente de desenvolvimento.

* Execute o programa: Abra o terminal e navegue até o diretório onde o arquivo está localizado e digite:

`python nome_do_arquivo.py`

### Siga as instruções:

* O programa irá pedir o nome do herói e o valor do XP.
* Após a avaliação, a categoria do herói será exibida com um efeito de digitação e cores.
* O programa perguntará se você deseja adicionar outro herói. Digite 's' para continuar ou 'n' para encerrar.
  
### Exemplo de Execução
Aqui está um exemplo de como o programa funciona no terminal:
```sh
Bem-vindo ao sistema de categorias de Heróis!

Coloque o nome do seu Herói: SuperMan
Qual valor do XP do seu Herói (número inteiro): 8500
Avaliando o herói SuperMan...

Herói SuperMan pertence à categoria: Ascendente!
SuperMan é um herói com 8500 de experiência.

Deseja adicionar outro herói? (s/n): n
Encerrando o programa... Obrigado por jogar!
```
## Explicação do Código
* Entrada de Dados: O programa começa pedindo o nome do herói e o valor do XP.
* O XP deve ser um número inteiro, e o código valida isso usando um loop while para garantir que o valor inserido seja válido.

```sh
nome = input("Coloque o nome do seu Herói: ")
while True:
    try:
        xp = int(input("Qual valor do XP do seu Herói (número inteiro): "))
        break
    except ValueError:
        print("XP inválido! Por favor, insira um número inteiro.")
```
**Classificação de Categorias**: O programa então compara o valor de XP com os intervalos definidos e atribui uma categoria ao herói, exibindo a categoria em cores. 
Para isso, usamos uma função cor_texto que aplica códigos ANSI para colorir a saída no terminal.

```sh
if xp < 1000:
    categoria = cor_texto("Ferro", "ciano")
elif 1001 <= xp < 2000:
    categoria = cor_texto("Bronze", "amarelo")
```
    
**Exibição Dinâmica**: Para impressionar o usuário, criamos uma função efeito_digitar que simula uma digitação lenta, exibindo os textos com pequenas pausas.
```sh
def efeito_digitar(texto, delay=0.05):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Quebra de linha após a exibição do texto
```
**Repetição**: O programa permite que o usuário continue inserindo novos heróis até que ele escolha parar, utilizando um loop while.
```sh
continuar = input("Deseja adicionar outro herói? (s/n): ").lower()
if continuar != 's':
    print("Encerrando o programa.")
    break
```

## Conclusão
 Esse programa mostra como entrada de dados, condicionais e loops, com recursos mais avançados, como animação de texto e cores no terminal.
