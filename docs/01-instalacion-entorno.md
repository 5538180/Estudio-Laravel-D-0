# 01. Instalación del entorno en Debian

Este documento cubre la instalación base para trabajar con Laravel y PHP en **Debian**.

La idea es que puedas arrancar desde cero y comprobar si tu equipo está listo para:

- PHP
- Composer
- Node.js y npm
- Git
- SQLite o MySQL/MariaDB
- Laravel Installer

---

## 1. Qué necesitas realmente

Para trabajar cómodo con Laravel en Debian necesitas, como mínimo:

- **PHP 8.2 o superior**
- extensiones habituales de PHP
- **Composer**
- **Git**
- **Node.js + npm**
- una base de datos
- opcionalmente **Laravel Installer**

Laravel 12 requiere PHP moderno. En los proyectos revisados se usa `php: ^8.2` y `laravel/framework: ^12.0`. Además, también aparecen `laravel/sanctum`, `laravel/breeze` y `darkaonline/l5-swagger`. fileciteturn8file0 fileciteturn9file0

---

## 2. Actualizar paquetes

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 3. Instalar Git

```bash
sudo apt install -y git
```

Comprobar:

```bash
git --version
```

---

## 4. Instalar PHP y extensiones necesarias

Ejemplo base en Debian:

```bash
sudo apt install -y php php-cli php-common php-mbstring php-xml php-curl php-zip php-sqlite3 php-mysql php-bcmath php-intl unzip curl
```

Comprobar versión:

```bash
php -v
```

Comprobar módulos:

```bash
php -m
```

Módulos especialmente habituales en Laravel:

- `mbstring`
- `xml`
- `curl`
- `zip`
- `pdo_sqlite`
- `pdo_mysql`
- `bcmath`
- `intl`

---

## 5. Instalar Composer

Instalación rápida desde apt:

```bash
sudo apt install -y composer
```

Comprobar:

```bash
composer --version
```

Si en algún momento falla o la versión es vieja, puedes reinstalar Composer manualmente, pero para estudiar y trabajar en Debian normalmente esta vía es suficiente.

---

## 6. Instalar Node.js y npm

Laravel usa Vite para el frontend. Aunque tu foco sea backend, necesitas `npm` para proyectos con Breeze y para compilar assets.

```bash
sudo apt install -y nodejs npm
```

Comprobar:

```bash
node -v
npm -v
```

---

## 7. Base de datos

### Opción A. SQLite

Es la opción más sencilla para practicar.

```bash
touch database.sqlite
```

O dentro del proyecto Laravel:

```bash
touch database/database.sqlite
```

Ventajas:

- no necesitas servidor aparte
- ideal para prácticas rápidas
- muy útil para test y examen

### Opción B. MySQL / MariaDB

Si quieres practicar como en un entorno más real:

```bash
sudo apt install -y mariadb-server mariadb-client
```

Comprobar servicio:

```bash
sudo systemctl status mariadb
```

Entrar:

```bash
sudo mysql
```

Crear base de datos:

```sql
CREATE DATABASE academia_laravel;
```

---

## 8. Instalar Laravel Installer

Puedes crear proyectos con Composer o con el instalador de Laravel.

### Instalar con Composer global

```bash
composer global require laravel/installer
```

Añadir al PATH si hace falta. En Debian muchas veces se usa:

```bash
echo 'export PATH="$HOME/.config/composer/vendor/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

O en algunos sistemas:

```bash
echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Comprobar:

```bash
laravel --version
```

---

## 9. Comprobación rápida del entorno

Ejecuta:

```bash
php -v
git --version
composer --version
node -v
npm -v
laravel --version
```

Si todo responde bien, ya tienes el entorno mínimo listo.

---

## 10. Errores típicos

### `composer: command not found`
No está instalado o no está en el PATH.

### `laravel: command not found`
El instalador global no está en el PATH.

### `Class "PDO" not found` o problemas de base de datos
Faltan extensiones como `php-sqlite3` o `php-mysql`.

### Error con `zip`
Falta `php-zip`.

### `npm` o `node` no existen
No está instalado Node.js.

---

## 11. Recomendación de estudio

Para aprender backend sin pelearte demasiado con el entorno:

1. empieza con **SQLite**
2. usa **Git** desde el principio
3. crea proyectos con `laravel new` o `composer create-project`
4. instala Breeze y Sanctum en un segundo paso

---

## 12. Qué deberías saber hacer antes de seguir

Antes de pasar al siguiente documento deberías ser capaz de:

- comprobar la versión de PHP
- comprobar Composer
- comprobar Git
- comprobar Node.js
- crear una base SQLite
- instalar Laravel Installer

Si esto falla, el resto del flujo de Laravel se complica mucho.
