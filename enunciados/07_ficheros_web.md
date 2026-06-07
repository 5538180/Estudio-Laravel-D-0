# 07 - Subida de ficheros web

## Preparar el codigo

Crea la rama `practica/07-ficheros-web` desde el resultado del ejercicio 06.

## Notas

- Los formularios de subida deben usar `multipart/form-data`.
- Los ficheros deben guardarse en el disco `public`.
- Si no existe fichero, debe mostrarse un valor por defecto.

## Ejercicios

1. Imagen de familia profesional

Permite subir una imagen para una familia profesional. Validacion:

```text
nullable
image
mimes:jpg,jpeg,png,webp
max:2048
```

Guarda el fichero en `imagenes`.

2. PDF de curriculo

Permite asociar un PDF a un curriculo. Validacion:

```text
nullable
file
mimes:pdf
max:5120
```

Guarda el fichero en una carpeta especifica para curriculos.

3. Documento de reconocimiento

Permite subir un documento justificativo al crear o editar un reconocimiento. El listado debe mostrar si el documento existe.

4. Enlace publico

Comprueba que `php artisan storage:link` permite acceder a los ficheros desde navegador.

## Comprobacion

Sube una imagen, un PDF y un documento. Rechaza manualmente un fichero con extension incorrecta.
