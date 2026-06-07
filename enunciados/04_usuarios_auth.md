# 04 - Usuarios, perfiles y autenticacion

## Preparar el codigo

Crea la rama `practica/04-usuarios-auth` desde el resultado del ejercicio 03.

## Notas

- No elimines Breeze ni Sanctum.
- El perfil propio debe poder consultarse sin pasar id.
- El perfil debe servirse con controlador y vista; no con una ruta que devuelva texto directo.
- Los seeders deben crear usuarios con roles distintos.

## Ejercicios

1. Ampliacion de usuarios

Revisa o crea los campos de usuario:

```text
nombre      string(50) nullable
apellidos   string(100) nullable
avatar      string nullable
rol         string(30) default estudiante
```

Actualiza `User` para permitir el uso de estos campos y crea el accesor `fullName` si no existe.

2. Perfil

La ruta `GET /perfil/{id?}` debe llamar a un controlador y devolver una vista que muestre:

```text
email
nombre
apellidos
rol
curriculo si existe
proyectos relacionados si existen
```

Si no se indica `{id}`, se mostrara el usuario autenticado.

3. Proteccion de rutas

Protege con `auth` las rutas web de creacion y edicion de proyectos, usuarios, actividades, reconocimientos y curriculos.

4. Seeder de usuarios

El seeder debe crear al menos:

```text
1 administrador
2 docentes
5 estudiantes
2 empresas
```

## Comprobacion

Prueba login, logout, perfil propio, perfil por id y acceso anonimo a rutas protegidas.
