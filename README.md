
# Comunicación indirecta - Emulador Iot

Consigna:
Control de Eventos en IoT, los dispositivos pueden publicar eventos, y los servidores o aplicaciones
suscritas pueden recibir y actuar en consecuencia. Esto se utiliza en aplicaciones de automatización y
monitorización.
Se pide:
1. Emular el ecosistema de dispositivos del tipo Internet de las Cosas (IoT) y clientes interesados
en valores censados y transmitidos por los mismos.
Para emular un dispositivo IoT considere la creación de un proceso que emita ciertos valores, en
períodos regulares, como si de un sensor se tratase.
Para emular los clientes considere la creación de procesos. Cada cliente puede estar interesado en uno o
más valores.


## Instalación

Descargar https://www.apache.org/dyn/closer.cgi?filename=/activemq/5.18.3/apache-activemq-5.18.3-bin.zip&action=download

```bash
  cd [activemq_install_dir]
```

Donde [activemq_install_dir] es donde esté descompmrimido ActiveMQ. Por ejemplo c:\Archivos de programa\ActiveMQ-5.x.
Después


```bash
  bin\activemq start
```
    

# Ver la interfaz de administrador
Abrir
URL: http://127.0.0.1:8161/admin/

Login: admin

Passwort: admin

# Para modificar el ip del servidor en caso que este configurado como localhost

Ubicar y abrir el archivo de configuración principal de Apache ActiveMQ se llama activemq.xml, en la carpeta conf. 

Modificar la dirección IP localhost y el puerto 61616. Debes cambiar localhost a la dirección IP o el nombre de host de la máquina desde la que queres que ActiveMQ escuche las conexiones. Para escuchar en todas las interfaces de red, cambia de localhost a 0.0.0.0:


```bash
<transportConnector name="openwire" uri="tcp://0.0.0.0:61616?maximumConnections=1000&amp;wireFormat.maxFrameSize=104857600"/>
```


# Instalar stomp
 Para poder usar ActiveMQ con python

```bash
  pip install stomp.py
```

En dos terminales diferentes ejecutar

```bash
  python iot.py
```


```bash
  pyton cliente.py
```
