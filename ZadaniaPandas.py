import pandas as pd

data = {
    "imie": ["Adam", "Jan", "Marta", "Anna", "Wojciech", "Karol", "Zofia", "Wiktoria", "Artur", "Beata"],
    "wzrost (cm)": [186, 180, 163, 167, 176, 187, 173, 170, 190, 165],
    "waga (kg)": [94, 85, 68, 66, 80, 83, 65, 71, 81, 70]
}

df = pd.DataFrame(data)

df["BMI"] = df["waga (kg)"] / df["wzrost (cm)"]^2
print(df)