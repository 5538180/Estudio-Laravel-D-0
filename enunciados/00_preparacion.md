# 00 - Preparacion del codigo para practicar

## Preparar el codigo

Parte de este repositorio. Clonalo en tu maquina de trabajo y crea una rama por cada ejercicio.

Antes de empezar:

```bash
cp .env.example .env
composer install
npm install
php artisan key:generate
php artisan migrate:fresh --seed
```

Si usas SQLite, configura el fichero `.env` segun el metodo visto en clase. Si usas MySQL/MariaDB, crea la base de datos y revisa `DB_DATABASE`, `DB_USERNAME` y `DB_PASSWORD`.

## Notas

- No se entregan soluciones en este repositorio.
- Cada ejercicio debe funcionar antes de pasar al siguiente.
- Cada ejercicio debe terminar con un commit.
- Las pruebas de API se haran con Talet API Tester, Rested, Postman o herramienta equivalente.
- Las rutas API deben mantenerse bajo `/api/v1`.
- Usa los mismos patrones del curso: controladores, Resources, migraciones, seeders, middleware, policies y Mailables.

## Entrega recomendada

Para cada ejercicio:

1. Crea una rama `practica/NN-nombre`.
2. Implementa solo lo que pide el enunciado.
3. Ejecuta `php artisan migrate:fresh --seed`.
4. Comprueba las rutas web o API indicadas.
5. Haz commit.
6. Crea Pull Request si quieres simular entrega.

## Variables de entorno que se usaran

```env
APP_URL=http://localhost:8000
FRONTEND_URL=http://localhost:5173
EMAIL_EMPRESA=tu_correo@alu.murciaeduca.es
GITHUB_TOKEN=
GITHUB_OWNER=
GITHUB_PROYECTOS_REPO=
MAIL_MAILER=smtp
```
