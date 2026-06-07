# 16 - Resultados de olimpiadas

## Preparar el codigo

Crea la rama `practica/16-olimpiadas-resultados` desde el resultado del ejercicio 15.

## Notas

- Este bloque es independiente en entidad, pero usa lo aprendido de migraciones, seeders, controladores y API.
- El endpoint se probara por API.
- Los datos se generaran con seeder o factory.

## Ejercicios

1. Tabla de resultados cacheados

Crea `resultados_olimpiadas_cache`:

```text
id                    bigint autoincremental
grado                 varchar(2) nullable
lastname              varchar(100) default ''
firstname             varchar(100) default ''
id_prueba             bigint default 0
maxpuntuacion          decimal(10,5) nullable
MomentoConsecucion     datetime nullable
penalizaciones         bigint default 0
TiempoFinal            datetime nullable
nombrePrueba           varchar(255) nullable
updated_at             timestamp nullable
created_at             timestamp nullable
```

2. Datos semilla

Genera 30 registros.

Reglas:

```text
grado: GM o GS
maxpuntuacion: 0, 33, 66 o 100
MomentoConsecucion: fecha del 13 de mayo
penalizaciones: entre 0 y 5
TiempoFinal: MomentoConsecucion + 30 segundos por penalizacion
```

Pruebas:

```text
GM: Hardware, Sistemas, Redes Locales
GS: Programacion, Bases de datos, Redes Locales, Sistemas, Lenguajes de Marcas
```

3. Endpoint mi puesto

Crea:

```text
GET /miPuesto
```

Parametro:

```text
nombreCompleto = firstname + espacio + lastname
```

Respuesta:

```json
{
  "parciales": [
    {
      "nombrePrueba": "Programacion",
      "TiempoFinal": "2026-05-13 10:30:00",
      "posicion": 1
    }
  ],
  "global": {
    "grado": "GS",
    "posicion": 2
  }
}
```

Para la clasificacion global solo cuentan pruebas con `maxpuntuacion = 100`.

## Comprobacion

Busca un participante generado por el seeder y consulta `/miPuesto?nombreCompleto=Nombre Apellido`.
