# Documentación Técnica

**Sistema de TeleVentas en Java**

---

## 1. Introducción

Este proyecto implementa un sistema de ventas utilizando **Programación Orientada a Objetos en Java**.

Se aplican conceptos fundamentales como:

* Encapsulamiento
* Herencia
* Polimorfismo
* Relaciones entre clases

---

## 2. Descripción del sistema

El sistema permite gestionar el proceso de venta de productos, incluyendo la interacción entre clientes, productos y métodos de pago.

---

## 3. Clases principales

* **Cliente**: representa al cliente del sistema.
* **Producto**: contiene información del producto como nombre y precio.
* **Venta**: gestiona la relación entre cliente, producto y cantidad.
* **Pago (clase abstracta)**: define el comportamiento general del pago.
* **PagoTarjeta**: implementación específica del pago mediante tarjeta.

---

## 4. Funcionalidades

* Cálculo del total de la venta
* Procesamiento del pago
* Visualización de la información de la compra

---

## 5. Diagrama UML


https://mermaid.ai/app/projects/624e1028-269b-4cef-b26b-1961c8b1e276/diagrams/2fdfca60-4bf5-411c-9ae0-2fae227c4d2e/version/v0.1/edit

---

## 6. Conceptos aplicados

* **Encapsulamiento** → uso de atributos privados
* **Herencia** → `Pago` → `PagoTarjeta`
* **Polimorfismo** → método `procesarPago()`

---

## 7. Implementación

* Lenguaje: Java
* Uso de clases separadas
* Aplicación de principios de POO

---

## 8. Ejecución

Ejecutar la clase principal:

```bash id="l2u6kg"
java Main
```

---

## 9. Conclusión

Este ejercicio permitió aplicar correctamente los conceptos de programación orientada a objetos, evidenciando una estructura clara, modular y reutilizable del sistema.

