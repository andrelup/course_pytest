# course_pytest
Repositorio orientado al aprendizaje y práctica del uso de la librería pytest para la creación de pruebas automatizadas en Python. Incluye ejemplos prácticos, casos de uso habituales y buenas prácticas aplicables tanto en entornos académicos como profesionales, con el objetivo de mejorar la calidad del software.

## PostgreSQL (Docker)

Arranca una instancia local de PostgreSQL sin instalar nada en el sistema:

```bash
docker run -d --name pytest-postgres \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=mypassword \
  postgres:16
