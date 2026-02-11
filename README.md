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

- **Topología de red del escenario**
  
  ![Topología](screenshots/topologia.png)

- **Configuración STP antes del ataque**
  
  ![STP Before](screenshots/stp_before.png)

- **Ejecución del ataque STP Root Attack**
  
  ![Ataque STP](screenshots/ataque_stp.png)

- **Switch atacante como nuevo Root Bridge**
  
  ![New Root](screenshots/new_root_bridge.png)

- **Tráfico STP interceptado (BPDUs)**
  
  ![Wireshark](screenshots/wireshark_bpdu.png)

- **Cambios en la topología STP**
  
  ![Topology Change](screenshots/topology_change.png)

## STP Root Attack - Bridge Priority Manipulation
Script de Python que utiliza Scapy para realizar ataques de manipulación del protocolo Spanning Tree Protocol (STP) enviando BPDUs maliciosos con prioridad superior para convertirse en el Root Bridge.

### Requisitos
```bash
pip install scapy
```

### Uso
```bash
git clone https://github.com/tuusuario/STP-Root-Attack.git
cd STP-Root-Attack
chmod +x stp_attack.py
sudo python3 stp_attack.py
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

## 🌐 Topología de Red

### Diagrama de Topología

```
                            Cloud My House
                                  |
                   +--------------+---------------+
                   |                              |
                e1/0                            e0/1
          Kali Linux Atacante                 SW-Cloud
           (STP Priority: 0)                    e0/0
                e0/0                              |
                   |                            e0/1
                e1/0                              |
                 SW-1 ----------PNET----------- R-SD
               (ARISTA)         (ISP)         (Root Bridge Original)
             [Priority: 32768]              [Priority: 32768]
                e0/3 \                         e0/0
                      \                          |
                    e0/0                       e1/0
                     SW-2                        |
                   (ARISTA)                    SW-3
             [Priority: 32768]               (ARISTA)
                    e0/2 \         e0/2  e0/4  [Priority: 32768]
                          \         |     |    / e1/2
                         e0/0     e0/0  e0/0  /  e1/1
                           |       |     |   /   e1/3
                         USER    USER  USER USER
```

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

### Estados STP

#### Antes del Ataque
| Dispositivo | Bridge ID | Prioridad | MAC Address | Rol |
|-------------|-----------|-----------|-------------|-----|
| R-SD | 32768.xxxx.xxxx.xxxx | 32768 | Original | **Root Bridge** |
| SW-1 | 32768.xxxx.xxxx.xxxx | 32768 | Original | Designated |
| SW-2 | 32768.xxxx.xxxx.xxxx | 32768 | Original | Designated |
| SW-3 | 32768.xxxx.xxxx.xxxx | 32768 | Original | Designated |
| SW-Cloud | 32768.xxxx.xxxx.xxxx | 32768 | Original | Designated |

#### Después del Ataque
| Dispositivo | Bridge ID | Prioridad | MAC Address | Rol |
|-------------|-----------|-----------|-------------|-----|
| **Atacante** | **0.0000.0000.0001** | **0** | **Falsa** | **🔴 NEW Root Bridge** |
| R-SD | 32768.xxxx.xxxx.xxxx | 32768 | Original | Designated |
| SW-1 | 32768.xxxx.xxxx.xxxx | 32768 | Original | Designated |
| SW-2 | 32768.xxxx.xxxx.xxxx | 32768 | Original | Designated |
| SW-3 | 32768.xxxx.xxxx.xxxx | 32768 | Original | Designated |
| SW-Cloud | 32768.xxxx.xxxx.xxxx | 32768 | Original | Designated |

### Tabla de Interfaces

#### Kali Linux Atacante (STP Root Malicioso)
| Interfaz | Dirección IP | Estado STP | Descripción |
|----------|--------------|------------|-------------|
| e0 | 192.168.1.50 | **Root** | Interfaz de ataque |
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
| VLAN | 1 (default) | VLAN sin segmentación |
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

---

### Dispositivos de Red Compatibles

#### Switches
| Fabricante | Modelos Soportados | Versión OS | Soporte STP | Estado |
|------------|-------------------|------------|-------------|--------|
| **Arista** | **7050/7280/7500** | **EOS 4.x+** | **802.1D/w/s** | **✅ Completo** |
| Cisco | Catalyst 2960/3560/3750 | IOS 15.0+ | 802.1D/w/s | ✅ Completo |
| HP | ProCurve 2530/2920 | KB.16.x | 802.1D/w | ✅ Completo |
| Juniper | EX2200/EX3300 | Junos 12.x+ | 802.1D/w/s | ✅ Completo |

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
Switch(config)# interface range GigabitEthernet0/1-23
Switch(config-if-range)# spanning-tree portfast
Switch(config-if-range)# spanning-tree bpduguard enable

! Verificar configuración
Switch# show spanning-tree summary
```

