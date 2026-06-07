# 11 - Tokens, login API y usuario autenticado

## Preparar el codigo

Crea la rama `practica/11-tokens-api` desde el resultado del ejercicio 10.

## Notas

- Usa Sanctum.
- No devuelvas passwords ni datos sensibles.
- Las rutas protegidas deben usar `auth:sanctum`.

## Ejercicios

1. Crear token

Crea o revisa:

```text
POST /api/v1/tokens
```

Entrada:

```json
{
  "email": "usuario@example.com",
  "password": "password"
}
```

Respuesta correcta:

```json
{
  "token": "token_generado",
  "user": {
    "id": 1,
    "email": "usuario@example.com",
    "nombre": "Nombre",
    "apellidos": "Apellidos",
    "rol": "estudiante"
  }
}
```

2. Usuario autenticado

Crea o revisa:

```text
GET /api/v1/user
```

Debe devolver `id`, `email`, `nombre`, `apellidos`, `rol` y `fullName`.

3. Eliminar token

Crea o revisa:

```text
DELETE /api/v1/tokens
```

Debe eliminar el token actual y devolver JSON indicando que la sesion API ha finalizado.

4. Proteccion inicial

Protege con `auth:sanctum` las rutas de creacion, actualizacion y borrado de los recursos que no deban ser publicos.

## Comprobacion

Haz login por API, copia el Bearer token, consulta `/api/v1/user` y elimina el token.
