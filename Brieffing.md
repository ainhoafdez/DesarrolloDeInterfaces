# BRIEFFING: PROYECTO CHAT
---

## Esquema de Arquitectura

```mermaid
graph LR
    subgraph ClientBox ["CLIENTE (DI NT / PSP)"]
        direction TB
        C1[Cliente]
        C2[Python]
        C3[Socket]
        style ClientBox fill:#f9f9f9,stroke:#333,stroke-width:2px
    end

    subgraph ServerBox ["SERVIDOR (PSP Cripto)"]
        direction TB
        S1[STV]
        S2[Java]
        S3[Socket]
        style ServerBox fill:#f9f9f9,stroke:#333,stroke-width:2px
    end

    ClientBox <--"TCP / IP"--> ServerBox
```

---

## REQUISITOS

### Funcionales (Capacidad)

**VERSION 1 (MVP)**
- Enviar msj
- Recibir msj
- Registro horario msj
- Usuarios
- Encriptados

**VERSION 2**
- Grupos
- Stickers
- Responder msj

**VERSION 3**
- Documentos (fotos)
- Visto msj
- Filtro busqueda
- Estado usuario (conectado, desconectado, ausente)
- Reenvio msj

**VERSION 4**
- Biblioteca docs

### No Funcionales (Tecnologías)

* **Servidor:** Java (Multihilo)
* **Cliente:** Python / QTDesigner + PySide6
* **Protocolo y Seguridad (Payload):**

```mermaid
flowchart LR
    subgraph Datos ["Datos en Claro"]
        direction TB
        A["Time Stamp<br/>(AAAA/MM/DD/HH/MM/SS)"]
        B(Usuario)
        C(Mensaje)
    end
    
    Datos -->|Concatenar| D{Encriptación}
    D -->|Generar| E[PAYLOAD FINAL]
    
    style E fill:#000,stroke:#fff,color:#fff
```

---

## TAREAS

- [ ] Investigar cripto
- [ ] Investigar sockets python
- [ ] Mockup Interfaz
- [ ] Diagrama de clases (Cliente, Servidor)
- [ ] Interfaz QTDesigner
- [ ] Servidor Multihilo
- [ ] Cliente Python con sockets
- [ ] Interfaz: Señales + Slots
- [ ] Pruebas
- [ ] Documentación
