# Inventario de armas

Proyecto de una API hecha con FastAPI, SQLite y una pagina simple en HTML,
CSS y JavaScript.

## Como funciona

```mermaid
flowchart LR

    Usuario["Usuario"]
    Frontend["Frontend<br>HTML + CSS + app.js"]
    Fetch["fetch()<br>HTTP + JSON"]
    CORS["Middleware CORS"]
    API["FastAPI"]
    Pydantic["Pydantic<br>valida los datos"]
    Manager["armasmanager.py<br>consultas SQL"]
    DB[("Residentevil.db<br>SQLite")]
    Respuesta["Respuesta JSON"]
    Tabla["JavaScript actualiza<br>la tabla"]

    Usuario -->|"Usa el formulario"| Frontend
    Frontend --> Fetch
    Fetch -->|"Peticion HTTP"| CORS
    CORS --> API
    API --> Pydantic
    Pydantic --> Manager
    Manager --> DB
    DB --> Manager
    Manager --> API
    API --> Respuesta
    Respuesta --> Frontend
    Frontend --> Tabla
    Tabla --> Usuario

    subgraph Rutas["Rutas de la API"]
        Crear["POST /agregar"]
        Leer["GET /leer_armas"]
        Precio["GET /leer_precio"]
        Potencia["GET /leer_daño"]
        Borrar["DELETE /eliminar_armas/{id}"]
        Actualizar["PUT /actualizararmas"]
    end

    API --> Crear
    API --> Leer
    API --> Precio
    API --> Potencia
    API --> Borrar
    API --> Actualizar
```

## Cuando se agrega un arma

```mermaid
sequenceDiagram
    actor Usuario
    participant Pagina as HTML y JavaScript
    participant API as FastAPI
    participant Modelo as Pydantic
    participant Manager as armasmanager.py
    participant DB as SQLite

    Usuario->>Pagina: Completa el formulario
    Usuario->>Pagina: Pulsa Agregar
    Pagina->>Pagina: Lee los campos
    Pagina->>Pagina: Convierte los datos a JSON
    Pagina->>API: POST /agregar
    API->>Modelo: Valida los datos
    Modelo-->>API: Datos correctos
    API->>Manager: AgregarArma()
    Manager->>DB: INSERT INTO armas
    DB-->>Manager: Registro guardado
    Manager-->>API: Respuesta
    API-->>Pagina: JSON
    Pagina->>Pagina: Limpia el formulario
    Pagina->>API: GET /leer_armas
    API->>DB: SELECT * FROM armas
    DB-->>API: Lista de armas
    API-->>Pagina: Lista en JSON
    Pagina->>Pagina: Actualiza la tabla
    Pagina-->>Usuario: Muestra el arma nueva
```

## Como iniciar el proyecto

```bash
python3 -m uvicorn main:app --reload
```

La documentacion automatica de FastAPI queda disponible en:

```text
http://127.0.0.1:8000/docs
```
