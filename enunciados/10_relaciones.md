# 10 - Relaciones Eloquent

## Preparar el codigo

Crea la rama `practica/10-relaciones` desde el resultado del ejercicio 09.

## Notas

- Las tablas pivote deben tener claves foraneas.
- Evita duplicados en relaciones muchos a muchos.
- Los seeders deben crear relaciones suficientes para probar la API.

## Ejercicios

1. Usuarios y catalogos

Revisa o crea las relaciones:

```text
users <-> ciclos
users <-> competencias
users <-> idiomas
users <-> proyectos
```

2. Actividades y competencias

Relaciona actividades y competencias mediante tabla pivote.

3. Proyectos y ciclos

Relaciona proyectos y ciclos. Un proyecto puede estar asociado a varios ciclos y un ciclo a varios proyectos.

4. Participantes de proyecto

Relaciona usuarios y proyectos como participantes. Mantén separado el tutor del proyecto y los participantes.

5. Resources con relaciones

Los Resources de detalle deben incluir relaciones principales:

```text
UserResource: ciclos, competencias, idiomas
ProyectoResource: tutor, ciclos, participantes
ActividadResource: competencias
CurriculoResource: usuario
ReconocimientoResource: estudiante, actividad, docente_validador
```

## Comprobacion

Ejecuta seeders y consulta un detalle de usuario y de proyecto desde la API. Deben aparecer relaciones.
