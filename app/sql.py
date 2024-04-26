from sqlalchemy import create_engine, text
from os import environ


def parse(result: list, header: iter):  # I regret starting this...

    if result:
        print(result)

        columns = list(zip(*result))
        col_width = {}
        for col, head in zip(columns, header):
            col_width[head] = max([len(head)] + [len(str(i)) for i in col])

        total_width = sum(col_width.values()) + 4 + (len(columns) - 1) * 3

        print("|", "=" * (total_width - 2), "|", sep="")
        print("| ", end="")
        for n in range(len(header)):
            padding = list(col_width.values())[n] + 1
            if n + 1 == len(header):
                print(str(header[n]).ljust(padding), end="|\n")
            else:
                print(str(header[n]).ljust(padding), end="| ")
        print("|", "=" * (total_width - 2), "|", sep="")

        for row in result:
            print("| ", end="")
            for n in range(len(row)):  # iter row by index
                padding = list(col_width.values())[n] + 1
                if n + 1 == len(row):  # detect last column and print new line
                    print(str(row[n]).ljust(padding), end="|\n")
                else:  # cast value to string, add padding according to longest value (including headers) in the column
                    print(str(row[n]).ljust(padding), end="| ")
        print("|", "=" * (total_width - 2), "|", sep="")
    else:
        print("- No results -")


def query_db(txt: str):
    query = text(txt)
    # print(query)

    engine = create_engine(  # sqlalchemy connection to postgres database
        # f"postgresql+psycopg2://postgres:postgres@db:5432/DB"
        f"postgresql+psycopg2://postgres:{environ['DB_PASSWORD_FILE']}@db:5432/DB"
    )  # credentials shouldn't be hardcoded like this, but since it's a test with no real data it's not an issue
    conn = engine.connect()

    result = conn.execute(query)

    parse(result.fetchall(), list(result.keys()))


if __name__ == "__main__":
    pass
