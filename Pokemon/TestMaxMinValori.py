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