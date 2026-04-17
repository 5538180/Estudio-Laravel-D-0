# 04. Contexto de entidades

Este proyecto usa un dominio sencillo de **academia** para que puedas aprender Laravel sin pelearte con reglas de negocio demasiado complejas.

## 1. Centro
Representa la academia o centro principal.

Sirve para agrupar usuarios, aulas y cursos.

## 2. Usuario
Representa una persona que accede al sistema.

En un sistema real podría ser:
- administrador
- profesor
- alumno

Aquí lo usamos como núcleo para autenticación y relaciones generales.

## 3. Perfil
Guarda información ampliada del usuario:
- teléfono
- dirección
- bio

Se separa del usuario para practicar una relación 1 a 1.

## 4. Aula
Representa una clase o sala física.

## 5. Horario
Representa un horario asociado a un aula.

Aunque en una app real un aula podría tener muchos horarios, aquí también sirve para practicar una segunda variante de relación sencilla.

## 6. Curso
Representa una formación concreta.

Ejemplos:
- Laravel básico
- PHP intermedio
- Bases de datos

## 7. Lección
Cada curso se divide en lecciones.

Ejemplo:
- Introducción a rutas
- Modelos Eloquent
- Migraciones

## 8. Tarea
Representa ejercicios o actividades.

Ejemplo:
- crear modelo Curso
- hacer migración de alumnos
- probar relación belongsToMany

## 9. Alumno
Representa a un estudiante inscrito en cursos o talleres.

## 10. Taller
Representa una actividad paralela a los cursos.

Ejemplo:
- Taller de Git
- Taller de testing

## 11. Comentario
Representa mensajes escritos por usuarios en cursos o tareas.

Se usa para practicar polimorfismo.

## 12. Etiqueta
Sirve para clasificar cursos o tareas.

Ejemplos:
- urgente
- repaso
- examen

## 13. Foto
Sirve para asociar una imagen a distintos modelos.

Ejemplo:
- avatar de usuario
- portada de curso

## 14. Categoría
Sirve para practicar jerarquías.

Ejemplo:
- Programación
  - PHP
  - Laravel

## 15. Por qué este dominio es bueno para examen
Porque permite practicar:
- autenticación
- CRUD
- Blade
- API
- relaciones Eloquent
- seeders
- tests

sin depender de una lógica demasiado abstracta.
