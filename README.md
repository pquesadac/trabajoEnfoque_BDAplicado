SmartManuTech IoT Sistema de Monitoreo | Hecho por Pablo Quesada | Big Data Aplicado

Sistema de monitorización en tiempo real para entornos industriales basado en tecnologías Big Data. Este proyecto simula sensores IoT en máquinas de producción, detecta anomalías y muestra los datos en un dashboard interactivo.

📌 Descripción
Este sistema ha sido desarrollado como solución al problema planteado por SmartManuTech, donde el alto volumen de datos generados por sensores IoT dificulta su procesamiento en tiempo real.

La aplicación permite:

Simular datos de sensores IoT
Detectar anomalías en tiempo real
Almacenar datos en una base de datos
Exponer los datos mediante una API REST
Visualizar el estado del sistema en un dashboard interactivo

⚙️ Tecnologías utilizadas
Python
FastAPI
SQLite (simulación de Cassandra)
HTML, CSS, JavaScript
Simulación de streaming de datos en tiempo real

🧠 Arquitectura del sistema
El flujo de datos sigue el siguiente esquema:

Sensores IoT (simulados) → Procesamiento en Python → Base de datos → API REST → Dashboard

🚀 Ejecución del proyecto
1. Clonar el repositorio
git clone https://github.com/pquesadac/trabajoEnfoque_BDAplicado.git
cd trabajoEnfoque_BDAplicado
2. Ejecutar el proyecto

En una terminal:

python simulador.py

Esto iniciará la generación de datos cada 2 segundos.

3. Ejecutar la API
En otra terminal:

python -m uvicorn api:app --reload --port 8000

La API estará disponible en:
👉 http://localhost:8000

4. Abrir el dashboard
Abrir el archivo dashboard.html en el navegador.

El dashboard se conectará automáticamente a la API y mostrará:
Estado de las máquinas
Alertas en tiempo real
Estadísticas del sistema

⚠️ Detección de anomalías
El sistema clasifica las lecturas en tres estados:
NORMAL
ADVERTENCIA
CRÍTICO

Estos estados se determinan mediante umbrales definidos para cada sensor.

📊 Funcionalidades principales
Generación continua de datos IoT
Procesamiento en tiempo real
Almacenamiento estructurado
API REST con múltiples endpoints
Dashboard interactivo con actualización automática

🔧 Limitaciones
Uso de SQLite en lugar de Cassandra (entorno de demostración)
Datos generados de forma simulada
No se utiliza Kafka real (simulación de streaming con Python)

🚀 Mejoras futuras
Implementación real de Apache Kafka
Uso de Cassandra en entorno distribuido
Integración de modelos de Machine Learning
Sistema de alertas por email o SMS
Despliegue en la nube con Docker
