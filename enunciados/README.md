# Indice de practica acumulativa

Realiza los ejercicios en orden. Cada bloque se apoya en tablas, modelos, rutas o permisos creados anteriormente.

| Numero | Enunciado | Bloque |
| --- | --- | --- |
| 00 | [Preparacion](00_preparacion.md) | Entorno, ramas y entrega |
| 01 | [Vistas parciales y rutas con controlador](01_rutas_vistas.md) | Rutas, controlador y partials |
| 02 | [Controladores web y formularios](02_controladores_formularios.md) | Controladores, CSRF, PUT |
| 03 | [Proyectos, migraciones, modelos y seeders](03_proyectos_bd.md) | Base de datos |
| 04 | [Usuarios, perfiles y autenticacion](04_usuarios_auth.md) | Usuarios y auth |
| 05 | [Familias profesionales y ciclos](05_familias_ciclos.md) | Catalogos |
| 06 | [Curriculos, actividades y reconocimientos](06_curriculos_actividades_reconocimientos.md) | Entidades centrales |
| 07 | [Subida de ficheros web](07_ficheros_web.md) | Storage y validacion |
| 08 | [API REST con Resources](08_api_resources.md) | API v1 |
| 09 | [React-admin, filtros y cabeceras](09_reactadmin_filtros.md) | Adaptacion frontend |
| 10 | [Relaciones Eloquent](10_relaciones.md) | Uno a muchos y muchos a muchos |
| 11 | [Tokens, login API y usuario autenticado](11_tokens_api.md) | Sanctum |
| 12 | [Roles, Policies y autorizacion](12_policies_roles.md) | Autorizacion |
| 13 | [Ficheros de proyecto y API externa GitHub](13_ficheros_github.md) | Upload + servicio externo |
| 14 | [Empresas, tokens de acceso y correos](14_empresas_email.md) | Mailables |
| 15 | [Permisos de descarga de curriculo](15_permisos_descarga.md) | Segunda convocatoria |
| 16 | [Resultados de olimpiadas](16_olimpiadas_resultados.md) | Examen tipo ranking |
| 17 | [ePortfolio, evidencias y evaluaciones](17_eportfolio_evaluaciones.md) | Recursos anidados |
| 18 | [Backend EAC y progreso del estudiante](18_backend_eac.md) | Evaluacion API |
| 19 | [Revision final acumulativa](19_revision_final.md) | Simulacro completo |

## Flujo recomendado de ramas

```bash
git checkout master
git checkout -b practica/01-rutas-vistas
```

Cuando termines:

```bash
git add .
git commit -m "Practica 01 rutas y vistas"
git checkout -b practica/02-controladores-formularios
```

No mezcles varios ejercicios en el mismo commit si estas practicando para examen.
