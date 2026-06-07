# 01 - Vistas parciales y rutas con controlador

## Preparar el codigo

Crea la rama `practica/01-vistas-partials`.

Este ejercicio usa `routes/web.php`, `CatalogController` y vistas Blade ya presentes en el proyecto. No modifiques todavia la base de datos ni crees un layout completo nuevo.

## Notas

- No devuelvas texto directamente desde una ruta.
- Las rutas deben llamar a metodos de controlador.
- Practica `@include`, partials y paso de variables a vistas.
- Puedes reutilizar layouts existentes, pero el objetivo no es crear uno desde cero.

## Ejercicios

1. Rutas web con controlador

Revisa y deja preparadas estas rutas para que todas llamen a `CatalogController`:

```text
GET /catalog                  listado de proyectos
GET /catalog/show/{id}        detalle de proyecto
GET /catalog/create           formulario de creacion de proyecto
GET /catalog/edit/{id}        formulario de edicion de proyecto
```

El parametro `{id}` debe validarse con expresion regular para aceptar solo numeros naturales.

2. Vista de listado con partial de tarjeta

En la vista de listado de proyectos, usa un partial para pintar cada proyecto.

Partial esperado:

```text
resources/views/catalog/partials/project-card.blade.php
```

La vista principal debe recorrer la coleccion de proyectos y llamar al partial con `@include`, enviando el proyecto actual.

La tarjeta debe mostrar:

```text
nombre
dominio si existe
url_github si existe
calificacion si existe
enlace al detalle
enlace a editar
```

3. Partial de acciones

Crea un partial reutilizable para los botones o enlaces de acciones del proyecto:

```text
resources/views/catalog/partials/project-actions.blade.php
```

Debe poder usarse desde el listado y desde el detalle.

Acciones minimas:

```text
ver detalle
editar
volver al listado
```

4. Partial de formulario

Crea un partial para compartir el formulario entre crear y editar:

```text
resources/views/catalog/partials/project-form.blade.php
```

El partial debe recibir:

```text
proyecto o null
action
method
```

Debe incluir campos para `nombre`, `dominio`, `url_github` y `metadatos`.

5. Detalle desde controlador

El detalle de proyecto debe cargarse desde `CatalogController@getShow`. No debe ser una ruta con closure ni una respuesta de texto.

## Comprobacion

Ejecuta:

```bash
php artisan route:list
```

Comprueba:

```text
/catalog muestra varios proyectos usando project-card
/catalog/show/{id} usa controlador y vista
/catalog/create y /catalog/edit/{id} comparten project-form
```
