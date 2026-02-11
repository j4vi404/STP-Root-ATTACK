# STP Root Attack
Network Security Tool  
![Python](https://img.shields.io/badge/Python-3.7%2B-blue)

Herramienta automatizada para demostración de ataques STP Root Bridge Manipulation en entornos de laboratorio controlados

## 📋 Tabla de Contenidos
- [Objetivo del Script](#-objetivo)
- [Características Principales](#características)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Topología de Red](#-topología-de-red)
- [Parámetros de Configuración](#parámetros-usados)
- [Uso y Ejemplos](#uso)
- [Medidas de Mitigación](#-medidas-de-mitigación)

## 🎯 Objetivo
El objetivo de este script es simular, en un entorno de laboratorio controlado, un ataque de **STP Root Bridge Manipulation** para forzar al switch atacante a convertirse en el Root Bridge de la topología STP, permitiendo interceptar todo el tráfico de la red al posicionarse como punto central de conmutación, con fines exclusivamente educativos y de análisis de seguridad.

## 🖼️ Capturas de Pantalla
Las capturas incluidas en este repositorio documentan el proceso completo del laboratorio:

## Topología de red del escenario
  
<img width="809" height="434" alt="image" src="https://github.com/user-attachments/assets/0d6e3f83-2117-489d-8eb4-442d19b6b1cf" />

---
## Configuración STP antes del ataque
  <img width="1387" height="494" alt="image" src="https://github.com/user-attachments/assets/23f25e4f-46f5-491c-aef7-07c330992ba6" />

---

## Ejecución del ataque STP Root Attack
  
 <img width="684" height="826" alt="image" src="https://github.com/user-attachments/assets/bc516d8f-1ced-4ef4-a726-e2253d40f230" />

---
## Puerto del Switch como nuevo Root Bridge
  
<img width="1581" height="417" alt="image" src="https://github.com/user-attachments/assets/8cc99241-8aec-430d-b826-45f709096ab6" />

---
## Tráfico STP interceptado (BPDUs)
---
<img width="842" height="565" alt="image" src="https://github.com/user-attachments/assets/3a6571bc-1255-4ed0-95a0-43148281574f" />

---
## STP Root Attack - Bridge Priority Manipulation
Script de Python que utiliza Scapy para realizar ataques de manipulación del protocolo Spanning Tree Protocol (STP) enviando BPDUs maliciosos con prioridad superior para convertirse en el Root Bridge.

### Requisitos
```bash
pip install scapy
```

### Uso
```bash
git clone https://github.com/j4vi404/STP-Root-ATTACK.git
cd STP-Root-Attack
chmod +x STP.py
sudo python3 STP.py
```

## Características
🎯 **STP Root Manipulation**: Envío de BPDUs con prioridad 0 (máxima)  
🔄 **Bridge ID Spoofing**: Falsificación del Bridge ID  
⚡ **Convergencia forzada**: Fuerza reconvergencia de la topología STP  
✅ **Intercepción de tráfico**: Todo el tráfico pasa por el atacante  
✅ **Monitoreo en tiempo real**: Muestra cambios en topología STP  
📊 **Logging detallado**: Registra todos los BPDUs enviados  
🔧 **Configuración simple**: Variables fáciles de modificar  
🚨 **DoS potencial**: Puede causar loops de switching si se deshabilita

## 🔧 Configuración
Edita las siguientes variables según tu red:

```python
interface = "eth0"                    # Interfaz de red
bridge_priority = 0                   # Prioridad del bridge (0 = máxima)
bridge_mac = "00:00:00:00:00:01"     # MAC del bridge falso
root_path_cost = 0                    # Costo del path al root
hello_time = 2                        # Intervalo de Hello BPDU (segundos)
max_age = 20                          # Tiempo máximo de edad BPDU
forward_delay = 15                    # Tiempo de forward delay
```

## Notas
⚠️ **Advertencia**: Este script requiere privilegios de root para enviar tramas de capa 2.

⚠️ **Peligro de loop**: Deshabilitar STP puede causar broadcast storms y colapso de red.

⚠️ **Uso responsable**: Utiliza este script únicamente en entornos de prueba autorizados y con fines educativos.

⚠️ **Legal**: El uso no autorizado de este script puede ser ilegal. Asegúrate de tener permiso explícito.

## Cómo funciona
1. **Captura topología actual**: Escucha BPDUs para conocer el Root Bridge actual
2. **Genera BPDUs maliciosos**: Crea BPDUs con prioridad 0 (superior a cualquiera)
3. **Envío continuo**: Transmite BPDUs cada 2 segundos
4. **Elección como Root**: Los switches eligen al atacante como nuevo Root Bridge
5. **Redirección de tráfico**: Todo el tráfico inter-switch pasa por el atacante
6. **Intercepción**: Permite capturar y analizar todo el tráfico de la red

## Detección
Este ataque puede ser detectado mediante:

- Monitoreo de cambios frecuentes en Root Bridge
- Detección de prioridades STP anómalas (0 o muy bajas)
- BPDU Guard en puertos de acceso
- Root Guard en puertos uplink
- Alertas de Topology Change Notifications (TCN) excesivas
- IDS/IPS configurados para detectar BPDUs anómalos

## Autor
**ALEXIS JAVIER CRUZ MINYETE**

---

## Reporte de Seguridad
Durante la ejecución del laboratorio se identificó que la red evaluada carece de mecanismos de protección STP, lo que permitió la ejecución exitosa de un ataque de STP Root Bridge Manipulation. La ausencia de BPDU Guard, Root Guard y validación de prioridades STP representa un riesgo crítico para la estabilidad y seguridad de la red de switching.

El impacto principal del ataque es la capacidad de redirigir todo el tráfico inter-switch a través del atacante, permitiendo ataques Man-in-the-Middle masivos, captura de credenciales en tránsito y análisis completo del tráfico de la red. Adicionalmente, existe el riesgo de loops de switching si se deshabilita STP, lo que causaría un Denial of Service (DoS) completo.

En un entorno real, este tipo de vulnerabilidad podría facilitar el acceso no autorizado a información confidencial, comprometer la integridad de comunicaciones corporativas y causar interrupciones severas del servicio. La implementación de controles como BPDU Guard, Root Guard, BPDU Filter y monitoreo activo permitiría reducir considerablemente la superficie de ataque.

---
**Elementos de la red:**
- **Cloud My House**: Conexión a Internet
- **Kali Linux Atacante**: Switch malicioso con prioridad STP 0
- **SW-Cloud**: Switch de conexión a cloud
- **SW-1 (ARISTA)**: Switch con prioridad 32768 (default)
- **SW-2 (ARISTA)**: Switch con prioridad 32768 (default)
- **SW-3 (ARISTA)**: Switch con prioridad 32768 (default)
- **R-SD**: Router/Switch con prioridad 32768 (Root Bridge original)
- **PNET**: Proveedor de Internet (ISP)
- **USER**: Dispositivos finales (4 clientes)

### Tabla de Interfaces

#### Kali Linux Atacante (STP Root Malicioso)
| Interfaz | Dirección IP | Estado STP | Descripción |
|----------|--------------|------------|-------------|
| e0 | 15.0.7.2 | **Root** | Interfaz de ataque |
| e1 | Acceso Cloud | Forwarding | Conexión a Internet |

#### R-SD (Root Bridge Original)
| Interfaz | Estado STP Antes | Estado STP Después | Descripción |
|----------|------------------|---------------------|-------------|
| e0/0 | Root Port | Designated | Red interna |
| e0/1 | Designated | Designated | Uplink SW-Cloud |
| e1/0 | Designated | Designated | Conexión SW-3 |

#### SW-1 (ARISTA - Switch Principal)
| Interface | Estado STP Antes | Estado STP Después | Descripción |
|-----------|------------------|---------------------|-------------|
| e0/0 | Designated | **Root Port** | Conexión Atacante |
| e1/0 | Root Port | Designated | Uplink Cloud |
| e0/3 | Designated | Designated | Conexión SW-2 |

#### SW-2 (ARISTA - Switch Segmento Inferior)
| Interface | Estado STP Antes | Estado STP Después | Descripción |
|-----------|------------------|---------------------|-------------|
| e0/0 | Root Port | Designated | Uplink SW-1 |
| e0/2 | Designated | Designated | Usuario 1 |

#### SW-3 (ARISTA - Switch Segmento Derecho)
| Interface | Estado STP Antes | Estado STP Después | Descripción |
|-----------|------------------|---------------------|-------------|
| e0/0 | Designated | Designated | Uplink SW-Cloud |
| e0/2 | Designated | Designated | Conexión PNET |
| e0/4 | Designated | Designated | Usuario 2 |
| e1/0 | Root Port | Designated | Uplink R-SD |
| e1/1 | Designated | Designated | Usuario 3 |
| e1/2 | Designated | Designated | Usuario 3 (secundaria) |
| e1/3 | Designated | Designated | Usuario 3 (terciaria) |

---

## Parámetros Usados

### Configuración de Red
| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| Protocolo STP | IEEE 802.1D | Spanning Tree Protocol estándar |
| VLAN | 20 | VLAN Victima |
| Hello Time | 2 segundos | Intervalo de envío de BPDUs |
| Max Age | 20 segundos | Tiempo máximo de vida de BPDU |
| Forward Delay | 15 segundos | Tiempo de transición entre estados |

### Parámetros de Ataque

#### STP Root Bridge Manipulation
| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| Interfaz | eth0 | Interfaz de red del atacante |
| **Bridge Priority** | **0** | **Prioridad máxima (0 = Root)** |
| Bridge MAC | 00:00:00:00:00:01 | MAC falsa del bridge |
| Root Path Cost | 0 | Costo del path (0 = mínimo) |
| Port ID | 0x8001 | Identificador del puerto |
| BPDU Type | Configuration | Tipo de BPDU enviado |
| Intervalo de envío | 2 segundos | Frecuencia de BPDUs maliciosos |
| Protocol ID | 0x0000 | Identificador del protocolo STP |
| Version | 0 | Versión STP (802.1D) |

### Estructura BPDU Malicioso
```
Ethernet Frame:
  Destination MAC: 01:80:c2:00:00:00 (STP Multicast)
  Source MAC: [MAC del atacante]
  Type: 0x0026 (STP)

BPDU Fields:
  Protocol ID: 0x0000
  Version: 0x00
  BPDU Type: 0x00 (Configuration)
  Flags: 0x00
  Root ID: 0.00:00:00:00:00:01 (Priority 0 + MAC falsa)
  Root Path Cost: 0
  Bridge ID: 0.00:00:00:00:00:01
  Port ID: 0x8001
  Message Age: 0
  Max Age: 20
  Hello Time: 2
  Forward Delay: 15
```

#### Protocolos STP Soportados
| Protocolo | Estándar | Convergencia | Vulnerable a Root Attack |
|-----------|----------|--------------|--------------------------|
| STP | 802.1D | 30-50 seg | ✅ Sí |
| RSTP | 802.1w | 3-6 seg | ✅ Sí |
| MSTP | 802.1s | 3-6 seg | ✅ Sí |
| PVST+ | Cisco Propietario | 30-50 seg | ✅ Sí |
| Rapid PVST+ | Cisco Propietario | 3-6 seg | ✅ Sí |

### Conectividad Requerida
- ✅ Acceso físico a la red de switching
- ✅ Interfaz en modo promiscuo
- ✅ Capacidad de enviar tramas de capa 2
- ⚠️ STP habilitado en la red objetivo

---

## 🛡️ Medidas de Mitigación

### Análisis de Riesgos y Controles - STP Root Attack

| ID | Riesgo Identificado | Severidad | Probabilidad | Impacto | Medida de Mitigación Implementada |
|----|---------------------|-----------|--------------|---------|-----------------------------------|
| R-001 | STP Root Bridge Manipulation | **CRÍTICO** | Alta | Crítico | • **BPDU Guard** en puertos de acceso<br>• **Root Guard** en puertos uplink<br>• Configuración de Root Primary/Secondary<br>• Monitoreo de cambios de Root Bridge<br>• Alertas de TCN (Topology Change Notification) |
| R-002 | Man-in-the-Middle vía STP | **CRÍTICO** | Alta | Crítico | • Root Guard en uplinks<br>• BPDU Filter en puertos críticos<br>• Port Security<br>• Segmentación de VLANs<br>• Cifrado de tráfico (802.1AE MACsec) |
| R-003 | Switching Loops y Broadcast Storms | **CRÍTICO** | Media | Crítico | • Loop Guard<br>• Storm Control<br>• UDLD (UniDirectional Link Detection)<br>• Monitoreo de utilización de CPU/memoria<br>• Rate limiting de broadcasts |
| R-004 | BPDU Spoofing | **ALTO** | Alta | Alto | • BPDU Guard en puertos de acceso<br>• Validación de Bridge ID<br>• Autenticación 802.1X en puertos<br>• Monitoring de BPDUs anómalos |
| R-005 | Denial of Service (DoS) | **ALTO** | Media | Crítico | • Storm Control<br>• Rate limiting<br>• Port Security<br>• CPU protection<br>• QoS para BPDUs legítimos |
| R-006 | Topology Manipulation | **ALTO** | Alta | Alto | • Root Guard global<br>• BPDU Filter<br>• Configuration de prioridades estáticas<br>• Documentación de topología esperada |
| R-007 | Falta de detección de ataques | **ALTO** | Alta | Alto | • IDS/IPS para BPDUs anómalos<br>• SIEM con alertas STP<br>• Syslog centralizado<br>• Baseline de topología STP<br>• Monitoreo 24/7 |
| R-008 | Acceso físico no autorizado | **MEDIO** | Media | Alto | • Control de acceso físico a salas de equipos<br>• Cámaras de seguridad<br>• Port Security con shutdown<br>• Auditorías de seguridad física |

---

### Controles Específicos - STP Root Attack

#### 1. BPDU Guard
**Protección en puertos de acceso - Deshabilita puertos que reciben BPDUs**

```cisco
! Habilitar BPDU Guard globalmente en PortFast
Switch(config)# spanning-tree portfast bpduguard default

! Habilitar BPDU Guard por interfaz
SW-1(config)# interface range tEthernet1/0-5
SW-1(config-if-range)# spanning-tree portfast
SW-1(config-if-range)# spanning-tree bpduguard enable

! Verificar configuración
Switch# show spanning-tree summary
```

**Configuración Arista (EOS):**
```
! Habilitar BPDU Guard en puertos de acceso
SW-1(config)# interface Ethernet1/0
SW-1(config-if)# spanning-tree bpduguard enable
SW-1(config-if)# spanning-tree portfast
```

#### 2. Root Guard
**Previene que puertos se conviertan en Root Port**

```cisco
! Configurar Root Guard en puertos uplink
SW-1(config)# interface Ethernet1/0
SW-1(config-if)# spanning-tree guard root

! Verificar Root Guard
SW-1# show spanning-tree inconsistentports
```

**Configuración Arista (EOS):**
```
! Habilitar Root Guard en uplinks
SW-1(config)# interface Ethernet0/2
SW-1(config-if)# spanning-tree guard root
```

#### 3. Bridge Priority Configuration
**Configuración manual de Root Primary y Secondary**

```cisco
! Configurar Root Primary (prioridad 24576)
SW-1(config)# spanning-tree vlan 20 root primary

! Configurar Root Secondary (prioridad 28672)
SW-1(config)# spanning-tree vlan 20 root secondary

! Configuración manual de prioridad
SW-1(config)# spanning-tree vlan 20 priority 4096

! Verificar configuración
SW-1# show spanning-tree vlan 20
```

**Configuración Arista (EOS):**
```
! Configurar prioridad del bridge
SW-1(config)# spanning-tree vlan 20 priority 4096
```

#### 4. BPDU Filter
**Filtra BPDUs en puertos específicos**

```cisco
! Habilitar BPDU Filter globalmente
SW-1(config)# spanning-tree portfast bpdufilter default

! Habilitar BPDU Filter por interfaz
SW-1(config)# interface Ethernet1/0
SW-1(config-if)# spanning-tree bpdufilter enable
```

⚠️ **Advertencia**: BPDU Filter es peligroso - usar solo en casos específicos

#### 5. Loop Guard
**Previene loops alternativos en caso de fallo unidireccional**

```cisco
! Habilitar Loop Guard globalmente
SW-1(config)# spanning-tree loopguard default

! Habilitar Loop Guard por interfaz
SW-1(config)# interface Ethernet1/0
SW-1(config-if)# spanning-tree guard loop
```

#### 6. Storm Control
**Limita broadcasts, multicasts y unicasts desconocidos**

```cisco
! Configurar Storm Control
SW-1(config)# interface range Ethernet1/0
SW-1(config-if-range)# storm-control broadcast level 10.00
SW-1(config-if-range)# storm-control multicast level 10.00
SW-1(config-if-range)# storm-control action shutdown

! Verificar Storm Control
SW-1# show storm-control
```

#### 7. Port Security
**Limita direcciones MAC y previene spoofing**

```cisco
SW-1(config)# interface range Ethernet1/0
SW-1(config-if-range)# switchport port-security
SW-1(config-if-range)# switchport port-security maximum 3
SW-1(config-if-range)# switchport port-security violation shutdown
SW-1(config-if-range)# switchport port-security mac-address sticky
```

#### 8. UDLD (UniDirectional Link Detection)
**Detecta enlaces unidireccionales que pueden causar loops**

```cisco
! Habilitar UDLD globalmente
SW-1(config)# udld enable

! Habilitar UDLD agresivo en enlaces críticos
SW-1(config)# interface Ethernet1/0
SW-1(config-if)# udld port aggressive
```

---

### Configuración de Seguridad STP Completa (Cisco)

```cisco
!==================================================
! CONFIGURACIÓN RECOMENDADA PARA PROTECCIÓN STP
!==================================================

! 1. Configurar Root Bridge con prioridad baja
spanning-tree vlan 20 root primary
spanning-tree vlan 20 priority 0

! 2. Configurar Root Secondary (backup)
! (En segundo switch más crítico)
spanning-tree vlan 1-100 root secondary

! 3. Habilitar protecciones globales
spanning-tree portfast bpduguard default
spanning-tree loopguard default
udld aggressive

! 4. Configurar puertos de acceso
interface range Ethernet1/0
 description Access Ports - Usuarios
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast
 spanning-tree bpduguard enable
 storm-control broadcast level 10.00
 storm-control action shutdown
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation shutdown

! 5. Configurar puertos uplink/trunk
interface Ethernet1/2-5
 description Uplink to Core Switch
 switchport trunk encapsulation dot1q
 switchport mode trunk
 spanning-tree guard root
 udld port aggressive

! 6. Deshabilitar puertos no utilizados
interface range Ethernet1/0-5
 shutdown
 description UNUSED - Security Policy

! 7. Logging y monitoreo
logging buffered 51200 informational
logging trap notifications
logging source-interface Vlan 20 
logging host 192.168.1.100

! 8. SNMP para monitoreo (opcional)
snmp-server enable traps stp
snmp-server enable traps port-security
```

---

### Monitoreo y Detección

| Herramienta | Propósito | Implementación |
|-------------|-----------|----------------|
| Wireshark/tcpdump | Análisis de BPDUs | Captura y análisis de tramas STP |
| show spanning-tree | Estado STP | Verificación de Root Bridge y puertos |
| Syslog | Logging centralizado | Logs de cambios STP y violations |
| SNMP Traps | Alertas en tiempo real | Notificaciones de cambios de topología |
| Nagios/Zabbix | Monitoreo de red | Alertas de Root Bridge changes |
| Snort/Suricata | IDS/IPS | Reglas para detectar BPDUs anómalos |
| SIEM (Splunk/ELK) | Correlación de eventos | Análisis de patrones de ataque STP |

### Comandos de Verificación

```cisco
! Verificar Root Bridge actual
show spanning-tree root

! Ver estado STP por VLAN
show spanning-tree vlan 20

! Verificar inconsistencias
show spanning-tree inconsistentports

! Ver resumen de STP
show spanning-tree summary

! Verificar BPDU Guard violations
show spanning-tree bpduguard

! Ver estadísticas de interfaces
show spanning-tree interface Ethernet1/0 detail

! Verificar Storm Control
show storm-control

! Ver Root Guard status
show spanning-tree guard
```

---

### Plan de Respuesta a Incidentes

#### FASE 1: DETECCIÓN 
1. Sistema detecta cambio de Root Bridge inesperado
2. Alerta automática SNMP trap o Syslog
3. Verificar con `show spanning-tree root`
4. Identificar nuevo Root Bridge y MAC address
5. Localizar puerto físico del atacante

#### FASE 2: CONTENCIÓN 
1. **Shutdown inmediato** del puerto sospechoso
   ```
   Sw-1(config)# interface EthernetX/X
   Sw-1(config-if)# shutdown
   ```
2. Aislar switch atacante de la topología
3. Preservar evidencia (captura de tráfico, logs)
4. Verificar que Root Bridge legítimo recupere control
5. Documentar Bridge ID y MAC del atacante

#### FASE 3: ERRADICACIÓN 
1. Identificar dispositivo físico conectado al puerto
2. Desconectar dispositivo atacante de la red
3. Analizar logs para determinar duración del ataque
4. Revisar configuración de todos los switches
5. Verificar integridad de configuraciones STP

#### FASE 4: RECUPERACIÓN 
1. Forzar reconvergencia STP si es necesario
   ```
   SW-1# clear spanning-tree detected-protocols
   ```
2. Verificar topología STP en todos los switches
3. Confirmar que Root Bridge correcto está activo
4. Restaurar puertos a estado operacional
5. Monitoreo intensivo durante 24 horas

#### FASE 5: MEJORAS 
1. Documentar el incidente completo
2. Implementar controles faltantes:
   - BPDU Guard en TODOS los puertos de acceso
   - Root Guard en uplinks
   - Port Security con sticky MAC
3. Actualizar políticas de seguridad
4. Capacitación al equipo de networking
5. Realizar pentest de validación

---

### Matriz de Controles de Seguridad STP

| Control | Tipo | Efectividad | Complejidad | Costo | Recomendación |
|---------|------|-------------|-------------|-------|---------------|
| BPDU Guard | Preventivo | ⭐⭐⭐⭐⭐ | Baja | Ninguno | **OBLIGATORIO** |
| Root Guard | Preventivo | ⭐⭐⭐⭐⭐ | Baja | Ninguno | **OBLIGATORIO** |
| Port Security | Preventivo | ⭐⭐⭐⭐ | Media | Ninguno | Muy Recomendado |
| Storm Control | Preventivo | ⭐⭐⭐⭐ | Baja | Ninguno | Recomendado |
| Loop Guard | Preventivo | ⭐⭐⭐ | Baja | Ninguno | Recomendado |
| UDLD | Detectivo | ⭐⭐⭐⭐ | Media | Ninguno | Recomendado |
| IDS/IPS | Detectivo | ⭐⭐⭐⭐ | Alta | $$$ | Muy Recomendado |
| SIEM | Detectivo | ⭐⭐⭐⭐⭐ | Alta | $$$ | Recomendado |

---

### Checklist de Seguridad STP

- [ ] **BPDU Guard** habilitado en todos los puertos de acceso
- [ ] **Root Guard** habilitado en todos los uplinks
- [ ] **Root Primary** configurado manualmente con prioridad baja
- [ ] **Root Secondary** configurado en switch de respaldo
- [ ] **PortFast** habilitado solo en puertos de acceso
- [ ] **Storm Control** configurado en todos los puertos
- [ ] **Port Security** implementado con sticky MAC
- [ ] **Loop Guard** habilitado globalmente
- [ ] **UDLD** habilitado en enlaces críticos
- [ ] Puertos no utilizados en **shutdown**
- [ ] **Logging** configurado y centralizado
- [ ] **SNMP traps** habilitados para eventos STP
- [ ] **Baseline** de topología STP documentada
- [ ] **Monitoreo** activo de cambios de Root Bridge
- [ ] **Plan de respuesta** a incidentes documentado
- [ ] **Backups** de configuración automatizados
- [ ] **Capacitación** del equipo en seguridad STP

---

**⚠️ Disclaimer de Responsabilidad**

Este proyecto es **exclusivamente para fines educativos y de investigación** en entornos de laboratorio controlados. El uso de estas técnicas en redes sin autorización explícita es **ilegal** y puede resultar en consecuencias legales graves.

El ataque STP Root Bridge puede causar **interrupciones severas del servicio** e incluso **colapso total de la red** si no se maneja adecuadamente. El autor no se hace responsable del mal uso de esta herramienta.

Al utilizar este código, aceptas usar este conocimiento de manera ética y legal, y solo en redes donde tienes autorización explícita para realizar pruebas de seguridad.

---

*Última actualización: Febrero 2026*
