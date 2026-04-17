# 03. Composer, PHP y Laravel Installer

## 1. Qué es PHP
PHP es el lenguaje sobre el que funciona Laravel. Laravel no sustituye PHP: lo organiza y lo estructura.

## 2. Qué es Composer
Composer es el gestor de dependencias de PHP.

Sirve para:
- instalar paquetes
- actualizar paquetes
- cargar clases automáticamente
- ejecutar scripts del proyecto

## 3. Archivo `composer.json`
Es el archivo donde se define:
- versión de PHP requerida
- dependencias del proyecto
- dependencias de desarrollo
- scripts
- autoload

## 4. Comandos básicos de Composer
Instalar dependencias del proyecto:
```bash
composer install
```

Actualizar dependencias:
```bash
composer update
```

Instalar una dependencia:
```bash
composer require paquete/nombre
```

Instalar una dependencia de desarrollo:
```bash
composer require --dev paquete/nombre
```

Regenerar autoload:
```bash
composer dump-autoload
```

## 5. Diferencia entre `install` y `update`
### `composer install`
Instala lo que está definido en `composer.lock`.

### `composer update`
Busca versiones nuevas compatibles y actualiza el `composer.lock`.

Para trabajar en equipo o en examen, normalmente usarás más `install` que `update`.

## 6. Qué es autoload
Laravel usa autoload PSR-4. Eso permite que Composer cargue automáticamente clases de:
- `app/`
- `database/factories/`
- `database/seeders/`
- `tests/`

## 7. Laravel Installer
El instalador de Laravel permite crear proyectos rápidamente.

Instalación global:
```bash
composer global require laravel/installer
```

Comprobar:
```bash
laravel --version
```

## 8. Crear proyecto con Laravel Installer
```bash
laravel new academia
```

## 9. Crear proyecto con Composer
Alternativa equivalente:
```bash
composer create-project laravel/laravel academia
```

## 10. Qué opción usar
### Para estudiar
`laravel new academia`

### Para entender mejor el proceso
`composer create-project laravel/laravel academia`

## 11. Dependencias que verás en este curso
- `laravel/framework`
- `laravel/breeze`
- `laravel/sanctum`
- `darkaonline/l5-swagger`
- `fakerphp/faker`
- `phpunit/phpunit`

## 12. Scripts útiles del proyecto
Muchos proyectos Laravel incluyen scripts en `composer.json` para:
- instalar
- arrancar entorno de desarrollo
- lanzar tests

## 13. Flujo real tras crear proyecto
```bash
cd academia
composer install
cp .env.example .env
php artisan key:generate
php artisan migrate
npm install
npm run dev
```

## 14. Errores típicos
### `composer: command not found`
Composer no está instalado o no está en PATH.

### `laravel: command not found`
Laravel Installer no está en PATH.

### conflicto de dependencias
A veces dos paquetes no aceptan la misma versión.

### clases no encontradas
Suele arreglarse con:
```bash
composer dump-autoload
```

## 15. Qué debes dominar
- qué hace Composer
- diferencia entre `install` y `update`
- cómo instalar paquetes
- cómo crear proyecto Laravel
- cómo regenerar autoload
