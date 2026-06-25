#importantes para o jogo.
# --- Estado do Jogador ---
inventario_fotos = [] # Lista onde guardaremos as fotos tiradas
conquistas_completadas = [] # Lista para não ganhar a mesma recompensa duas vezes
snowball_fight_wins = 0 # Contador para a conquista Guerreiro de Neve
# Define a estação atual do jogo
current_season = "primavera" # Pode ser "primavera", "verao", "outono", "inverno"

# Dicionário de itens por estação
seasons_items = {
    "primavera": ["sakura", "rosa", "lirio"],
    "verao": ["girassol", "concha", "sorvete", "manga", "abacaxi", "banana"],
    "outono": ["folha seca", "abobora", "castanha", "abobora_desenhada", "folha_amarela", "folha_laranja", "folha_vermelha"], # Added new autumn items
    "inverno": [
        "boneco de neve", "cenoura_nariz", "carvao_olhos", "cachecol", # Para Esculpidor de Neve
        "chocolate_quente_tradicional", "chocolate_quente_com_marshmallow", "chocolate_quente_com_canela" # Para Aquecedor
    ]
}

# --- Funções do Sistema ---
def tirar_foto(item):
    if item not in inventario_fotos:
        inventario_fotos.append(item)
        print(f"Foto de '{item}' adicionada ao inventário!")
        verificar_conquistas()
    else:
        print(f"Você já tem uma foto de '{item}'.")

def ganhar_luta_neve():
    global snowball_fight_wins
    snowball_fight_wins += 1
    print(f"Você ganhou uma guerra de bolas de neve! Total de vitórias: {snowball_fight_wins}")
    verificar_conquistas()

def verificar_conquistas():
    global conquistas_completadas, snowball_fight_wins

    # 1. Conquista: Bênção das Flores (Primavera)
    if all(flower in inventario_fotos for flower in seasons_items["primavera"]):
        if "bênção das flores" not in conquistas_completadas:
            print("\n*** CONQUISTA DESBLOQUEADA: Bênção das Flores! ***")
            print("Recompensa: As pessoas se tornam mais tranquilas pelo seu aroma.")
            conquistas_completadas.append("bênção das flores")

    # 2. Conquista: Doce como o mel
    if inventario_fotos.count("colmeia") >= 3:
        if "doce como o mel" not in conquistas_completadas:
            print("\n*** CONQUISTA DESBLOQUEADA: Doce como o mel! ***")
            print("Recompensa: Seus vegetais têm 30% de chance de qualidade máxima.")
            conquistas_completadas.append("doce como o mel")

    # 3. Conquista: Tesouros do Verão (Verão)
    if all(item in inventario_fotos for item in seasons_items["verao"]):
        if "tesouros do verao" not in conquistas_completadas:
            print("\n*** CONQUISTA DESBLOQUEADA: Tesouros do Verão! ***")
            print("Recompensa: Você encontra itens raros com mais frequência.")
            conquistas_completadas.append("tesouros do verao")

    # 4. Conquista: Noite Estrelada de Verão (Vagalumes)
    if "vagalumes" in inventario_fotos:
        if "noite estrelada de verao" not in conquistas_completadas:
            print("\n*** CONQUISTA DESBLOQUEADA: Noite Estrelada de Verão! ***")
            print("Recompensa: Aumento de sorte ao pescar a noite.")
            conquistas_completadas.append("noite estrelada de verao")

    # 5. Conquista: Mestre do Festival de Verão
    if "trofeu_festival_verao" in inventario_fotos:
        if "mestre do festival de verao" not in conquistas_completadas:
            print("\n*** CONQUISTA DESBLOQUEADA: Mestre do Festival de Verão! ***")
            print("Recompensa: Descontos especiais na loja do festival no próximo ano.")
            conquistas_completadas.append("mestre do festival de verao")

    # 6. Conquista: Colheita de Outono (Outono) - Updated to include new items
    if all(item in inventario_fotos for item in seasons_items["outono"]):
        if "colheita de outono" not in conquistas_completadas:
            print("\n*** CONQUISTA DESBLOQUEADA: Colheita de Outono! ***")
            print("Recompensa: Sua energia é restaurada mais rapidamente.")
            conquistas_completadas.append("colheita de outono")

    # 7. Conquista: Fotógrafo da Vida Selvagem (Esquilo)
    if "esquilo_bochechudo" in inventario_fotos:
        if "fotografo da vida selvagem" not in conquistas_completadas:
            print("\n*** CONQUISTA DESBLOQUEADA: Fotógrafo da Vida Selvagem! ***")
            print("Recompensa: Aumenta a chance de encontrar sementes raras.")
            conquistas_completadas.append("fotografo da vida selvagem")

    # 8. Conquista: Esculpidor de Neve (Inverno) - Nova Condição
    snowman_parts = ["boneco de neve", "cenoura_nariz", "carvao_olhos", "cachecol"]
    if all(part in inventario_fotos for part in snowman_parts):
        if "esculpidor de neve" not in conquistas_completadas:
            print("\n*** CONQUISTA DESBLOQUEADA: Esculpidor de Neve! ***")
            print("Recompensa: Produtos ganham promoção de 30%.")
            conquistas_completadas.append("esculpidor de neve")

    # 9. Conquista: Guerreiro de Neve (Inverno) - Nova Conquista
    if snowball_fight_wins >= 5:
        if "guerreiro de neve" not in conquistas_completadas:
            print("\n*** CONQUISTA DESBLOQUEADA: Guerreiro de Neve! ***")
            print("Recompensa: Você dá um dano de 20% a mais.")
            conquistas_completadas.append("guerreiro de neve")

    # 10. Conquista: Aquecedor (Inverno) - Nova Conquista
    hot_chocolate_types = ["chocolate_quente_tradicional", "chocolate_quente_com_marshmallow", "chocolate_quente_com_canela"]
    if all(choc in inventario_fotos for choc in hot_chocolate_types):
        if "aquecedor" not in conquistas_completadas:
            print("\n*** CONQUISTA DESBLOQUEADA: Aquecedor! ***")
            print("Recompensa: O incômodo do frio é diminuído em 30%.") # Generic reward
            conquistas_completadas.append("aquecedor")


