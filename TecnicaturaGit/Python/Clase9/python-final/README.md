# Hoy vamos a hacer actividad en Python en un día como programadores

> En este caso vamos a hacer lo que hace PyCharm por nosotros; si querés saber más, investigá utilizando el tutor de IA para profundizar en entornos virtuales de Python.

**1. Abrir la terminal de Git Bash o la terminal en Linux; en Windows debe ejecutarse con permisos de administrador.**

**2. Creamos una carpeta o directorio:**

```sh
mkdir python-final
```

**3. Entramos en ella:**

```sh
cd python-final
```

**4. Iniciamos el repositorio:**

```sh
git init
```

**5. Creamos un archivo:**

```sh
touch finales.py
```

**6. Abrimos VSC:**

```sh
code .
```

**7. En terminal ingresamos el comando para saber la versión de Python que tenemos instalada:**

```sh
python -V
python3 -V
```

**8. Creamos el entorno virtual en Python:**

```sh
python3 -m venv venv  # Creamos el entorno virtual
```

**9. Activamos el entorno virtual:**

```sh
source venv/bin/activate  # Activamos el entorno virtual en Linux
venv\Scripts\activate  # En Windows
```

**10. Hacemos actualización del pip de Python**

```sh
python3 -m pip install --upgrade pip  # Actualizamos el pip
```

**11. Investigar: ¿Qué es el pip y por qué lo actualizamos?**

### **Se actualiza porque las nuevas versiones suelen incluir:**
> Corrección de errores.
> Mejoras de seguridad.
> Mayor compatibilidad con versiones nuevas de Python.
> Mejor rendimiento al instalar paquetes.
> Soporte para nuevas funciones y formatos de paquetes.

**12. Hacer el primer commit de este trabajo y unirlo al repositorio remoto.**

```sh
git add .
git commit -m "Primer commit"
# Conectar al remoto (reemplazar <URL>) y subir:
git remote add origin <URL>
git push -u origin main
```

**13. Enviar el enlace del repositorio remoto; el repositorio debe tener un README.md con todos los detalles de los comandos y la respuesta al punto 11.**