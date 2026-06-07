# 02 - Controladores web y formularios

## Preparar el codigo

Crea la rama `practica/02-controladores-formularios` desde el resultado del ejercicio 01.

## Notas

- Los formularios deben incluir `@csrf`.
- Las actualizaciones deben usar `@method('PUT')`.
- La logica de negocio no debe quedar dentro de `routes/web.php`.
- No crees un layout nuevo para este ejercicio; usa las vistas y partials del ejercicio anterior.

## Ejercicios

1. Controlador de catalogo

Completa o revisa `CatalogController` para que tenga metodos equivalentes a:

```text
getIndex
getShow
getCreate
getEdit
store
putEdit
editCalificacion
```

Cada metodo debe devolver una vista Blade. No debe haber rutas que devuelvan strings ni closures con logica de proyecto.

2. Formulario de proyecto compartido

Usa el partial `resources/views/catalog/partials/project-form.blade.php` creado en el ejercicio anterior para la creacion y la edicion.

El formulario debe trabajar con estos campos:

```text
user_id
nombre
dominio
url_github
metadatos
calificacion
```

El campo `calificacion` solo debe poder modificarse desde la ruta especifica de calificacion.

3. Validacion basica

Valida como minimo:

```text
nombre       obligatorio, maximo 120 caracteres
dominio      nullable, maximo 30 caracteres
url_github   nullable, url
metadatos    nullable, texto
calificacion nullable, numerica
```

Si la validacion falla, debe volver al formulario con errores.

## Comprobacion

Usa navegador para crear, editar y consultar un proyecto. Comprueba tambien que una peticion PUT sin CSRF no se acepta.
