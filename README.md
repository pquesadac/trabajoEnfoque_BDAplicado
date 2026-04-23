#  SmartManuTech – Sistema IoT de Monitorización en Tiempo Real | Hecho por Pablo Quesada Castellano | Big Data Aplicado

Sistema de monitorización industrial basado en **Big Data**, desarrollado para simular el uso de sensores IoT en máquinas de producción. Permite detectar anomalías en tiempo real, almacenar datos y visualizarlos mediante un dashboard interactivo.

---

## 📌 Descripción

Este proyecto surge como solución al problema de SmartManuTech, donde el gran volumen de datos generado por sensores IoT impide su procesamiento en tiempo real.

La aplicación permite:

*  Simular datos de sensores IoT
*  Detectar anomalías en tiempo real
*  Almacenar datos en base de datos
*  Exponer datos mediante una API REST
*  Visualizar el estado del sistema en un dashboard

---

## 🛠 Tecnologías utilizadas

| Tecnología         | Descripción                             |
| ------------------ | --------------------------------------- |
| Python             | Procesamiento de datos y simulación     |
| FastAPI            | API REST para exponer datos             |
| SQLite             | Base de datos (simulación de Cassandra) |
| HTML, CSS, JS      | Dashboard interactivo                   |
| Streaming simulado | Flujo de datos en tiempo real           |

---

## 🧠 Arquitectura del sistema

El sistema sigue un flujo de datos típico de Big Data:

**Sensores IoT (simulados) → Procesamiento → Base de datos → API → Dashboard**

---

## 🚀 Ejecución del proyecto

### 1️⃣ Clonar repositorio

```bash
git clone https://github.com/pquesadac/trabajoEnfoque_BDAplicado.git
cd trabajoEnfoque_BDAplicado
```

---

### 2️⃣ Ejecutar simulador

En una terminal:

```bash
python simulador.py
```

 Genera datos cada 2 segundos

---

### 3️⃣ Ejecutar API

En otra terminal:

```bash
python -m uvicorn api:app --reload --port 8000
```

 Disponible en: http://localhost:8000

---

### 4️⃣ Abrir dashboard

Abrir el archivo:

```bash
dashboard.html
```

 Mostrará:

* Estado de máquinas
* Alertas en tiempo real
* Estadísticas

---

##  Detección de anomalías

El sistema clasifica las lecturas en:

* 🟢 NORMAL
* 🟡 ADVERTENCIA
* 🔴 CRÍTICO

Basado en umbrales definidos para cada sensor.

---

## 📊 Funcionalidades

* Generación continua de datos IoT
* Procesamiento en tiempo real
* API REST con múltiples endpoints
* Dashboard dinámico
* Sistema de alertas

---

## 🔧 Limitaciones

* Uso de SQLite en lugar de Cassandra
* Datos simulados (no reales)
* No se utiliza Kafka real (streaming simulado con Python)

---

## 🚀 Mejoras futuras

* Implementación de Apache Kafka
* Uso de Cassandra en entorno distribuido
* Modelos de Machine Learning
* Sistema de notificaciones (email/SMS)
* Despliegue en la nube con Docker


