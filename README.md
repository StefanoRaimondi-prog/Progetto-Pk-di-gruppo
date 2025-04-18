# Analisi Dati Pokémon

Uno script Python per analizzare le statistiche dei Pokémon da un database e identificare quelli con valori massimi, minimi e statistiche specifiche.

## Descrizione

Questa applicazione si connette a un database Pokémon ed esegue varie analisi sulle statistiche dei Pokémon, tra cui altezza, peso, esperienza di base e statistiche di combattimento (HP, Attacco, Difesa, Attacco Speciale, Difesa Speciale e Velocità). Identifica e visualizza i Pokémon con valori massimi e minimi per ogni attributo, nonché i Pokémon con valori statistici superiori o inferiori a soglie specificate dall'utente.

## Requisiti

- Python 3.x
- NumPy
- Modulo database personalizzato (`Db.py`)
- Un database Pokémon configurato correttamente

## Struttura del Database

Lo script richiede un database con almeno le seguenti tabelle:
- `pokemon`: Contiene informazioni di base sui Pokémon (id, name, height, weight, base_experience)
- `base_stats`: Contiene statistiche di combattimento (pokemon_id, hp, attack, defense, special_attack, special_defense, speed)

## Funzionalità

- **Analisi dei Valori Massimi**: Identifica i Pokémon con il valore più alto per ogni attributo
- **Analisi dei Valori Minimi**: Identifica i Pokémon con il valore più basso per ogni attributo
- **Confronto con Soglie**: Elenca i Pokémon con valori di HP, Attacco o Difesa maggiori o minori di una soglia specificata dall'utente

## Utilizzo

1. Assicurarsi che il modulo di connessione al database (`Db.py`) sia configurato correttamente
2. Eseguire lo script:
   ```
   TestMaxMinValori.py
   ```
3. Quando richiesto, inserire i valori di soglia per trovare Pokémon con statistiche superiori o inferiori a tali valori

## Esempio di Output

```
Pokémon con valori MASSIMI:
Altezza → [nome Pokémon] (valore)
Peso → [nome Pokémon] (valore)
Esperienza → [nome Pokémon] (valore)
HP → [nome Pokémon] (valore)
...

Pokémon con valori MINIMI:
Altezza → [nome Pokémon] (valore)
Peso → [nome Pokémon] (valore)
...

Inserisci un numero per confrontare HP, ATTACK e DEFENSE. Valore maggiore di: [input utente]

Pokémon con valori MAGGIORI di [valore]

HP > [valore]:
 - [nome Pokémon] → HP = [valore]
 - [nome Pokémon] → HP = [valore]
...
```

## Note

- Lo script utilizza NumPy per una gestione e analisi efficiente dei dati
- Tutte le connessioni al database vengono chiuse correttamente dopo l'uso
- La validazione dell'input non è implementata e potrebbe causare errori se vengono inseriti valori non numerici
