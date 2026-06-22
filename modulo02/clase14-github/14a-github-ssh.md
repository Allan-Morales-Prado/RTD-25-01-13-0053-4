# ¿Para qué sirve usar SSH en GitHub?

Cuando trabajas con GitHub, hay dos formas principales de conectar tu computadora con los repositorios remotos: **HTTPS** y **SSH**. Entender SSH te hará la vida mucho más fácil como desarrollador.

## 🎯 El problema que resuelve SSH

Imagina que cada vez que quieras subir (`push`) o descargar (`pull`) código de GitHub, tuvieras que escribir tu usuario y contraseña (o un token). Es tedioso, lento y poco seguro .

**SSH elimina ese problema.** Con SSH, configuras tu computadora una sola vez y luego puedes interactuar con GitHub sin volver a escribir credenciales .

## 🔑 ¿Cómo funciona? La analogía del candado

SSH funciona con un sistema de **dos claves** que se generan juntas :

1.  **Clave pública**: Es como un **candado**. Puedes ponerla en GitHub, en tu servidor, donde quieras. Es segura de compartir .
2.  **Clave privada**: Es como la **única llave** que abre ese candado. Esta **NUNCA se comparte** y debe estar solo en tu computadora .

Cuando intentas conectarte a GitHub, este te envía un "reto" cifrado con tu candado (clave pública). Tu computadora lo descifra con tu llave (clave privada) y lo devuelve. ¡Así GitHub sabe que realmente eres tú! 

## ✅ Ventajas de SSH para estudiantes y desarrolladores

| Ventaja | Explicación |
| :--- | :--- |
| **Sin contraseñas repetitivas** | Después de la configuración inicial, no tienes que escribir usuario/contraseña ni tokens cada vez que usas `git push` o `git pull` . |
| **Más seguro** | Las claves SSH son mucho más difíciles de robar que una contraseña . Además, GitHub elimina automáticamente las claves SSH que no se usan por un año por seguridad . |
| **Sin fechas de vencimiento** | A diferencia de los tokens de acceso personal (PAT) que caducan, las claves SSH son permanentes hasta que tú decidas revocarlas . |

## 🆚 SSH vs HTTPS en GitHub

| Característica | SSH | HTTPS |
| :--- | :--- | :--- |
| **Autenticación** | Clave pública/privada (candado y llave)  | Usuario + contraseña o token  |
| **Configuración inicial** | Un paso extra (generar claves y subir la pública a GitHub)  | Más simple, solo usar las credenciales |
| **Uso diario** | No pide credenciales nunca  | Pide credenciales en cada operación (o requiere caché) |
| **Recomendado para** | Trabajo diario y frecuente con repositorios  | Clonados rápidos o entornos con firewalls restrictivos  |

## 🚀 ¿Cuándo usar SSH?

**Úsalo siempre que vayas a trabajar de forma habitual con un repositorio.** Es el estándar en la industria para desarrolladores porque ahorra tiempo y es más seguro .

Para tu día a día como desarrollador, la comodidad y seguridad de SSH lo convierten en la opción preferida .