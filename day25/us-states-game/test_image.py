# test_image.py
import turtle

print("Iniciando o teste do Turtle...")

try:
    screen = turtle.Screen()
    screen.title("Teste de Diagnóstico do Turtle")

    # --- PASSO 1: Teste de Cor ---
    # Vamos tentar definir uma cor de fundo sólida.
    # Se uma tela azul aparecer, significa que a renderização básica do Turtle está funcionando.
    print("Passo 1: Tentando definir a cor de fundo para 'blue'.")
    screen.bgcolor("blue")

    # --- PASSO 2: Teste de Imagem ---
    # Agora, tentamos carregar a imagem usando o caminho absoluto.
    image_path = "/media/braulio/Projeto/100days/day25/us-states-game/blank_states_img.gif"
    print(f"Passo 2: Tentando carregar a imagem de: {image_path}")
    screen.bgpic(image_path)
    print("-> A função bgpic() foi chamada sem gerar uma exceção.")

    print("\nTeste concluído. Mantendo a janela aberta...")
    turtle.mainloop()

except Exception as e:
    print("\n--- ERRO CRÍTICO ---")
    print(f"Uma exceção ocorreu durante a configuração do Turtle: {e}")
    # Adicionamos um input para que a janela de terminal não feche imediatamente.
    input("Pressione Enter para fechar.")

