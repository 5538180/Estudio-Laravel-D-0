# 09 - React-admin, filtros y cabeceras

## Preparar el codigo

Crea la rama `practica/09-reactadmin-filtros` desde el resultado del ejercicio 08.

## Notas

- React-admin necesita listados con cabecera `X-Total-Count`.
- El filtro `q` debe funcionar en varios modelos.
- La ordenacion debe controlarse desde parametros.

## Ejercicios

1. Middleware de respuesta

Revisa o crea un middleware que adapte las respuestas de listado para React-admin:

```text
elimina envoltorios innecesarios si existen
anade X-Total-Count
mantiene JSON valido
```

2. Busqueda general

Anade el parametro `q` a los listados. Debe buscar en los campos que existan:

```text
name
nombre
apellidos
email
descripcion
```

Ejemplos:

```text
GET /api/v1/users?q=garcia
GET /api/v1/empresas?q=software
```

3. Ordenacion

Anade soporte a:

```text
_sort
_order
```

Ejemplo:

```text
GET /api/v1/proyectos?_sort=nombre&_order=DESC
```

4. Helper reutilizable

Extrae la logica compartida a un helper o metodo reutilizable para no repetir el mismo codigo en todos los controladores.

## Comprobacion

Comprueba que `X-Total-Count` refleja el total despues de filtrar, no el total completo de la tabla.
