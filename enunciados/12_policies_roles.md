# 12 - Roles, Policies y autorizacion

## Preparar el codigo

Crea la rama `practica/12-policies-roles` desde el resultado del ejercicio 11.

## Notas

- Roles validos: `admin`, `docente`, `estudiante`, `empresa`.
- Usa Policies cuando el permiso dependa del modelo.
- Usa middleware cuando la restriccion sea transversal.

## Ejercicios

1. Reglas por entidad

Implementa las reglas:

```text
Actividad:
  store: docente
  update/destroy: docente propietario

Ciclo, Competencia, FamiliaProfesional, Idioma:
  store/update/destroy: admin

Curriculo:
  store: estudiante
  update/destroy: estudiante propietario

Empresa:
  store/update: docente
  destroy: propietario o admin

Proyecto:
  store: docente
  update/destroy: tutor propietario

Reconocimiento:
  store: estudiante
  update/destroy: propietario
```

2. Acciones publicas

Las acciones `index` y `show` de los recursos principales deben poder consultarse sin autenticacion salvo que el controlador ya tenga una restriccion justificada.

3. Asignacion automatica de propietario

Cuando un usuario cree curriculo, actividad, proyecto o reconocimiento, el controlador debe asignar automaticamente el usuario propietario cuando proceda.

4. Respuestas

Una accion no autorizada debe devolver `403` en API. Una accion sin token debe devolver `401`.

## Comprobacion

Prueba la misma accion con usuario admin, docente, estudiante y empresa.
