# 18 - Backend EAC y progreso del estudiante

## Preparar el codigo

Crea la rama `practica/18-backend-eac` desde el resultado del ejercicio 17.

## Notas

- Este bloque practica una API de evaluacion.
- Deben distinguirse acciones de docente y estudiante.
- Las respuestas deben usar Resources.

## Ejercicios

1. Criterios de evaluacion

Crea o revisa `criterios_evaluacion`:

```text
id                         bigint autoincremental
resultado_aprendizaje_id    unsignedBigInteger
codigo                     string
descripcion                text
porcentaje                 decimal(5,2)
timestamps
```

2. Calificaciones

Crea una entidad para registrar calificaciones por estudiante y criterio:

```text
id                       bigint autoincremental
user_id                  unsignedBigInteger
criterio_evaluacion_id    unsignedBigInteger
puntuacion               decimal(5,2)
observaciones            text nullable
timestamps
```

3. Progreso del estudiante

Crea:

```text
GET /api/v1/estudiante/progreso
```

Debe devolver:

```text
modulos del estudiante
resultados de aprendizaje
criterios superados
porcentaje de progreso por modulo
```

4. Calificacion docente

Crea:

```text
POST /api/v1/docente/calificaciones
```

Entrada:

```json
{
  "estudiante_id": 1,
  "criterio_evaluacion_id": 4,
  "puntuacion": 8.5,
  "observaciones": "Trabajo correcto"
}
```

Solo un docente autenticado podra crear o actualizar una calificacion.

## Comprobacion

Registra una calificacion como docente y consulta el progreso como estudiante.
