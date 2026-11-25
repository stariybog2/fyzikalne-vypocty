Fyzikálne výpočty

Jednoduchá aplikácia v Pythone na výpočet mechanického výkonu podľa vzorca P = W / t. Práca W sa zadáva v jouloch (J), čas t v sekundách (s) a výsledok je vo wattoch (W).

Funkcie

- Vygeneruje a zoradí 50 náhodných hodnôt práce.
- Zobrazí priemer, minimum a maximum.
- V jednom grafe zobrazí hodnoty práce a vypočítaného výkonu.
- Umožní zadať vlastnú prácu a čas. Čas musí byť väčší ako nula.

Spustenie vo Windows

Potrebný je Python s Tkinterom. Na vykreslenie grafu sa používa knižnica Matplotlib.

    python -m pip install matplotlib
    python fyzikalne_vypocty.py

Príklad: pri práci 1500 J a čase 30 s je výkon 50 W.

Vytvorenie súboru EXE

    python -m pip install pyinstaller
    python -m PyInstaller --onefile --windowed --name FyzikalneVypocty fyzikalne_vypocty.py

Výsledný súbor sa nachádza v dist\FyzikalneVypocty.exe.

Verzie

v1.0.0. Prvá verzia aplikácie s výpočtom výkonu, štatistikou a grafom.

Autor: Artem Siliakov
