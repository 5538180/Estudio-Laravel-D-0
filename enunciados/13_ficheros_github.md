# 13 - Ficheros de proyecto y API externa GitHub

## Preparar el codigo

Crea la rama `practica/13-ficheros-github` desde el resultado del ejercicio 12.

Configura en `.env`:

```env
GITHUB_TOKEN=
GITHUB_OWNER=
GITHUB_PROYECTOS_REPO=
```

## Notas

- No subas tokens reales al repositorio.
- Los ficheros admitidos son `zip`, `rar`, `bz`, `bz2` y `7z`.
- El tamano maximo sera 5120 KB.

## Ejercicios

1. Campo fichero en proyecto

Revisa o crea el campo `fichero` en `proyectos`. Debe guardar la ruta del fichero comprimido asociado al proyecto.

2. Subida por API

Permite subir el fichero al crear o actualizar un proyecto desde la API. Validacion:

```text
nullable
file
mimes:zip,rar,bz,bz2,7z
max:5120
```

El fichero se almacenara inicialmente en `repoZips`.

3. ProyectoResource

El Resource debe devolver:

```json
{
  "attachments": [
    {
      "src": "ruta_o_url",
      "title": "nombre_del_fichero"
    }
  ]
}
```

4. Servicio GitHub

Crea o revisa un servicio para:

```text
crear repositorio
eliminar repositorio
subir ficheros descomprimidos
calcular ruta de repositorio comun
obtener SHA de un fichero remoto
```

Si se usa repositorio comun, la ruta sera:

```text
/{ciclo}/{anio}/ficherosProyecto
```

## Comprobacion

Prueba la subida de un ZIP y comprueba que el Resource devuelve `attachments`.
