
## Descripción:
How to automate tasks to run at intervals on linux servers?Use ssh to connect to this server:

```
Server: saturn.picoctf.net
Port: 52990
Username: picoplayer 
Password: ekj2GJuiv4
```

**Hints:**
1.(None)

## Solución:
- Para resolver este reto, tuve que googlear la pregunta de la descripción `How to automate tasks to run at intervals on linux servers?` lo que me dio como respuesta `Cron`.
- Por lo que investigando en varias fuentes que es cron y donde se ubicaba, encontre que "Estas tareas en Linux se conocen como **trabajos cron (Crontab).** Los trabajos cron se utilizan para **la automatización de tareas** que son útiles y ayudan a simplificar la ejecución de tareas repetitivas y, a veces, mundanas."
- Por lo que indagando mas, encontre que lo que necesitaba era el archivo `crontab`, que esta ubicado en `/etc`.
- Con el siguinete comando encontre la flag: `cat /etc/crontab`

```bash
icoplayer@challenge:/etc$ cat crontab 
# picoCTF{Sch3DUL7NG_T45K3_L1NUX_9d5cb744}
```

### Flag: picoCTF{Sch3DUL7NG_T45K3_L1NUX_9d5cb744}

## Notas adicionales:
#### El archivo Crontab
Un archivo crontab, también conocido como **tabla cron** , es un archivo de texto simple que contiene reglas o comandos que especifican el intervalo de tiempo de ejecución de una tarea. Hay dos categorías de archivos crontab:


## Referencias:
- [# Cómo automatizar tareas en Linux usando Crontab](https://www.linuxtechi.com/schedule-automate-tasks-linux-cron-jobs/)