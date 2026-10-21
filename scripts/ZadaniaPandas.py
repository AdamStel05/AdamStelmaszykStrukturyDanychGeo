import pandas as pd
import os
import statistics

# Zadanie a
dataA = {
    "imie": ["Adam", "Jan", "Marta", "Anna", "Wojciech", "Karol", "Zofia", "Wiktoria", "Artur", "Beata"],
    "wzrost (cm)": [186, 180, 163, 167, 176, 187, 173, 170, 190, 165],
    "waga (kg)": [94, 85, 68, 66, 80, 83, 65, 71, 81, 70]
}
dfA = pd.DataFrame(dataA)

dfA["BMI"] = (dfA["waga (kg)"] / ((dfA["wzrost (cm)"]/100)**2))
print(dfA)

# Zadanie b
dataB = {
    "miasto": ["Poznań", "Pekin", "Santiago", "Kair", "Vancouver"],
    "panstwo": ["Polska", "Chiny", "Chile", "Egipt", "Kanada"],
    "populacja (tys)": [534, 21893, 6767, 9539, 603]
}
dfB = pd.DataFrame(dataB)
print(dfB)

sciezka = input()
path = os.path.join(f"{sciezka}", "dataB.json")
dfB.to_json(path)

dfBplik = pd.read_json(f"{sciezka}/dataB.json")
print(dfBplik)

# Odpowiedź - Obie wersje DataFrame są identyczne.

# Zadanie c
dfA["wiek"] = [21, 24, 25, 22, 19, 26, 27, 23, 20, 28]
print(dfA)

srednia = statistics.mean(dfA["wiek"])
dfFiltr = (dfA[(dfA["wiek"] > srednia) & (dfA["BMI"] > 25)])

dataC = {}
dfC = pd.DataFrame(dataC)
dfC["imie"] = dfFiltr["imie"]
dfC["wiek"] = dfFiltr["wiek"]
dfC["BMI"] = dfFiltr["BMI"]
print(dfC)