# people-database

Python CLI application for interacting with a PostgreSQL database in docker

## <a name="quick-start"> Quick Start</a>

Follow these steps to set up the project locally on your machine.

**Prerequisites**

Make sure you have the following installed on your machine:

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/products/docker-desktop/)

**Cloning the Repository**

```bash
git clone hthttps://github.com/nad1991/people-database.git
cd people-database
```

**Installation**

You simply need to create/run the container in docker.


```bash
docker compose up
```

- *Optional*
    I you'd like to make changes in the python scripts without restarting the service run:
    ```bash
    docker compose watch
    ```

**Running the Project**

Attach to the running container with an interactive bash prompt

```bash
docker compose exec app bash
```

By default the database comes with a single empty table. 
I you'd like to populate it with some fluff data run:

```bash
python3 people_init.py
```

And to execute the application run:

```bash
python3 people.py
```

Running it without any arguments or adding `--help` will give you a summary of the commands.

**Example prompt and result**

```bash
$ python3 people.py age -gt 30 column firstname,age find -c firstname -ew n sort age

|=================|
| firstname | age |
|=================|
| Simon     | 39  |
| Kirsten   | 50  |
| Cathryn   | 53  |
| Colton    | 55  |
| Brandon   | 55  |
| Stephan   | 66  |
| Susan     | 73  |
| Irvin     | 76  |
| Milton    | 88  |
|=================|
```
