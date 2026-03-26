# Documentación Técnica: Sistema de Gestión TeleVentas y Administración de Acervo Museográfico

## 1. Introducción
El presente documento detalla la arquitectura, el diseño y la implementación de dos soluciones de software desarrolladas en lenguaje Python. Ambos sistemas han sido diseñados bajo el paradigma de Programación Orientada a Objetos (POO), aplicando principios de modularización, tipado estricto y separación de responsabilidades.

---

## 2. Ejercicio 1: Sistema de Soporte de Compras (TeleVentas)

### 2.1. Arquitectura de Clases
El sistema se divide en entidades que representan el núcleo del negocio de ventas a distancia.

| Clase              | Responsabilidad                                                                 |
|-------------------|-------------------------------------------------------------------------------|
| Producto          | Gestión de atributos físicos (código, precio, stock) y estado del inventario. |
| OrdenCompra       | Agrupación de productos seleccionados por un cliente y estado del pedido.     |
| Envio             | Gestión de la logística externa y asignación de transportistas.               |
| SistemaTeleVentas | Controlador principal que orquesta la interacción entre clientes y depósito.  |

### 2.2. Flujo de Procesos

- **Sincronización de Inventario:**  
  El sistema interactúa con un inventario preexistente para validar la disponibilidad antes de confirmar cualquier orden.

- **Gestión de Quejas:**  
  Implementación de un canal de comunicación directa con la gerencia para incidencias de clientes.

- **Logística:**  
  Selección automatizada de transportista basada en criterios de valor y tipo de producto.

---

## 3. Ejercicio 2: Sistema de Gestión Museográfica

### 3.1. Modelado de Datos (UML Conceptual)

Para este sistema se aplicó el principio de Herencia, donde una clase base define atributos comunes y las subclases especializan el comportamiento.

enlace: https://mermaid.live/edit#pako:eNqNUctOwzAQ_JVoTyDSKmkSHFlcqsIZCW4olyV2UwvHrjZ2BZR-EN_Bj-GmD6UiB_bkmfXOjHa3UFshgUNlao1dd6-wIWwrE4XqmejxlXBOTkbbA7uvm2dHyjSRU85r-5dH7ywN6KW26KIN6gv2-Fl2DsVQRJqNQpo_7RuesFbWXF0f-rthsoVHQXY01893bVSNo2bqlPhC7KGrvXbBbkyvRSdJof6X3nlhd1-TyTHkWOfsCDE0pARwR17G0EpqcQ-hT1KBW8lWVsDDUyC9VeFYuzCzRvNibXsaI-ubFfAl6i4gvxYh8_GcZ5akEZIW1hsHPL3tNYBv4R14xvJpnmR5XhSMsbRIihg-gOfltExnxSzLWJnkLGXFLobP3jaZlgH9ApbgsPU

### 3.2. Gestión de Seguridad y Roles

Se implementó un control de acceso basado en roles (RBAC) para garantizar la integridad de la información:

- **Encargado:**  
  Único perfil con permisos para la inserción y modificación de metadatos en el catálogo.

- **Restaurador Jefe:**  
  Responsable del ciclo de vida de mantenimiento de las obras.

- **Director:**  
  Acceso a reportes financieros y gestión de activos cedidos (Cesiones).

- **Visitante:**  
  Interfaz de solo lectura para consulta de obras disponibles por sala.

---

### 3.3. Lógica de Negocio Avanzada

- **Mantenimiento Preventivo:**  
  Algoritmo de detección automática para obras con más de cinco años desde su última intervención.

- **Gestión de Cesiones:**  
  Sistema de colas (First-In, First-Out) para solicitudes de museos externos sobre obras ya cedidas.

---

## 4. Estándares de Implementación

### 4.1. Tipado y Calidad de Código

Se ha utilizado el módulo `typing` de Python para implementar Type Hints, asegurando la robustez del código y facilitando el mantenimiento futuro.

$$
\text{Calidad} = \frac{\text{Modularización} + \text{Tipado Estricto}}{\text{Complejidad Ciclomática}}
$$

---

### 4.2. Control de Versiones

El proyecto sigue un flujo de trabajo basado en ramas (Branching), permitiendo un desarrollo aislado de la rama principal (`main`) para garantizar la estabilidad del código en producción.

---

## 5. Instrucciones de Ejecución

Para ejecutar cualquiera de los módulos, se requiere Python 3.9 o superior.

```bash
# Ejemplo de ejecución del sistema de museo
python main.py