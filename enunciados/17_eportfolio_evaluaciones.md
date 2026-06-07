# 17 - ePortfolio, evidencias y evaluaciones

## Preparar el codigo

Crea la rama `practica/17-eportfolio-evaluaciones` desde el resultado del ejercicio 16.

## Notas

- Este bloque practica recursos anidados.
- Mantén el prefijo `/api/v1`.
- Usa Resources para las respuestas.

## Ejercicios

1. Rutas anidadas

Crea o revisa rutas equivalentes a:

```text
GET /api/v1/familias-profesionales/{familia}/ciclos-formativos
GET /api/v1/ciclos-formativos/{ciclo}/modulos-formativos
GET /api/v1/modulos-formativos/{modulo}/resultados-aprendizaje
GET /api/v1/resultados-aprendizaje/{resultado}/criterios-evaluacion
GET /api/v1/criterios-evaluacion/{criterio}/tareas
GET /api/v1/tareas/{tarea}/evidencias
```

2. Evaluaciones

Crea `evaluaciones`:

```text
id             bigint autoincremental
evidencia_id   unsignedBigInteger
user_id        unsignedBigInteger
puntuacion     decimal(5,2) nullable
estado         enum pendiente/aprobado/suspenso default pendiente
observaciones  text nullable
timestamps
```

3. Endpoints

Crea:

```text
GET  /api/v1/evidencias/{id}/evaluaciones
POST /api/v1/evidencias/{id}/evaluaciones
GET  /api/v1/users/{id}/evidencias
GET  /api/v1/users/{id}/asignaciones-revision
```

4. Permisos

Un docente asignado puede crear evaluaciones. Un estudiante puede consultar sus evidencias y estados.

## Comprobacion

Crea una evidencia, registra una evaluacion como docente y consultala como estudiante.
