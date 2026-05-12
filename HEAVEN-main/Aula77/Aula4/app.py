# --- ESTUDO DE LAÇOS (FOR) - VERSÃO BLUE LOCK ---

# O laço for é finito: ideal para quando sabemos o número de repetições.
jogadores_blue_lock = ['Isagi', 'Bachira', 'Chigiri', 'Kunigami']

# Exemplo simples de iteração
for craque in jogadores_blue_lock:
    # print(craque[0])  # Isso imprimiria apenas a primeira letra de cada nome
    print(f"Atacante: {craque}")

print("-" * 30)

# for range (inicio, fim, salto)
# Útil para repetições numéricas ou gerar sequências
for i in range(1, 6, 1):
    print(f"Treino de finalização número {i}!")

print("-" * 30)

# Tabuada do Egoísta (Treinando o cálculo da trajetória do chute)
num = int(input("Digite o número para calcular o ângulo do chute (Tabuada): "))
for i in range(11):
    print(f"{i} x {num} = {i * num}")

print("-" * 30)

# Lista completa com os Mestres Mundiais e New Gens
lista_nomes = [
    'Noel Noa', 'Chris Prince', 'Marc Snuffy', 'Lavinho', 'Julian Loki',
    'Michael Kaiser', 'Sae Itoshi', 'Don Lorenzo', 'Isagi Yoichi', 
    'Rin Itoshi', 'Ryusei Shidou', 'Shoei Barou'
]

# Usando enumerate para criar um Ranking
print("--- RANKING MUNDIAL BLUE LOCK ---")
for i, nome in enumerate(lista_nomes):
    print(f"{i+1}º Lugar: {nome}")

print("-" * 30)

# Busca de jogador com a reação "Egoísta"
nome_buscar = input("Digite o nome de um jogador para buscar: ").title()

# Mantendo o espírito do seu código original (uma reação exagerada para um personagem específico)
if 'Ryusei Shidou' in lista_nomes:
    print("\n[AVISO DO SISTEMA]: O MEU GENE ESTÁ PULSANDO! ESSA É A EXPLOSÃO BIOLÓGICA QUE O CAMPO PRECISAVA!!")
    print("O QUE VOCÊ QUER DIZER COM 'O GOL É O MEU ÚNICO PRAZER'?!")

elif nome_buscar in lista_nomes:
    print(f"O jogador {nome_buscar} foi detectado pelo Blue Lock. Nível de Ego: Máximo.")
else:
    print(f"{nome_buscar} não foi encontrado. Provavelmente foi eliminado do projeto.")

print("i am atomic")