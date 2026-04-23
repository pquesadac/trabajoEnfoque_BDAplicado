"""
simulador.py — SmartManuTech IoT Sensor Simulador
Simula sensores IoT, detecta anomalías y almacena en SQLite (equivalente a Cassandra en demo).
Ejecutar: python simulador.py
"""

import sqlite3
import random
import time
import datetime

DB_PATH = "smartmanutech.db"

THRESHOLDS = {
    "temperatura":         {"warn": 75.0,  "crit": 90.0},
    "vibracion":           {"warn": 6.0,   "crit": 9.0},
    "velocidad_produccion":{"warn": 20.0,  "crit": 10.0},   
    "consumo_energia":     {"warn": 80.0,  "crit": 95.0},
    "errores_maquina":     {"warn": 3,     "crit": 7},
}

MACHINES = ["M-01", "M-02", "M-03"]


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS lecturas (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp    TEXT NOT NULL,
            maquina      TEXT NOT NULL,
            sensor       TEXT NOT NULL,
            valor        REAL NOT NULL,
            estado       TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def detectar_estado(sensor, valor):
    t = THRESHOLDS[sensor]
    if sensor == "velocidad_produccion":
        if valor <= t["crit"]:  return "CRITICO"
        if valor <= t["warn"]:  return "ADVERTENCIA"
    else:
        if valor >= t["crit"]:  return "CRITICO"
        if valor >= t["warn"]:  return "ADVERTENCIA"
    return "NORMAL"


def generar_lectura(maquina):
    """Genera valores realistas con picos aleatorios ocasionales."""
    spike = random.random() < 0.12  # 12% de probabilidad de pico
    return {
        "temperatura":          round(random.uniform(60, 80) + (20 if spike else 0), 2),
        "vibracion":            round(random.uniform(2, 6)   + (5  if spike else 0), 2),
        "velocidad_produccion": round(random.uniform(18, 35) - (15 if spike else 0), 2),
        "consumo_energia":      round(random.uniform(50, 78) + (20 if spike else 0), 2),
        "errores_maquina":      random.randint(0, 4)         + (6  if spike else 0),
    }


def guardar_lecturas(lecturas):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.executemany(
        "INSERT INTO lecturas (timestamp, maquina, sensor, valor, estado) VALUES (?,?,?,?,?)",
        lecturas
    )
    conn.commit()
    conn.close()


def run():
    init_db()
    print(" SmartManuTech IoT Simulador iniciado")
    print(f"Base de datos: {DB_PATH}")
    print("Generando lecturas cada 2 segundos. Ctrl+C para detener.\n")

    while True:
        batch = []
        ts = datetime.datetime.now().isoformat(timespec="seconds")

        for maquina in MACHINES:
            datos = generar_lectura(maquina)
            for sensor, valor in datos.items():
                estado = detectar_estado(sensor, valor)
                batch.append((ts, maquina, sensor, valor, estado))
                if estado != "NORMAL":
                    print(f"[{ts}] ⚠ {maquina} | {sensor}: {valor} → {estado}")

        guardar_lecturas(batch)
        time.sleep(2)


if __name__ == "__main__":
    run()