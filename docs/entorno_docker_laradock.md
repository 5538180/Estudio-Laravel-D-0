# Entorno de trabajo

El repositorio esta actualizado para poder clonarse y ejecutar `composer install` directamente con PHP 8.4.

Docker/Laradock sigue siendo una opcion si quieres trabajar igual que en otros proyectos del curso, pero ya no es obligatorio para instalar dependencias.

## Arranque directo en la maquina virtual

Desde la carpeta del proyecto:

```bash
composer install
npm install
cp .env.example .env
php artisan key:generate
php artisan migrate:fresh --seed
php artisan serve
```

Para el frontend:

```bash
npm run dev
```

## Arranque con Docker/Laradock

Desde la maquina virtual:

```bash
cd ~/Documentos/laravel/laradock
docker compose up -d nginx mysql workspace
docker compose exec workspace bash
```

Si tu instalacion usa el comando antiguo:

```bash
docker-compose up -d nginx mysql workspace
docker-compose exec workspace bash
```

Dentro del contenedor `workspace`:

```bash
cd /var/www/Estudio-Laravel-D-0
composer install
npm install
cp .env.example .env
php artisan key:generate
php artisan migrate:fresh --seed
```

## Versiones esperadas

El proyecto mantiene la base del curso, pero con dependencias compatibles con PHP 8.4:

```text
Laravel 10
Sanctum 3
Inertia Laravel 1
PHP 8.4 compatible
```

No ejecutes `composer update` salvo que quieras actualizar dependencias de forma consciente. Para practicar los ejercicios basta con `composer install`.
