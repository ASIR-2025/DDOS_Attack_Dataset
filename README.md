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