**Configuración Arista (EOS):**
```
! Habilitar BPDU Guard en puertos de acceso
switch(config)# interface Ethernet1-10
switch(config-if-Et1-10)# spanning-tree bpduguard enable
switch(config-if-Et1-10)# spanning-tree portfast
```

#### 2. Root Guard
**Previene que puertos se conviertan en Root Port**

```cisco
! Configurar Root Guard en puertos uplink
Switch(config)# interface GigabitEthernet0/24
Switch(config-if)# spanning-tree guard root

! Verificar Root Guard
Switch# show spanning-tree inconsistentports
```

**Configuración Arista (EOS):**
```
! Habilitar Root Guard en uplinks
switch(config)# interface Ethernet24
switch(config-if-Et24)# spanning-tree guard root
```

#### 3. Bridge Priority Configuration
**Configuración manual de Root Primary y Secondary**

```cisco
! Configurar Root Primary (prioridad 24576)
Switch(config)# spanning-tree vlan 1 root primary

! Configurar Root Secondary (prioridad 28672)
Switch(config)# spanning-tree vlan 1 root secondary

! Configuración manual de prioridad
Switch(config)# spanning-tree vlan 1 priority 4096

! Verificar configuración
Switch# show spanning-tree vlan 1
```

**Configuración Arista (EOS):**
```
! Configurar prioridad del bridge
switch(config)# spanning-tree vlan 1 priority 4096
```

#### 4. BPDU Filter
**Filtra BPDUs en puertos específicos**

```cisco
! Habilitar BPDU Filter globalmente
Switch(config)# spanning-tree portfast bpdufilter default

! Habilitar BPDU Filter por interfaz
Switch(config)# interface GigabitEthernet0/10
Switch(config-if)# spanning-tree bpdufilter enable
```

⚠️ **Advertencia**: BPDU Filter es peligroso - usar solo en casos específicos

#### 5. Loop Guard
**Previene loops alternativos en caso de fallo unidireccional**

```cisco
! Habilitar Loop Guard globalmente
Switch(config)# spanning-tree loopguard default

! Habilitar Loop Guard por interfaz
Switch(config)# interface GigabitEthernet0/24
Switch(config-if)# spanning-tree guard loop
```

#### 6. Storm Control
**Limita broadcasts, multicasts y unicasts desconocidos**

```cisco
! Configurar Storm Control
Switch(config)# interface range GigabitEthernet0/1-23
Switch(config-if-range)# storm-control broadcast level 10.00
Switch(config-if-range)# storm-control multicast level 10.00
Switch(config-if-range)# storm-control action shutdown

! Verificar Storm Control
Switch# show storm-control
```

#### 7. Port Security
**Limita direcciones MAC y previene spoofing**

```cisco
Switch(config)# interface range GigabitEthernet0/1-23
Switch(config-if-range)# switchport port-security
Switch(config-if-range)# switchport port-security maximum 3
Switch(config-if-range)# switchport port-security violation shutdown
Switch(config-if-range)# switchport port-security mac-address sticky
```

#### 8. UDLD (UniDirectional Link Detection)
**Detecta enlaces unidireccionales que pueden causar loops**

```cisco
! Habilitar UDLD globalmente
Switch(config)# udld enable

! Habilitar UDLD agresivo en enlaces críticos
Switch(config)# interface GigabitEthernet0/24
Switch(config-if)# udld port aggressive
```

---

### Configuración de Seguridad STP Completa (Cisco)

```cisco
!==================================================
! CONFIGURACIÓN RECOMENDADA PARA PROTECCIÓN STP
!==================================================

! 1. Configurar Root Bridge con prioridad baja
spanning-tree vlan 1-100 root primary
spanning-tree vlan 1-100 priority 0

! 2. Configurar Root Secondary (backup)
! (En segundo switch más crítico)
spanning-tree vlan 1-100 root secondary

! 3. Habilitar protecciones globales
spanning-tree portfast bpduguard default
spanning-tree loopguard default
udld aggressive

! 4. Configurar puertos de acceso
interface range GigabitEthernet0/1-23
 description Access Ports - Usuarios
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast
 spanning-tree bpduguard enable
 storm-control broadcast level 10.00
 storm-control action shutdown
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation shutdown

! 5. Configurar puertos uplink/trunk
interface GigabitEthernet0/24
 description Uplink to Core Switch
 switchport trunk encapsulation dot1q
 switchport mode trunk
 spanning-tree guard root
 udld port aggressive

! 6. Deshabilitar puertos no utilizados
interface range GigabitEthernet0/25-48
 shutdown
 description UNUSED - Security Policy

! 7. Logging y monitoreo
logging buffered 51200 informational
logging trap notifications
logging source-interface Vlan1
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
show spanning-tree vlan 1

! Verificar inconsistencias
show spanning-tree inconsistentports

! Ver resumen de STP
show spanning-tree summary

! Verificar BPDU Guard violations
show spanning-tree bpduguard

! Ver estadísticas de interfaces
show spanning-tree interface GigabitEthernet0/1 detail

! Verificar Storm Control
show storm-control

! Ver Root Guard status
show spanning-tree guard
```

