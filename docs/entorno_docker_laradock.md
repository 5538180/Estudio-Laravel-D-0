# Entorno Docker/Laradock

Este repositorio debe ejecutarse con el mismo entorno que los proyectos Laravel usados durante el curso.

No uses el PHP del sistema de la maquina virtual si es PHP 8.4. El proyecto base es Laravel 10 con dependencias del curso y el `composer.lock` esta pensado para el entorno Docker/Laradock habitual, no para actualizar paquetes a PHP 8.4.

## Arranque recomendado

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

Para arrancar Laravel:

```bash
php artisan serve --host=0.0.0.0 --port=8000
```

Para el frontend:

```bash
npm run dev -- --host=0.0.0.0
```

## Si Composer falla en la VM

Si ves un error parecido a:

```text
your php version (8.4.x) does not satisfy that requirement
```

significa que estas ejecutando `composer install` fuera del contenedor.

La solucion correcta para esta practica es entrar al contenedor `workspace` y ejecutar Composer alli.

## Versiones esperadas

El proyecto mantiene la pila del curso:

```text
Laravel 10
Sanctum 3
Inertia Laravel 0.6
PHP del contenedor Docker/Laradock del curso
```

No ejecutes `composer update` salvo que el ejercicio lo pida expresamente. La practica debe partir del mismo estilo y dependencias que los demas proyectos.
