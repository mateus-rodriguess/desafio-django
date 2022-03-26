# desafio-django

## Development environment
### Tools needed:
 * Install [Docker](https://docs.docker.com/compose/install/)
  * Make sure you leave port 8000 open
  * Run docker command in project root
    ```bash
      docker-compose up --build
    ``` 
 * Create the super user to access the CRUD routes
    ```bash
     docker exec -it web_desafio sh
     python manage.py createsuperuser
    ```
* Your application will be running on `http://127.0.0.1:8000`
