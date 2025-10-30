
# Diseño del Sistema de Gestión de Tareas

## Objetivo
Implementar un sistema modular con `Task` y `TaskManager` siguiendo TDD, SOLID y Clean Code.

## Decisiones de Diseño
- **Enums** para `Priority` y `Status` (evitan strings mágicos).
- **Dataclass** para `Task` (inmutabilidad controlada, legibilidad).
- **Validaciones** estrictas en setters para evitar estados inválidos.
- **TaskManager** mantiene una lista interna (_tasks) y garantiza unicidad por `id`.

## Principios SOLID
- **SRP:** `Task` gestiona su propio estado; `TaskManager` coordina y consulta.
- **OCP:** Nuevos estados/prioridades vía enums sin modificar lógica de negocio.
- **LSP:** No se rompen sustituciones; métodos conservan contratos.
- **ISP:** Interfaz mínima y explícita de `TaskManager`.
- **DIP:** Depende de abstracciones (`Task`, `Enum`), no de implementaciones concretas externas.

## Flujo TDD
1. Escribir test (rojo).
2. Implementar lo mínimo (verde).
3. Refactorizar conservando los tests.
