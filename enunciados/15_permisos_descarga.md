# 15 - Permisos de descarga de curriculo

## Preparar el codigo

Crea la rama `practica/15-permisos-descarga` desde el resultado del ejercicio 14.

Este ejercicio simula una segunda convocatoria.

## Notas

- La empresa se autentica usando el endpoint de acceso por token.
- El estudiante autoriza la descarga desde su usuario autenticado.
- Debe enviarse correo cuando una empresa solicita ver el curriculo.

## Ejercicios

1. Tabla permisos_descargas

Crea la tabla:

```text
id            bigint autoincremental
curriculo_id  unsignedBigInteger
empresa_id    unsignedBigInteger
validado      boolean nullable
timestamps
```

Significado de `validado`:

```text
NULL   solicitud pendiente
true   descarga autorizada
false  empresa baneada para ese curriculo
```

2. Modelo y Resource

Crea `PermisoDescarga` y `PermisoDescargaResource`.

El Resource debe devolver:

```json
{
  "id": 1,
  "curriculo_id": 1,
  "empresa_id": 5,
  "validado": null
}
```

3. Solicitar descarga

Crea:

```text
POST /api/v1/curriculos/{id}/permisoDescarga
```

Debe:

```text
comprobar que el usuario autenticado es empresa
crear la solicitud si no existe
guardar curriculo_id, empresa_id y validado null
enviar correo al estudiante del curriculo
devolver PermisoDescargaResource
```

4. Autorizar descarga

Crea:

```text
PUT /api/v1/curriculos/{idEmpresa}/permitirDescarga
```

Debe:

```text
comprobar que el usuario autenticado es estudiante
buscar el curriculo del estudiante autenticado
buscar la solicitud de esa empresa
poner validado a true
devolver PermisoDescargaResource
```

5. Middleware de empresa baneada

Crea un middleware que devuelva `412 Precondition Failed` si la empresa autenticada tiene alguna fila `validado = false`.

## Comprobacion

Haz el flujo completo:

```text
empresa obtiene token
empresa solicita permiso
estudiante autoriza
empresa vuelve a consultar el estado
```