# --- Simulação de Jogo ---
print("--- Simulando o jogo ---")

print("\n--- Tentando desbloquear Bênção das Flores (Primavera) ---")
tirar_foto("sakura")
tirar_foto("rosa")
tirar_foto("lirio") # Aqui deve desbloquear a primeira conquista

print("\n--- Tentando desbloquear Doce como o mel ---")
tirar_foto("colmeia")
tirar_foto("colmeia")
tirar_foto("colmeia") # Aqui deve desbloquear a segunda conquista

print("\n--- Mudando para o Verão e tentando desbloquear Tesouros do Verão, Noite Estrelada e Mestre do Festival ---")
current_season = "verao"
# Items for Tesouros do Verão
tirar_foto("girassol")
tirar_foto("concha")
tirar_foto("sorvete")
tirar_foto("manga")
tirar_foto("abacaxi")
tirar_foto("banana") # Should unlock Tesouros do Verão here

# Item for Noite Estrelada de Verão
tirar_foto("vagalumes") # Should unlock Noite Estrelada de Verão here

# Item for Mestre do Festival de Verão
tirar_foto("trofeu_festival_verao") # Should unlock Mestre do Festival de Verão here

print("\n--- Mudando para o Outono e tentando desbloquear Colheita de Outono e Fotógrafo da Vida Selvagem ---")
current_season = "outono"
tirar_foto("folha seca")
tirar_foto("abobora")
tirar_foto("castanha")
tirar_foto("abobora_desenhada") # New item for carving pumpkins
tirar_foto("folha_amarela") # New leaf color
tirar_foto("folha_laranja") # New leaf color
tirar_foto("folha_vermelha") # New leaf color (Should unlock Colheita de Outono here)

tirar_foto("esquilo_bochechudo") # New item for squirrel photo (Should unlock Fotógrafo da Vida Selvagem here)

print("\n--- Mudando para o Inverno e tentando desbloquear conquistas de Inverno ---")
current_season = "inverno"

# Tentando desbloquear Esculpidor de Neve
tirar_foto("boneco de neve")
tirar_foto("cenoura_nariz")
tirar_foto("carvao_olhos")
tirar_foto("cachecol") # Deve desbloquear Esculpidor de Neve aqui

# Tentando desbloquear Guerreiro de Neve
for _ in range(5):
    ganhar_luta_neve() # Deve desbloquear Guerreiro de Neve aqui

# Tentando desbloquear Aquecedor
tirar_foto("chocolate_quente_tradicional")
tirar_foto("chocolate_quente_com_marshmallow")
tirar_foto("chocolate_quente_com_canela") # Deve desbloquear Aquecedor aqui

print("\n--- Estado Final do Jogador ---")
print(f"Fotos no inventário: {inventario_fotos}")
print(f"Conquistas completadas: {conquistas_completadas}")
print(f"Vitórias em guerras de neve: {snowball_fight_wins}")

# Exemplo de como a recompensa pode ser usada (já existia)
chance_qualidade_maxima = 0.0
if "doce como o mel" in conquistas_completadas:
    chance_qualidade_maxima = 0.30
print(f"Chance de qualidade máxima de vegetais: {chance_qualidade_maxima*100}%")

promotion_chance = 0.0
if "esculpidor de neve" in conquistas_completadas:
    promotion_chance = 0.30
print(f"Chance de promoção de produtos: {promotion_chance*100}%")

damage_bonus = 0.0
if "guerreiro de neve" in conquistas_completadas:
    damage_bonus = 0.20
print(f"Bônus de dano: {damage_bonus*100}%")
