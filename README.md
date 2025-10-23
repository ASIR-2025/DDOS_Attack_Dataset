# DDOS Attack Dataset Stadistics

Este repositorio es un proyecto sobre el analisis estadistico de un dataset orientado a un ataque DDOS.

-------------------------------------------------------------------------------------------------------
Los integrantes de este proyecto lo conforman:
-  Javier
-  Milton
-  Diego
-------------------------------------------------------------------------------------------------------
La tecnologias a usar son:
- Python

Las librerias a usar son:
- numpy
- pandas
- matplotlib.pyplot
- seaborn
-------------------------------------------------------------------------------------------------------
# INFORMACION DEL DATASET
https://www.kaggle.com/datasets/shayalvaghasiya/ddos-sdn?resource=download

- dt: Generalmente representa la marca de tiempo (datetime) en que ocurrió el evento o captura del dato.
- switch: Puede referirse al identificador del switch de red donde se capturó el paquete o flujo.
- src: Dirección IP de origen (source IP).
- dst: Dirección IP de destino (destination IP).
- pktcount: Número total de paquetes en un flujo o intervalo de tiempo.
- bytecount: Número total de bytes transferidos en ese flujo o intervalo.
- dur: Duración del flujo o sesión en segundos (o la unidad de tiempo que uses).
- dur_nsec: Duración con mayor precisión en nanosegundos (parte fraccionaria de dur).
- tot_dur: Duración total acumulada o alguna duración combinada de múltiples flujos o sesiones.
- flows: Cantidad de flujos en un intervalo o segmento de tiempo.
- packetins: Paquetes entrantes (inbound packets).
- pktperflow: Promedio de paquetes por flujo (packet count / number of flows).
- byteperflow: Promedio de bytes por flujo (byte count / number of flows).
- pktrate: Tasa de paquetes, puede ser paquetes por segundo u otra unidad de tiempo.
- Pairflow: Probablemente representa un identificador de flujo par (bidireccional), por ejemplo combinación src-dst y dst-src.
- Protocol: Protocolo de transporte o red usado (TCP, UDP, ICMP, etc.).
- port_no: Número de puerto asociado (generalmente el puerto de destino o fuente).
- tx_bytes: Bytes transmitidos (transmitted bytes).
- rx_bytes: Bytes recibidos (received bytes).
- tx_kbps: Kilobits por segundo transmitidos (tasa de transmisión).
- rx_kbps: Kilobits por segundo recibidos (tasa de recepción).
- tot_kbps: Total de kilobits por segundo (tx_kbps + rx_kbps).

-------------------------------------------------------------------------------------------------------
# TX_BYTES VS RX_BYTES
- Permite ver cómo cambia el volumen de bytes transmitidos y recibidos a lo largo del tiempo/índice.
- Tipo de grafico: De lineas
<img width="935" height="642" alt="image" src="https://github.com/user-attachments/assets/3ff44fd3-3582-4403-9dcb-bfda43ec0e2f" />


-------------------------------------------------------------------------------------------------------
# Histograma de PKRate
- Muestra a distribución de tasas de paquetes entre los flujos.
- Por qué es útil: Un DDoS suele tener tasas anormalmente altas. Este gráfico te ayuda a ver si hay valores extremos (outliers).
- Grafico: Histograma
<img width="441" height="342" alt="image" src="https://github.com/user-attachments/assets/a6ec3014-c735-4eb1-84b6-d17a4213b824" />

-------------------------------------------------------------------------------------------------------
# pktcount vs bytecount
- Muestra la relación entre número de paquetes y cantidad de datos transferidos por flujo.
- Por qué es útil: En ataques, puede haber muchos paquetes con pocos bytes (como pings o SYNs). Te ayuda a ver patrones anómalos
- Grafico: Scatter plot
<img width="639" height="411" alt="image" src="https://github.com/user-attachments/assets/b2e041d7-3fd9-4a67-80e7-d26aa5ff6672" />

-------------------------------------------------------------------------------------------------------
# Cantidad de flujos por Protocol
- Muestra cuántos flujos se han realizado por cada protocolo (TCP, UDP, ICMP, etc.).
- Por qué es útil: Algunos ataques se basan en protocolos específicos (ej. UDP flood, ICMP flood). Un pico en un protocolo puede indicar ataque.
- Tipo de gráfico: Lineal
  
<img width="769" height="408" alt="image" src="https://github.com/user-attachments/assets/dcb724a4-071e-4001-bf08-ffdf6ae994f5" />

-------------------------------------------------------------------------------------------------------
# Heatmap de IPs origen (src) vs IPs destino (dst)
Muestra la frecuencia de comunicación entre pares de IPs.
Por qué es útil: En un DDoS, muchas IPs de origen apuntan a una sola IP destino. Esto se ve claramente en un heatmap.
Tipo de gráfico: Mapa de calor (heatmap) de conteo.

<img width="528" height="479" alt="imagen" src="https://github.com/user-attachments/assets/24f1c48f-c125-4587-ab00-e58f43d6d1e7" />


-------------------------------------------------------------------------------------------------------
# tot_kbps a lo largo del tiempo
- Muestra el uso total del ancho de banda (tx + rx) en el tiempo.
- Por qué es útil: Un DDoS suele generar picos repentinos de tráfico. Este gráfico te permite ver esos momentos críticos.
-Tipo de grafico: Line plot

<img width="445" height="340" alt="image" src="https://github.com/user-attachments/assets/0fa6ded6-57ea-402b-9ae3-2c52b8307221" />
