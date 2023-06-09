import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

fake = Faker()
planets = ["Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
accelerations = [9.8, 3.7, 24.8, 10.4, 8.9, 11.2]

def generate_sample():
    L = round(random.uniform(0.8, 2.5), 2)
    t = round(random.uniform(0.4, 0.7), 2)
    g_calculated = round((2 * L)/(t**2), 2)
    most_probable_planet = "Tierra" if abs(g_calculated - 9.8) < abs(g_calculated - 9.0) else "Saturno"
    second_most_probable_planet = "Saturno" if most_probable_planet == "Tierra" else "Tierra"

    return {
        "ID": fake.uuid4(),
        "Longitud (m)": L,
        "Tiempo (s)": t,
        "Gravedad calculada (m/s^2)": g_calculated,
        "Planeta más probable": most_probable_planet,
        "Segundo planeta más probable": second_most_probable_planet
    }

dataset = ([generate_sample() for _ in range(100)])

df = pd.DataFrame(dataset)
print(df.describe())

df.hist(column=["Longitud (m)", "Tiempo (s)", "Gravedad calculada (m/s^2)"])
plt.show()

plt.scatter(df["Longitud (m)"], df["Tiempo (s)"])
plt.xlabel("Longitud (m)")
plt.ylabel("Tiempo (s)")
plt.show()

label_encoder = LabelEncoder()
df["Planeta más probable (código)"] = label_encoder.fit_transform(df["Planeta más probable"])
df["Segundo planeta más probable (código)"] = label_encoder.fit_transform(df["Segundo planeta más probable"])

print(df.corr())

x = df["Longitud (m)"].values.reshape(-1, 1)
y = df["Tiempo (s)"].values.reshape(-1, 1)

model = LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)

plt.scatter(x, y, color="red")
plt.plot(x, y_pred, color="green")
plt.xlabel("Longitud (m)")
plt.ylabel("Tiempo (s)")
plt.show()

print(df["Planeta más probable"].value_counts())
print(df["Segundo planeta más probable"].value_counts())





