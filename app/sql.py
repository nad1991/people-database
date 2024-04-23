from sqlalchemy import create_engine, text


def output(result):
    for row in result:
        print(row)


def query_db(text: str):
    query=text(text)

    engine = create_engine(  # sqlalchemy connection to postgres database
        "postgresql+psycopg2://postgres:postgres@db:5432/DB"
    )  # credentials shouldn't be hardcoded like this, but since it's a test with no real data it's not an issue
    conn = engine.connect()
    
    return conn.execute(query)



if __name__ == "__main__":
    pass