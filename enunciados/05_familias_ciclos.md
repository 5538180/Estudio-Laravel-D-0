# 05 - Familias profesionales y ciclos

## Preparar el codigo

Crea la rama `practica/05-familias-ciclos` desde el resultado del ejercicio 04.

## Notas

- Respeta los nombres de tabla usados durante el curso.
- Las relaciones deben declararse en ambos modelos.
- Los datos iniciales deben cargarse con seeders.

## Ejercicios

1. Familias profesionales

Revisa o crea `familias_profesionales`:

```text
id        bigint autoincremental
codigo    char(4) unique
nombre    string(200)
imagen    string nullable
timestamps
```

2. Ciclos

Revisa o crea `ciclos`:

```text
id                       bigint autoincremental
familia_profesional_id   unsignedBigInteger
codigo                   string(10)
nombre                   string(200)
grado                    string(20)
timestamps
```

3. Relaciones

Define:

```text
FamiliaProfesional hasMany Ciclo
Ciclo belongsTo FamiliaProfesional
```

4. Seeders

Carga familias y ciclos reales. Puedes usar los datos de los materiales del curso si ya estan en el proyecto.

## Comprobacion

Desde Tinker, comprueba:

```php
App\Models\FamiliaProfesional::first()->ciclos
App\Models\Ciclo::first()->familiaProfesional
```
