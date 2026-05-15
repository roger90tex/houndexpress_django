# Hound Express Backend

Backend desarrollado con Django REST Framework para gestionar envíos, clientes y datos de rastreo del sistema Hound Express.

---

## Descripción

Este proyecto funciona como API REST para el frontend de Hound Express. Permite administrar registros de envíos mediante endpoints que pueden ser consumidos desde una aplicación React + TypeScript.

---

## Tecnologías

- Python
- Django
- Django REST Framework
- SQLite
- Git / GitHub

---

## Funcionalidades

- Registro de envíos
- Consulta de envíos
- Actualización de información de guías
- Eliminación de registros
- Exposición de datos mediante API REST
- Integración con frontend en React

---

## Modelo principal

El sistema maneja información básica de envíos como:

- Número de guía
- Nombre del cliente
- Origen
- Destino
- Estado del envío
- Descripción
- Fecha de creación
- Fecha de actualización

---

## Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/roger90tex/houndexpress_django.git
cd houndexpress_django
