# Contrato final de practica

Este documento resume lo que deberia existir al terminar todos los ejercicios. No es una solucion; es una lista de comprobacion del proyecto completo.

## Tablas principales

```text
users
proyectos
familias_profesionales
ciclos
curriculos
actividades
reconocimientos
competencias
idiomas
users_ciclos
users_competencias
users_idiomas
proyectos_ciclos
participantes_proyectos
competencias_actividades
empresas
permisos_descargas
resultados_olimpiadas_cache
evaluaciones
criterios_evaluacion
calificaciones
personal_access_tokens
```

## Endpoints API esperados

```text
POST   /api/v1/tokens
DELETE /api/v1/tokens
GET    /api/v1/user

GET    /api/v1/users
GET    /api/v1/proyectos
GET    /api/v1/familias_profesionales
GET    /api/v1/ciclos
GET    /api/v1/competencias
GET    /api/v1/idiomas
GET    /api/v1/curriculos
GET    /api/v1/actividades
GET    /api/v1/reconocimientos
GET    /api/v1/empresas

GET    /api/v1/empresas/acceso/{token}
POST   /api/v1/curriculos/{id}/permisoDescarga
PUT    /api/v1/curriculos/{idEmpresa}/permitirDescarga

GET    /miPuesto

GET    /api/v1/evidencias/{id}/evaluaciones
POST   /api/v1/evidencias/{id}/evaluaciones
GET    /api/v1/users/{id}/evidencias
GET    /api/v1/users/{id}/asignaciones-revision

GET    /api/v1/estudiante/progreso
POST   /api/v1/docente/calificaciones
```

## Patrones tecnicos que deben aparecer

```text
Route::get
Route::prefix
Route::apiResource
where('id', '[0-9]+')
middleware('auth')
middleware('auth:sanctum')
FormRequest o validate
Eloquent belongsTo, hasMany, belongsToMany
Resource::collection
Mail::to(...)->send(...)
Storage::disk('public')
Policies registradas
Seeders ejecutables
```
