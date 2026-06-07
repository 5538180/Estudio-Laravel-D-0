# 14 - Empresas, tokens de acceso y correos

## Preparar el codigo

Crea la rama `practica/14-empresas-email` desde el resultado del ejercicio 13.

Configura envio de correo en `.env`. Para examen puedes usar `MAIL_MAILER=log`.

## Notas

- Cada empresa debe estar asociada a un usuario.
- El token de empresa debe ser unico.
- Los correos se implementan con Mailables.

## Ejercicios

1. Modelo Empresa

Revisa o crea los campos:

```text
id        bigint autoincremental
user_id   unsignedBigInteger
nombre    string
token     string unique
timestamps
```

Al crear una empresa se debe crear o asociar un usuario con rol `empresa`.

2. Correo de registro

Crea o revisa el Mailable `NuevaEmpresaRegistrada`.

Al registrar una empresa debe enviarse un correo a la direccion de la empresa con:

```text
destinatario: email de la empresa
asunto: Nueva empresa registrada
datos: nombre de empresa y enlace de acceso
```

El enlace de acceso sera:

```text
/api/v1/empresas/acceso/{token}
```

3. Acceso por token

Crea o revisa:

```text
GET /api/v1/empresas/acceso/{token}
```

Si el token existe, devolvera datos basicos de empresa y token API. Si no existe, devolvera `404`.

4. Correos relacionados con curriculo

Prepara Mailables para:

```text
EmpresaQuiereVerTuCurriculo
EmpresaAutorizadaVerCurriculo
EmpresaAccesoRegistrado
```

## Comprobacion

Registra una empresa y revisa `storage/logs/laravel.log` si usas `MAIL_MAILER=log`.
