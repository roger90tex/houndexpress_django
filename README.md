# Hound Express Backend

Proyecto backend desarrollado con Django y Django REST Framework para la gestión de estatus de envíos de la paquetería Hound Express.

## Descripción

Este proyecto permite administrar el registro de envíos y sus estatus mediante un API REST, almacenando la información en una base de datos para futuras consultas.

## Funcionalidades

- Crear envíos
- Consultar envíos
- Actualizar estatus de envíos
- Eliminar registros
- Administración desde panel Django Admin
- API REST con Django REST Framework

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- SQLite

## Estructura principal

- `config/`: configuración general del proyecto
- `shipments/`: app principal para envíos y estatus
- `manage.py`: administrador del proyecto

## Modelo principal

`ShipmentStatus`

Campos:
- `tracking_number`
- `customer_name`
- `origin`
- `destination`
- `status`
- `description`
- `created_at`
- `updated_at`

## Instalación y ejecución

1. Clonar el repositorio
2. Crear entorno virtual
3. Instalar dependencias:

```bash
pip install -r requirements.txt