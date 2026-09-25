```mermaid
flowchart LR
    Usuario --> Pagina[HTML CSS JavaScript]
    Pagina -->|fetch| API[FastAPI]
    API --> Base[(SQLite)]
    Base --> API
    API --> Pagina
    Pagina --> Usuario
```
