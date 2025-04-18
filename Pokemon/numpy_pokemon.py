import mysql.connector  # Per connettersi al database MySQL
import numpy as np      # Per analisi numerica con array

# Funzione che restituisce una connessione al database
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Zanetti44C!",    # Cambialo se necessario
        database="pokemon_db"      # Nome del database
    )

# Funzione principale che analizza i dati dei Pokémon
def analizza_pokemon():
    conn = get_connection()                      # Connessione al database
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
    print("\n📈 Pokémon con valori MASSIMI:")
    for i in range(len(attributi)):
        indice_max = np.argmax(dati[:, i])  # Trova l'indice del valore massimo nella colonna i
        print(f"{attributi[i]} → {nomi[indice_max]} ({dati[indice_max, i]})")

    # Stampa dei Pokémon con valore minimo per ogni attributo
    print("\n📉 Pokémon con valori MINIMI:")
    for i in range(len(attributi)):
        indice_min = np.argmin(dati[:, i])  # Trova l'indice del valore minimo nella colonna i
        print(f"{attributi[i]} → {nomi[indice_min]} ({dati[indice_min, i]})")

    # Chiude connessione e cursore
    cursor.close()
    conn.close()

# Esecuzione della funzione
analizza_pokemon()



# Connessione al database
conn = get_connection("pokemon.db")
cursor = conn.cursor()

# Esegui una query per ottenere nome, hp, attacco e difesa dei Pokémon
cursor.execute('''
    SELECT p.name, bs.hp, bs.attack, bs.defense
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

# Chiediamo all’utente un numero di confronto
n = int(input("Inserisci un numero per confrontare HP, ATTACK e DEFENSE: "))

# Nomi degli attributi, nello stesso ordine dei dati
attributi = ["HP", "ATTACK", "DEFENSE"]

# Stampiamo i Pokémon con valori MAGGIORI di n
print("\n📈 Pokémon con valori MAGGIORI di", n)
for i in range(3):  # Per ogni colonna: hp, attacco, difesa
    print(f"\n{attributi[i]} > {n}:")
    for j in range(len(nomi)):  # Per ogni Pokémon
        if dati[j][i] > n:
            print(f" - {nomi[j]} → {attributi[i]} = {dati[j][i]}")


n = int(input("Inserisci un numero per confrontare HP, ATTACK e DEFENSE: "))
# Stampiamo i Pokémon con valori MINORI di n
print("\n Pokémon con valori MINORI di", n)
for i in range(3):  # Per ogni colonna: hp, attacco, difesa
    print(f"\n{attributi[i]} < {n}:")
    for j in range(len(nomi)):  # Per ogni Pokémon
        if dati[j][i] < n:
            print(f" - {nomi[j]} → {attributi[i]} = {dati[j][i]}")
