"""
api.py — SmartManuTech FastAPI REST API
Expone los datos procesados por el simulador para consumo del dashboard.
Ejecutar: uvicorn api:app --reload --port 8000
"""

import sqlite3
import datetime
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

DB_PATH = "smartmanutech.db"

app = FastAPI(
    title="SmartManuTech IoT API",
    description="API de monitoreo IoT para líneas de producción",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def query_db(sql, params=()):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(sql, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ─── Endpoints ────────────────────────────────────────────────

@app.get("/", summary="Estado de la API")
def root():
    return {"status": "ok", "sistema": "SmartManuTech IoT Monitor"}


@app.get("/lecturas", summary="Últimas lecturas de todos los sensores")
def get_lecturas(limite: int = Query(50, ge=1, le=500)):
    """Devuelve las N lecturas más recientes de todos los sensores."""
    return query_db(
        "SELECT * FROM lecturas ORDER BY id DESC LIMIT ?", (limite,)
    )


@app.get("/anomalias", summary="Lecturas con estado ADVERTENCIA o CRITICO")
def get_anomalias(limite: int = Query(50, ge=1, le=500)):
    """Devuelve las anomalías detectadas ordenadas por severidad y tiempo."""
    return query_db(
        """SELECT * FROM lecturas
           WHERE estado IN ('ADVERTENCIA','CRITICO')
           ORDER BY CASE estado WHEN 'CRITICO' THEN 0 ELSE 1 END, id DESC
           LIMIT ?""",
        (limite,)
    )


@app.get("/alertas/count", summary="Conteo de alertas por tipo")
def get_alertas_count():
    """Número total de ADVERTENCIAS y CRÍTICOS por sensor."""
    rows = query_db(
        """SELECT sensor, estado, COUNT(*) as total
           FROM lecturas
           WHERE estado != 'NORMAL'
           GROUP BY sensor, estado
           ORDER BY sensor, estado"""
    )
    return rows


@app.get("/estadisticas", summary="Estadísticas por máquina y sensor")
def get_estadisticas():
    """Media, mínimo y máximo de cada sensor por máquina."""
    return query_db(
        """SELECT maquina, sensor,
                  ROUND(AVG(valor), 2) as media,
                  ROUND(MIN(valor), 2) as minimo,
                  ROUND(MAX(valor), 2) as maximo,
                  COUNT(*) as lecturas
           FROM lecturas
           GROUP BY maquina, sensor
           ORDER BY maquina, sensor"""
    )


@app.get("/estado/maquinas", summary="Estado actual de cada máquina")
def get_estado_maquinas():
    """Último estado registrado de cada sensor por máquina."""
    return query_db(
        """SELECT maquina, sensor, valor, estado, timestamp
           FROM lecturas
           WHERE id IN (
               SELECT MAX(id) FROM lecturas GROUP BY maquina, sensor
           )
           ORDER BY maquina, sensor"""
    )


@app.get("/resumen", summary="Resumen global del sistema")
def get_resumen():
    """Métricas globales: total lecturas, anomalías, críticos."""
    rows = query_db(
        """SELECT
             COUNT(*) as total_lecturas,
             SUM(CASE WHEN estado='ADVERTENCIA' THEN 1 ELSE 0 END) as advertencias,
             SUM(CASE WHEN estado='CRITICO'     THEN 1 ELSE 0 END) as criticos,
             SUM(CASE WHEN estado='NORMAL'      THEN 1 ELSE 0 END) as normales
           FROM lecturas"""
    )
    return rows[0] if rows else {}