---

### Plan de Respuesta a Incidentes

#### FASE 1: DETECCIÓN (0-5 minutos)
1. Sistema detecta cambio de Root Bridge inesperado
2. Alerta automática SNMP trap o Syslog
3. Verificar con `show spanning-tree root`
4. Identificar nuevo Root Bridge y MAC address
5. Localizar puerto físico del atacante

#### FASE 2: CONTENCIÓN (5-15 minutos)
1. **Shutdown inmediato** del puerto sospechoso
   ```
   Switch(config)# interface GigabitEthernet0/X
   Switch(config-if)# shutdown
   ```
2. Aislar switch atacante de la topología
3. Preservar evidencia (captura de tráfico, logs)
4. Verificar que Root Bridge legítimo recupere control
5. Documentar Bridge ID y MAC del atacante

#### FASE 3: ERRADICACIÓN (15-30 minutos)
1. Identificar dispositivo físico conectado al puerto
2. Desconectar dispositivo atacante de la red
3. Analizar logs para determinar duración del ataque
4. Revisar configuración de todos los switches
5. Verificar integridad de configuraciones STP

#### FASE 4: RECUPERACIÓN (30-60 minutos)
1. Forzar reconvergencia STP si es necesario
   ```
   Switch# clear spanning-tree detected-protocols
   ```
2. Verificar topología STP en todos los switches
3. Confirmar que Root Bridge correcto está activo
4. Restaurar puertos a estado operacional
5. Monitoreo intensivo durante 24 horas

#### FASE 5: MEJORAS (1-2 semanas)
1. Documentar el incidente completo
2. Implementar controles faltantes:
   - BPDU Guard en TODOS los puertos de acceso
   - Root Guard en uplinks
   - Port Security con sticky MAC
3. Actualizar políticas de seguridad
4. Capacitación al equipo de networking
5. Realizar pentest de validación

---

### Reglas IDS/IPS para Detección

**Snort Rules:**
```
# Detectar BPDUs con prioridad 0 (sospechoso)
alert eth any any -> any any (msg:"STP Root Attack - Priority 0 Detected"; \
  content:"|01 80 C2 00 00 00|"; offset:0; depth:6; \
  content:"|00 00|"; offset:22; depth:2; \
  classtype:network-scan; sid:1000001; rev:1;)

# Detectar múltiples TCN (Topology Change Notifications)
alert eth any any -> any any (msg:"STP Possible Attack - Multiple TCN"; \
  content:"|01 80 C2 00 00 00|"; \
  threshold: type threshold, track by_src, count 10, seconds 60; \
  classtype:denial-of-service; sid:1000002; rev:1;)

# Detectar BPDUs desde puertos de acceso (no deberían enviar)
alert eth $HOME_NET any -> any any (msg:"STP BPDU from Access Port"; \
  content:"|01 80 C2 00 00 00|"; offset:0; depth:6; \
  classtype:policy-violation; sid:1000003; rev:1;)
```

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

**📚 Referencias**
- IEEE 802.1D - Media Access Control (MAC) Bridges
- IEEE 802.1w - Rapid Reconfiguration (RSTP)
- IEEE 802.1s - Multiple Spanning Trees (MSTP)
- Cisco Catalyst Switch Configuration Guide
- Arista EOS Configuration Guide - Spanning Tree
- NIST SP 800-189 - Resilient Interdomain Traffic Exchange
- Yersinia Tool Documentation (STP Attack Framework)

**📧 Contacto**
Para reportes de seguridad o consultas: alexis.minyete@example.com

---

**🔗 Recursos Adicionales**
- [Yersinia - Layer 2 Attack Framework](https://github.com/tomac/yersinia)
- [Scapy STP Documentation](https://scapy.readthedocs.io/en/latest/layers/stp.html)
- [Cisco STP Best Practices](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/24062-146.html)
- [Arista STP Configuration](https://www.arista.com/en/um-eos/eos-section-20-2-spanning-tree-protocol)

---

*Última actualización: Febrero 2026*
