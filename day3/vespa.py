print('''
                                       _
                                    ,-~ |
       ________________          o==]___|
      |                |            \ \
      |________________|            /\ \
 __  /  _,-----._      )           |  \ \.
|_||/_-~         `.   /()          |  /|]_|_____
  |//              \ |              \/ /_-~     ~-_
  //________________||              / //___________\
 //__|______________| \____________/ //___/-\ \~-_
((_________________/_-o___________/_//___/  /\,\  \
 |__/(  ((====)o===--~~                 (  ( (o/)  )
      \  ``==' /                         \  `--'  /
       `-.__,-'       Vespa P-200 E       `-.__,-
''')

print("Bem vindo ao jogo da Vespa!")
print("Sua missão é encontrar a Vespa.")
direcao = input("Você está na encruzilhada. Para onde você quer ir? Digite 'esquerda' ou 'direita': ").lower()
if direcao == "esquerda":
    acao = input("Você chegou a um lago. Digite 'esperar' para esperar por um barco ou 'nadar' para nadar até a ilha: ").lower()
    if acao == "esperar":
        porta = input("Você chegou à ilha. Há uma casa com 3 portas: uma vermelha, uma amarela e uma azul. Qual você escolhe? ").lower()
        if porta == "amarela":
            print("Você encontrou a Vespa! Parabéns!")
        elif porta == "vermelha":
            print("Você entrou em uma sala cheia de fogo. Game Over.")
        elif porta == "azul":
            print("Você entrou em uma sala cheia de feras. Game Over.")
        else:
            print("Essa porta não existe. Game Over.")
    else:
        print("Você foi atacado por peixes. Game Over.")
else:
    print("Você caiu em um buraco. Game Over.")

