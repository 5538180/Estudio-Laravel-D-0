# 08 - API REST con Resources

## Preparar el codigo

Crea la rama `practica/08-api-resources` desde el resultado del ejercicio 07.

## Notas

- Todas las rutas deben estar bajo `/api/v1`.
- Usa `Route::apiResource`.
- Las respuestas deben pasar por Resources cuando haya modelo.

## Ejercicios

1. Recursos principales

Revisa o crea controladores API y Resources para:

```text
users
proyectos
familias_profesionales
ciclos
competencias
idiomas
curriculos
actividades
reconocimientos
empresas
```

2. Rutas REST

Cada recurso debe responder a:

```text
GET    /api/v1/{recurso}
POST   /api/v1/{recurso}
GET    /api/v1/{recurso}/{id}
PUT    /api/v1/{recurso}/{id}
DELETE /api/v1/{recurso}/{id}
```

3. Resources

Los Resources deben devolver `id` y los campos principales. Si hay relaciones directas relevantes, pueden incluirse de forma controlada.

4. Codigos de respuesta

Usa codigos HTTP coherentes:

```text
200 lectura o actualizacion correcta
201 creacion correcta
404 registro no encontrado
422 validacion incorrecta
```

## Comprobacion

Prueba cada recurso con cliente API. Comprueba como minimo listado, detalle, creacion y actualizacion de un recurso.
