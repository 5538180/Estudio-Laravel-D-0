# 06. Crear el primer proyecto Laravel

## 1. Dos formas de crear el proyecto
### Opción A. Laravel Installer
```bash
laravel new academia
```

### Opción B. Composer
```bash
composer create-project laravel/laravel academia
```

## 2. Entrar al proyecto
```bash
cd academia
```

## 3. Preparar entorno
Si no existe `.env`:
```bash
cp .env.example .env
```

Generar clave:
```bash
php artisan key:generate
```

## 4. Base de datos con SQLite
Crear archivo:
```bash
touch database/database.sqlite
```

En `.env`:
```env
DB_CONNECTION=sqlite
DB_DATABASE=/ruta/completa/a/tu/proyecto/database/database.sqlite
```

## 5. Migrar
```bash
php artisan migrate
```

## 6. Arrancar servidor
```bash
php artisan serve
```

## 7. Instalar dependencias frontend
```bash
npm install
npm run dev
```

## 8. Comprobaciones mínimas
Debes ser capaz de:
- abrir la home de Laravel
- migrar sin errores
- levantar Vite

## 9. Qué entiendes aquí
- estructura mínima de un proyecto Laravel
- `.env`
- clave de la app
- conexión a base de datos
- migraciones iniciales
- servidor de desarrollo

## 10. Flujo recomendado real
```bash
laravel new academia
cd academia
cp .env.example .env
php artisan key:generate
touch database/database.sqlite
php artisan migrate
npm install
npm run dev
php artisan serve
```
