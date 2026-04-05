# Documentación Técnica

**Sistema de TeleVentas y Gestión Museográfica**

---

## 1. Introducción

Este proyecto contiene el desarrollo de dos sistemas en Python aplicando Programación Orientada a Objetos (POO).
Se implementan conceptos como clases, herencia, modularidad y organización del código.

---

## 2. Ejercicio 1: Sistema de TeleVentas

### 2.1 Descripción

Sistema encargado de gestionar pedidos, productos y envíos dentro de un entorno de ventas.

### 2.2 Clases principales

* **Producto**: maneja información como código, precio y stock.
* **OrdenCompra**: agrupa productos seleccionados por el cliente.
* **Envio**: gestiona la entrega del pedido.
* **SistemaTeleVentas**: coordina todo el proceso.

### 2.3 Funcionalidades

* Validación de inventario antes de confirmar pedidos
* Cálculo del total de compra
* Asignación de envíos

### 2.4 Diagrama UML

[https://mermaid.live/edit#LINK_TELEVENTAS](https://mermaid.ai/app/projects/624e1028-269b-4cef-b26b-1961c8b1e276/diagrams/2fdfca60-4bf5-411c-9ae0-2fae227c4d2e/version/v0.1/edit)

---

## 3. Ejercicio 2: Sistema de Gestión Museográfica

### 3.1 Descripción

Sistema para administrar piezas de un museo utilizando herencia entre clases.

### 3.2 Modelo de clases

* **Pieza** (clase base)
* **Pintura** (hereda de Pieza)
* **Escultura** (hereda de Pieza)

### 3.3 Roles del sistema

* **Encargado**: gestiona el catálogo
* **Restaurador Jefe**: mantenimiento de obras
* **Director**: supervisión general
* **Visitante**: consulta de información

### 3.4 Funcionalidades

* Registro de piezas
* Clasificación por tipo
* Control básico de información

### 3.5 Diagrama UML

[https://mermaid.live/edit#LINK_MUSEO](https://mermaid.live/edit#pako:eNplkE1PxCAQhv9KM-duU2jrFuJNvXs2XCYFd4kFNnwkurX_XVrtVuOF8AzvPDNhgsFJBRyGEUN41HjyaIRdqXjW6orFJGxRRB3T6HgRol8QU3R-J6vzk7ZxARUiyi05C7vLbEx-06nB6gH_p57CkMY9ZzAqr3H8Hfze6v7zcNicf2o3A5Rw8loCjz6pEozyBheE1SwgnpVRAni-SvRvArI_91zQvjhntjbv0ukM_BXHkCldZN7o55tuVa-sVP7BJRuBk251AJ_gPRMlFaFN35OadE1DSF_CB_CWVW3fsjvKOtowwvq5hOs6ta6Obduz-khr1rF80PkLU1OKgg)

---

## 4. Implementación

* Lenguaje: Python 3.9+
* Uso de clases y métodos
* Código organizado por módulos

---

## 5. Ejecución

```bash
python main.py
```
