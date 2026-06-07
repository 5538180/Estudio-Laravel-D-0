# 06 - Curriculos, actividades y reconocimientos

## Preparar el codigo

Crea la rama `practica/06-curriculos-actividades-reconocimientos` desde el resultado del ejercicio 05.

## Notas

- El curriculo pertenece a un usuario estudiante.
- La actividad pertenece a un docente.
- El reconocimiento une estudiante y actividad.

## Ejercicios

1. Curriculos

Revisa o crea `curriculos`:

```text
id                 bigint autoincremental
user_id            unsignedBigInteger
video_curriculum   string nullable
pdf_curriculo      string nullable
sobre_mi           text nullable
timestamps
```

2. Actividades

Revisa o crea `actividades`:

```text
id           bigint autoincremental
docente_id   unsignedBigInteger
nombre       string
descripcion  text nullable
insignia     string nullable
timestamps
```

3. Reconocimientos

Revisa o crea `reconocimientos`:

```text
id                  bigint autoincremental
estudiante_id       unsignedBigInteger
actividad_id        unsignedBigInteger
documento           string nullable
docente_validador   unsignedBigInteger nullable
fecha               date nullable
timestamps
```

4. Controladores web

Los listados, detalles, creacion y edicion de curriculos, actividades y reconocimientos deben leer de la base de datos.

## Comprobacion

Crea un estudiante, un docente, una actividad y un reconocimiento. Comprueba que las relaciones se resuelven desde los modelos.
