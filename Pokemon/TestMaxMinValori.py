import Db as db
import numpy as np  


# Funzione principale che analizza i dati dei Pokémon
def analizza_pokemon():
    conn = db.get_connection() # Connessione al database
    cursor = conn.cursor(dictionary=True)        # Cursor che restituisce righe come dizionari

    # Query che unisce le tabelle 'pokemon' e 'base_stats'
    query = """
    SELECT p.name, p.height, p.weight, p.base_experience,
           b.hp, b.attack, b.defense, b.special_attack, b.special_defense, b.speed
    FROM pokemon p
    JOIN base_stats b ON p.id = b.pokemon_id
    """
    cursor.execute(query)             # Esegue la query
    risultati = cursor.fetchall()     # Ottiene tutti i risultati come lista di dizionari

    # Se non ci sono risultati, termina la funzione
    if not risultati:
        print("Nessun Pokémon trovato.")
        return

    # Lista dei nomi dei Pokémon
    nomi = [row['name'] for row in risultati]

    # Array 2D con i valori numerici per ogni Pokémon
    # Ogni riga rappresenta un Pokémon
    # Ogni colonna rappresenta un attributo
    dati = np.array([
        [
            row['height'],
            row['weight'],
            row['base_experience'],
            row['hp'],
            row['attack'],
            row['defense'],
            row['special_attack'],
            row['special_defense'],
            row['speed']
        ]
        for row in risultati
    ])

    # Etichette per ogni colonna (attributo)
    attributi = [
        "Altezza", "Peso", "Esperienza", "HP",
        "Attacco", "Difesa", "Attacco Speciale", "Difesa Speciale", "Velocità"
    ]

    # Stampa dei Pokémon con valore massimo per ogni attributo
    print("\nPokémon con valori MASSIMI:")
    for i in range(len(attributi)):
        indice_max = np.argmax(dati[:, i])  # Trova l'indice del valore massimo nella colonna i
        print(f"{attributi[i]} → {nomi[indice_max]} ({dati[indice_max, i]})")

    # Stampa dei Pokémon con valore minimo per ogni attributo
    print("\nPokémon con valori MINIMI:")
    for i in range(len(attributi)):
        indice_min = np.argmin(dati[:, i])  # Trova l'indice del valore minimo nella colonna i
        print(f"{attributi[i]} → {nomi[indice_min]} ({dati[indice_min, i]})")

    # Chiude connessione e cursore
    cursor.close()
    conn.close()

# Esecuzione della funzione
analizza_pokemon()

# Connessione al database
conn = db.get_connection()

cursor = conn.cursor()

# Esegui una query per ottenere nome, hp, attacco e difesa dei Pokémon
cursor.execute('''
    SELECT DISTINCT p.name, bs.hp, bs.attack, bs.defense
    FROM pokemon p
    JOIN base_stats bs ON p.id = bs.pokemon_id
''')
# Ottieni tutti i risultati
risultati = cursor.fetchall()

# Se non ci sono dati, interrompi
if not risultati:
    print("Nessun Pokémon trovato.")
    exit()

# Separiamo i nomi e i dati numerici
nomi = [r[0] for r in risultati]                  # Solo i nomi
dati = np.array([r[1:] for r in risultati])       # Solo hp, attack, defense

# Nomi degli attributi, nello stesso ordine dei dati
attributi = ["HP", "ATTACK", "DEFENSE"]

# Chiediamo all'utente cosa vuole fare
scelta = input("Vuoi cercare Pokémon con valori maggiori o minori di un numero? (1/2): ")

if scelta == "1":
    # Chiediamo all'utente un numero di confronto
    n = int(input("Inserisci un numero per confrontare HP, ATTACK e DEFENSE. Valore maggiore di: "))
    
    # Stampiamo i Pokémon con valori MAGGIORI di n
    print(f"\nPokémon con valori MAGGIORI di {n}")
    for i in range(3):  # Per ogni colonna: hp, attacco, difesa
        print(f"\n{attributi[i]} > {n}:")
        trovati = False
        for j in range(len(nomi)):  # Per ogni Pokémon
            if dati[j][i] > n:
                print(f" - {nomi[j]} → {attributi[i]} = {dati[j][i]}")
                trovati = True
        if not trovati:
            print(f"  Nessun Pokémon ha {attributi[i]} maggiore di {n}")

elif scelta == "2":
    # Chiediamo all'utente un numero di confronto
    n = int(input("Inserisci un numero per confrontare HP, ATTACK e DEFENSE. Valore minore di: "))
    
    # Stampiamo i Pokémon con valori MINORI di n
    print(f"\nPokémon con valori MINORI di {n}")
    for i in range(3):  # Per ogni colonna: hp, attacco, difesa
        print(f"\n{attributi[i]} < {n}:")
        trovati = False
        for j in range(len(nomi)):  # Per ogni Pokémon
            if dati[j][i] < n:
                print(f" - {nomi[j]} → {attributi[i]} = {dati[j][i]}")
                trovati = True
        if not trovati:
            print(f"  Nessun Pokémon ha {attributi[i]} minore di {n}")

else:
    print("Scelta non valida. Inserisci 'maggiori' o 'minori'.")

# Chiudere connessione e cursore
cursor.close()
conn.close()
# # Ottieni tutti i risultati
# risultati = cursor.fetchall()

# # Se non ci sono dati, interrompi
# if not risultati:
#     print("Nessun Pokémon trovato.")
#     exit()

# # Separiamo i nomi e i dati numerici
# nomi = [r[0] for r in risultati]                  # Solo i nomi
# dati = np.array([r[1:] for r in risultati])# Solo hp, attack, defense

# # Chiediamo all’utente un numero di confronto
# n = int(input("Inserisci un numero per confrontare HP, ATTACK e DEFENSE. Valore maggiore di: "))

# # Nomi degli attributi, nello stesso ordine dei dati
# attributi = ["HP", "ATTACK", "DEFENSE"]

# # Stampiamo i Pokémon con valori MAGGIORI di n
# print("\nPokémon con valori MAGGIORI di", n)
# for i in range(3):  # Per ogni colonna: hp, attacco, difesa
#     print(f"\n{attributi[i]} > {n}:")
#     for j in range(len(nomi)):  # Per ogni Pokémon
#         if dati[j][i] > n:
#             print(f" - {nomi[j]} → {attributi[i]} = {dati[j][i]}")


# n = int(input("Inserisci un numero per confrontare HP, ATTACK e DEFENSE. Valore minore di: "))
# # Stampiamo i Pokémon con valori MINORI di n
# print("\nPokémon con valori MINORI di", n)
# for i in range(3):  # Per ogni colonna: hp, attacco, difesa
#     print(f"\n{attributi[i]} < {n}:")
#     for j in range(len(nomi)):  # Per ogni Pokémon
#         if dati[j][i] < n:
#             print(f" - {nomi[j]} → {attributi[i]} = {dati[j][i]}")