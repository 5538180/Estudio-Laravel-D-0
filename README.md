# DWES - Practica acumulativa de examenes

Repositorio de practica para 0613 - Desarrollo Web en Entorno Servidor.

La base tecnica es el proyecto `marcapersonalFP23_24`, porque ya usa la misma forma de trabajar vista durante el curso: Laravel 10, Breeze/Sanctum, rutas web y API, controladores, migraciones, modelos Eloquent, seeders, factories, Resources, middleware, policies, Mailables, subida de ficheros y consumo de servicios externos.

Este repositorio no contiene soluciones de examen. Contiene enunciados acumulativos para practicar. Cada ejercicio deja preparada una parte que se usa en los ejercicios siguientes.

## Como usarlo

1. Lee [enunciados/00_preparacion.md](enunciados/00_preparacion.md).
2. Crea una rama por ejercicio siguiendo el formato indicado.
3. Empieza por el ejercicio 01 y no saltes dependencias.
4. Al terminar cada ejercicio, ejecuta migraciones, seeders y pruebas manuales con navegador o cliente API.
5. Haz commit de tu solucion antes de pasar al siguiente ejercicio.

## Enunciados

El indice completo esta en [enunciados/README.md](enunciados/README.md).

La vision final del proyecto esta en [docs/proyecto_final_mermaid.md](docs/proyecto_final_mermaid.md).

El contrato final de tablas, endpoints y patrones esta en [docs/contrato_final.md](docs/contrato_final.md).

Plantillas utiles:

- [Checklist de ejercicio](plantillas/checklist_ejercicio.md)
- [Plantilla de Pull Request](plantillas/pull_request.md)

## Reglas de practica

- No copies soluciones de ramas antiguas.
- No uses inteligencia artificial para resolver el codigo si estas simulando examen.
- No cambies nombres de tablas, rutas o modelos salvo que el enunciado lo pida.
- Mantén la sintaxis y estilo del curso: `Route::apiResource`, controladores por recurso, Resources, `auth:sanctum`, Policies, Mailables y seeders.
- Cada ejercicio debe quedar reproducible con `php artisan migrate:fresh --seed`.
- Si un ejercicio ya esta implementado en la base, rehacelo en una rama nueva partiendo del punto anterior y usa el enunciado como contrato.

## Arranque habitual

```bash
cp .env.example .env
composer install
npm install
php artisan key:generate
php artisan migrate:fresh --seed
php artisan serve
```

Para el frontend:

```bash
npm run dev
```
