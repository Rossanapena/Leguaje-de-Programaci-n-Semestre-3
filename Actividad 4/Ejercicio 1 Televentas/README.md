# Documentación Técnica

**Sistema de Gestión Museográfica en Java**

---

## 1. Introducción

Este sistema modela la gestión de obras de arte en un museo utilizando **Programación Orientada a Objetos en Java**.

Se implementan conceptos clave como:

* Generalización
* Especialización
* Jerarquía de clases
* Polimorfismo

---

## 2. Descripción del sistema

El sistema permite representar diferentes tipos de obras de arte, manteniendo una estructura jerárquica basada en una clase general.

---

## 3. Modelo de clases

* **Obra (clase base)**: contiene atributos comunes.
* **Pintura**: hereda de Obra e incluye técnica.
* **Escultura**: hereda de Obra e incluye material.

---

## 4. Funcionalidades

* Registro de obras
* Clasificación por tipo
* Visualización de información
* Uso de herencia para reutilización de código

---

## 5. Diagrama UML

Puedes visualizar el diagrama UML en el siguiente enlace:

https://mermaid.ai/app/projects/624e1028-269b-4cef-b26b-1961c8b1e276/diagrams/2fdfca60-4bf5-411c-9ae0-2fae227c4d2e/version/v0.1/edit

---

## 6. Conceptos aplicados

* **Generalización** → Clase `Obra`
* **Especialización** → `Pintura` y `Escultura`
* **Polimorfismo** → método `mostrarInfo()`

---

## 7. Implementación

* Lenguaje: Java
* Uso de herencia (`extends`)
* Sobrescritura de métodos (`@Override`)

---

## 8. Ejecución

Ejecutar:

```bash
java Main
```

---

## 9. Conclusión

Este ejercicio permitió evidenciar la jerarquía de clases y la reutilización de código mediante herencia, cumpliendo con los principios fundamentales de la POO.
