# 08. Comandos php artisan

`artisan` es la consola de Laravel. Se usa para generar código, ejecutar migraciones, limpiar cachés, lanzar tests y más.

## 1. Ver ayuda
```bash
php artisan
```

## 2. Levantar servidor
```bash
php artisan serve
```

## 3. Migraciones
Ejecutar migraciones:
```bash
php artisan migrate
```

Revertir la última tanda:
```bash
php artisan migrate:rollback
```

Reiniciar todas:
```bash
php artisan migrate:fresh
```

Reiniciar y sembrar datos:
```bash
php artisan migrate:fresh --seed
```

## 4. Generar modelos
Modelo simple:
```bash
php artisan make:model Curso
```

Modelo con migración:
```bash
php artisan make:model Curso -m
```

Modelo con migración, factory y seeder:
```bash
php artisan make:model Curso -mfs
```

## 5. Generar controladores
Controlador normal:
```bash
php artisan make:controller CursoController
```

Controlador resource:
```bash
php artisan make:controller CursoController --resource
```

Controlador API:
```bash
php artisan make:controller Api/V1/CursoController --api
```

## 6. Requests
```bash
php artisan make:request StoreCursoRequest
```

## 7. Resources
```bash
php artisan make:resource CursoResource
```

Colección de recursos:
```bash
php artisan make:resource CursoCollection
```

## 8. Seeders y factories
```bash
php artisan make:seeder CursoSeeder
php artisan make:factory CursoFactory
```

## 9. Tests
```bash
php artisan make:test CursoTest
php artisan make:test CursoApiTest --unit
php artisan test
```

## 10. Tinker
Permite probar Eloquent y consultas rápidamente.
```bash
php artisan tinker
```

## 11. Limpiar cachés
```bash
php artisan config:clear
php artisan cache:clear
php artisan route:clear
php artisan view:clear
```

## 12. Publicar assets o configuración de paquetes
Algunos paquetes lo necesitan.
```bash
php artisan vendor:publish
```

## 13. Comandos que debes dominar para examen
- `serve`
- `make:model -m`
- `make:controller`
- `make:request`
- `make:resource`
- `make:seeder`
- `make:factory`
- `migrate`
- `migrate:fresh --seed`
- `test`
- `tinker`
