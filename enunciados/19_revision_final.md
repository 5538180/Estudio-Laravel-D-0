# 19 - Revision final acumulativa

## Preparar el codigo

Crea la rama `practica/19-revision-final` desde el resultado del ejercicio 18.

Este ejercicio no pide una entidad nueva. Sirve para revisar que el proyecto completo se puede entregar como simulacro.

## Notas

- No anadas funcionalidades nuevas si no corrigen algo roto.
- La base de datos debe regenerarse desde cero.
- La API debe responder de forma coherente en errores.

## Ejercicios

1. Reconstruccion limpia

Ejecuta:

```bash
php artisan migrate:fresh --seed
```

Corrige cualquier migracion, seeder o relacion que impida reconstruir la base de datos.

2. Rutas web

Comprueba:

```text
/catalog
/catalog/show/{id}
/users
/actividades
/reconocimientos
/curriculos
/perfil/{id?}
```

3. API publica

Comprueba listados y detalles:

```text
GET /api/v1/users
GET /api/v1/proyectos
GET /api/v1/ciclos
GET /api/v1/familias_profesionales
GET /api/v1/curriculos
GET /api/v1/actividades
GET /api/v1/reconocimientos
```

4. API protegida

Comprueba:

```text
POST /api/v1/tokens
GET /api/v1/user
DELETE /api/v1/tokens
POST /api/v1/curriculos/{id}/permisoDescarga
PUT /api/v1/curriculos/{idEmpresa}/permitirDescarga
```

5. Correos y ficheros

Comprueba:

```text
subida de imagen de familia profesional
subida de PDF de curriculo
subida de ZIP de proyecto
correo de registro de empresa
correo de solicitud de descarga
```

6. Entrega

Prepara un Pull Request con:

```text
resumen de cambios
pasos de prueba realizados
capturas o respuestas JSON relevantes si el profesor las pide
```

## Comprobacion final

El proyecto debe poder probarse desde cero con:

```bash
composer install
npm install
cp .env.example .env
php artisan key:generate
php artisan migrate:fresh --seed
php artisan serve
```
