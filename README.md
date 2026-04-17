# 🌤 Weather App (Python)

Aplicación en Python para consultar el clima actual y el pronóstico de una o múltiples ciudades usando la API de Open-Meteo.

Este proyecto está diseñado para **programadores principiantes**, pero incorpora buenas prácticas reales como arquitectura modular, manejo de errores y optimización con caché.

---

## 🎯 Objetivo del proyecto

La aplicación permite:

* Recibir una o varias ciudades ingresadas por el usuario
* Obtener sus coordenadas (latitud y longitud)
* Consultar el clima actual
* Obtener un pronóstico de 5 días
* Mostrar la información en un formato claro y amigable
* Optimizar llamadas a la API mediante caché

---

## 🧱 Estructura del proyecto

```
weather-app/
│
├── app/
│   ├── main.py                # Punto de entrada principal
│
│   ├── config/
│   │   └── settings.py        # Configuración (URLs, timeout, caché)
│
│   ├── models/
│   │   └── weather.py         # Modelo de datos Weather
│
│   ├── services/
│   │   └── weather_api.py     # Lógica de conexión con la API
│
│   ├── ui/
│   │   └── cli.py             # Interfaz de consola
│
│   └── utils/
│       ├── formatter.py       # Formateo de datos
│       └── cache.py           # Sistema de caché en memoria
│
├── run.py                     # Script de ejecución
├── requirements.txt           # Dependencias
└── README.md                  # Documentación
```

---

## ⚙️ ¿Cómo funciona?

Flujo principal:

1. El usuario elige si desea consultar una o varias ciudades
2. Se obtiene la latitud y longitud de cada ciudad
3. Se consulta el clima actual desde la API
4. Se consulta el pronóstico de 5 días
5. Se transforman los datos en objetos y texto legible
6. Se muestran los resultados en consola

---

## ⚡ Sistema de caché

La aplicación incluye un sistema de caché en memoria para mejorar el rendimiento.

* Evita llamadas repetidas a la API
* Reduce tiempos de respuesta
* Expira automáticamente (configurable)

Ejemplo:

```
⚡ Datos obtenidos desde caché
```

Configuración en:

```
app/config/settings.py
```

---

## 🚀 Instalación

### 1. Clonar el proyecto

```bash
git clone <url-del-repositorio>
cd weather-app
```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

Ejecuta la aplicación:

```bash
python run.py
```

---

### 🌍 Modo una ciudad

```
¿Una ciudad o varias? (1/m): 1
🌍 Ingresa el nombre de una ciudad: Bogota
```

---

### 🌍 Modo múltiples ciudades

```
¿Una ciudad o varias? (1/m): m
🌍 Ingresa ciudades separadas por coma: Bogota, Madrid, Lima
```

---

## 🖥 Ejemplo de salida

```
🌍 Bogota

╔══════════════════════╗
   🌤 Clima actual
╠══════════════════════╣
   Estado: Parcialmente nublado ⛅
   🌡 Temperatura: 18°C
   💨 Viento: 10 km/h
╚══════════════════════╝

📅 Pronóstico 5 días:
2026-04-16 | 🌤 12°C - 22°C
2026-04-17 | ☁️ 11°C - 20°C
```

---

## 🧠 Conceptos clave

### 🔹 Arquitectura modular

* `services/` → lógica de negocio y APIs
* `models/` → estructura de datos
* `utils/` → transformación y utilidades
* `ui/` → interacción con usuario
* `main.py` → orquestación del flujo

---

### 🔹 Manejo de errores

El sistema maneja:

* Entradas vacías
* Ciudades inexistentes
* Fallos de red
* Datos incompletos
* Errores de API

---

### 🔹 Concurrencia

Para múltiples ciudades se usa:

* `ThreadPoolExecutor`
* Consultas en paralelo
* Manejo independiente de errores por ciudad

---

## 🧪 Pruebas recomendadas

* Ciudades válidas (Bogota, Madrid)
* Entradas vacías o con espacios
* Ciudades inexistentes
* Múltiples ciudades
* Repetición de consultas (caché)
* Simulación de fallos de red

---

## 🔧 Posibles mejoras

* Interfaz gráfica (Tkinter, PyQt)
* Aplicación web (Flask o Django)
* Persistencia del caché (archivo o base de datos)
* Tests automatizados con pytest
* Soporte multilenguaje
* Historial de búsquedas

---

## 📌 Requisitos

* Python 3.8+
* Conexión a internet

---

## 👩‍💻 Contribución

Puedes contribuir:

* Mejorando el diseño de salida
* Agregando nuevos datos del clima
* Implementando pruebas automatizadas
* Mejorando el sistema de caché

---

## 🏁 Estado del proyecto

✅ Funcional
✅ Optimizado (caché)
✅ Soporte para múltiples ciudades
🚀 Listo para portafolio

---

Este proyecto demuestra buenas prácticas desde etapas tempranas: organización, manejo de errores, optimización y escalabilidad.
