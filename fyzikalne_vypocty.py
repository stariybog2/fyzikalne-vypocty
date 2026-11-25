import math
import random
import tkinter as tk
from statistics import mean
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def vypocitaj_vykon(praca, cas):
    return praca / cas


def main():
    prace = sorted(random.randint(50, 500) for _ in range(50))

    okno = tk.Tk()
    okno.title("Výpočet výkonu")
    okno.geometry("900x670")
    okno.minsize(630, 520)

    ram = ttk.Frame(okno, padding=18)
    ram.pack(fill="both", expand=True)

    ttk.Label(ram, text="Výpočet výkonu", font=("Segoe UI", 20)).pack(anchor="w")
    ttk.Label(ram, text="P = W / t  ·  výkon = práca / čas").pack(anchor="w", pady=(4, 12))

    statistika = (
        f"Práca ({len(prace)} hodnôt)  ·  Priemer: {mean(prace):.2f} J"
        f"  ·  Minimum: {min(prace)} J  ·  Maximum: {max(prace)} J"
    )
    ttk.Label(ram, text=statistika, wraplength=590).pack(anchor="w")

    fig = Figure(figsize=(8, 4), dpi=100, layout="constrained")
    graf = fig.add_subplot()
    platno = FigureCanvasTkAgg(fig, master=ram)
    platno.get_tk_widget().pack(side="top", fill="both", expand=True, pady=12)

    formular = ttk.Frame(ram)
    formular.pack(fill="x")
    formular.columnconfigure(0, weight=1)
    formular.columnconfigure(1, weight=1)

    ttk.Label(formular, text="Práca W (J)").grid(row=0, column=0, sticky="w")
    ttk.Label(formular, text="Čas t (s)").grid(row=0, column=1, sticky="w")
    vstup_praca = ttk.Entry(formular)
    vstup_praca.grid(row=1, column=0, sticky="ew", padx=(0, 12))
    vstup_cas = ttk.Entry(formular)
    vstup_cas.grid(row=1, column=1, sticky="ew", padx=(0, 12))
    vstup_cas.insert(0, "5")

    sprava = tk.StringVar(value="Zadajte prácu a čas.")
    ttk.Label(ram, textvariable=sprava, wraplength=590).pack(anchor="w", pady=(10, 0))

    def vykresli(cas):
        vykony = [vypocitaj_vykon(praca, cas) for praca in prace]
        poradie = range(1, len(prace) + 1)
        graf.clear()
        graf.plot(poradie, prace, color="#1857c9", label="Práca (J)", linewidth=2)
        graf.plot(poradie, vykony, color="#a84b12", label="Výkon (W)", linewidth=2)
        graf.set_title(f"Práca a výkon pri čase {cas:g} s")
        graf.set_xlabel("Poradie podľa veľkosti práce")
        graf.set_ylabel("Číselná hodnota")
        graf.grid(alpha=0.25)
        graf.legend()
        platno.draw_idle()

    def vypocitaj(event=None):
        try:
            praca = float(vstup_praca.get().replace(",", "."))
            cas = float(vstup_cas.get().replace(",", "."))
        except ValueError:
            sprava.set("Zadajte dve platné čísla.")
            return

        if not math.isfinite(praca) or not math.isfinite(cas):
            sprava.set("Zadajte konečné čísla.")
            return
        if cas <= 0:
            sprava.set("Čas musí byť väčší ako 0.")
            return

        vykon = vypocitaj_vykon(praca, cas)
        if not math.isfinite(vykon) or not math.isfinite(vypocitaj_vykon(max(prace), cas)):
            sprava.set("Výsledok je príliš veľký. Upravte vstupné hodnoty.")
            return

        sprava.set(f"Výkon: {vykon:.2f} W")
        vykresli(cas)

    ttk.Button(formular, text="Vypočítať", command=vypocitaj).grid(row=1, column=2)
    okno.bind("<Return>", vypocitaj)
    vstup_praca.focus_set()
    vykresli(5)
    okno.mainloop()


if __name__ == "__main__":
    main()
