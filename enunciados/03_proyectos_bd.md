# 03 - Proyectos, migraciones, modelos y seeders

## Preparar el codigo

Crea la rama `practica/03-proyectos-bd` desde el resultado del ejercicio 02.

## Notas

- La base de datos debe reconstruirse con `php artisan migrate:fresh --seed`.
- El modelo debe usar los campos asignables de forma masiva.
- Los seeders deben crear datos suficientes para probar listados y detalles.

## Ejercicios

1. Tabla proyectos

Revisa o crea la migracion de `proyectos` con esta estructura minima:

```text
id            bigint autoincremental
user_id       unsignedBigInteger nullable
nombre        string(120)
dominio       string(30) nullable
url_github    string nullable
fichero       string nullable
metadatos     text nullable
calificacion  decimal nullable
timestamps
```

2. Modelo Proyecto

Configura el modelo `Proyecto` con:

```text
$fillable
relacion con User como tutor o docente
relaciones que ya existan con ciclos y participantes si estan disponibles
```

3. Seeder

Crea o ajusta el seeder para generar al menos 10 proyectos. Algunos deben tener `url_github`, otros `dominio` y otros `calificacion`.

4. Uso desde controlador

El listado y detalle de proyectos deben leer de la base de datos. No debe haber proyectos escritos directamente en arrays dentro de las vistas.

## Comprobacion

Ejecuta:

```bash
php artisan migrate:fresh --seed
php artisan tinker
```

Comprueba que `App\Models\Proyecto::count()` devuelve registros y que el listado web los muestra.
