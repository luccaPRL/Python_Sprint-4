# PROJETO GLOBAL SOLUTION
# Integrantes:
# Lucca Pereira Locambo De Oliveira - RM:560731
# Diego Garcia Tosta - RM:556724
# Joud Jihad Jaber - RM:556482

import random

# Aqui mostramos a previsão de chuva e o nível de risco
def ver_previsao_e_risco():
    print("\n=== PREVISÃO DE CHUVA E NÍVEL DE RISCO ===")
    opcoes = ["0%", "30%", "45%", "55%", "65%", "78%", "85%", "92%", "100%"]
    chuva_aleatoria = random.choice(opcoes)
    print("Previsão atual de chuva:", chuva_aleatoria)

    # Aqui funciona a lógica para determinar o nível de risco
    try:
        percentual = int(chuva_aleatoria.replace('%', '').strip())
        if percentual >= 80:
            print("🔴 RISCO ALTO")
        elif percentual >= 50:
            print("🟠 RISCO MÉDIO")
        else:
            print("🟢 RISCO BAIXO")
    except ValueError:
        print("Erro ao processar a previsão de chuva.")

# Aqui mostramos os locais de risco
def locais_de_risco():
    print("\n=== LOCAIS DE RISCO ===")
    todos_locais = ["AV. Paulista", "Itaim Bibi", "Vila Madalena", "Pinheiros", "Liberdade", "Bela Vista"]
    locais_com_risco = random.sample(todos_locais, k=3)
    print("Locais com maior risco de enchentes:")
    for local in locais_com_risco:
        print("- " + local)
    return locais_com_risco

# Aqui mostramos as rotas de segurança que funcuionam de acordo com os locais de risco
def rotas_de_seguranca(locais_com_risco):
    print("\n=== ROTAS DE SEGURANÇA ===")
    rotas = {
        "AV. Paulista": "Siga pela Rua Augusta até o abrigo municipal.",
        "Itaim Bibi": "Siga pela Avenida Faria Lima até o centro comunitário.",
        "Vila Madalena": "Siga pela Rua Harmonia até a escola pública.",
        "Pinheiros": "Siga pela Avenida Rebouças até o hospital local.",
        "Liberdade": "Siga pela Rua Galvão Bueno até o templo comunitário.",
        "Bela Vista": "Siga pela Avenida Brigadeiro Luís Antônio até o ponto de apoio."
    }
    for local in locais_com_risco:
        if local in rotas:
            print(f"{local}: {rotas[local]}")

# Aqui mostramos as instruções de emergência
def instrucoes_emergencia():
    print("\n=== INSTRUÇÕES DE EMERGÊNCIA ===")
    instrucoes = [
        "Verifique o sistema de drenagem da sua casa.",
        "Evite entulhos que possam obstruir bueiros.",
        "Tenha um kit de emergência com água, alimentos e medicamentos.",
        "Mantenha a caixa d'água cheia.",
        "Tenha um plano de evacuação familiar."
        "Fique atento às sirenes e avisos da Defesa Civil.",
        "Evite áreas alagadas e não tente atravessar ruas inundadas.",        
    ]
    for item in instrucoes:
        print(item)

# Aqui mostramos os contatos de emergência
def contatos_emergencia():
    print("\n=== CONTATOS DE EMERGÊNCIA ===")
    contatos = {
        "Bombeiros": "193",
        "Defesa Civil": "199",
        "Polícia": "190",
        "SAMU": "192"
    }
    for servico, numero in contatos.items():
        print(f"{servico}: {numero}")

# Aqui criamos o menu principal do programa
def menu():
    locais_com_risco = []
    while True:
        print("\n=== INFORMAÇÕES DE ENCHENTES ===")
        print("1. Previsão de chuva e nível de risco")
        print("2. Locais de risco")
        print("3. Rotas de segurança")
        print("4. Instruções de emergência")
        print("5. Contatos de emergência")
        print("6. Sair")
        print("===================================")

        escolha = input("Escolha uma opção (1-6): ")

        if escolha == "1":
            ver_previsao_e_risco()
        elif escolha == "2":
            locais_com_risco = locais_de_risco()
        elif escolha == "3":
            if locais_com_risco:
                rotas_de_seguranca(locais_com_risco)
            else:
                print("Primeiro, veja os locais de risco (opção 2).")
        elif escolha == "4":
            instrucoes_emergencia()
        elif escolha == "5":
            contatos_emergencia()
        elif escolha == "6":
            print("Saindo do programa. Fique seguro!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciamos o programa
menu()