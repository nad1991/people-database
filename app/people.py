import click
from sql import query_db


QUERY = ""


@click.group(chain=True)
@click.pass_context
def cli(ctx):
    """Program to query a small database"""
    ctx.ensure_object(dict)

    pass


@cli.result_callback()
@click.pass_context
def parse(ctx, result):
    QUERY = "SELECT "
    where = False

    try:
        if ctx.obj["COLUMN"]:
            QUERY += f"{ctx.obj['COLUMN']} FROM people"
    except:
        QUERY += "* FROM people"
    try:
        if ctx.obj["AGE"]:
            if where:
                QUERY += f" AND {ctx.obj['AGE']}"
            else:
                QUERY += f" WHERE {ctx.obj['AGE']}"

            where = True
    except:
        pass
    try:
        if ctx.obj["FIND"]:
            if where:
                QUERY += f" AND {ctx.obj['FIND']}"
            else:
                QUERY += f" WHERE {ctx.obj['FIND']}"

            where = True
    except:
        pass
    try:
        if ctx.obj["SORT"]:
            QUERY += f" {ctx.obj['SORT']}"
    except:
        pass

    QUERY += ";"

    query_db(QUERY)


@click.command()
# @click.option("-c", default="*", help="Columns to show")
@click.argument(
    "head",
    type=str,
    default="*",
)
@click.pass_context
def column(ctx, head):
    """Columns to show. Comma-separated, no spaces."""
    columns = ["*", "id", "firstname", "lastname", "email", "age"]

    select = ""
    for arg in head.split(","):
        if arg not in columns:
            exit(f"'{arg}' is not a valid argument.")
        select += f"{arg}, "

    # click.echo(f"SELECT {select[:-2]} FROM people")
    ctx.obj["COLUMN"] = select[:-2]


@click.command()
@click.option("-eq", type=int, help="Shows results equal to this number.")
@click.option(
    "-lt", type=int, help="Shows results lower than this number (non-inclusive)."
)
@click.option(
    "-gt", type=int, help="Shows results greater than this number (non-inclusive)."
)
@click.pass_context
def age(ctx, eq: int, lt: int, gt: int):
    """Filter results by age. '-lt' and '-gt' can be combined."""

    age = "age"

    if eq:
        if lt or gt:
            click.echo("'-eq' cannot be used with '-gt' or '-lt'")
            exit()
        age += f" = {eq}"

    elif gt or lt:
        if gt and not lt:
            age += f" > {gt}"
        elif lt and not gt:
            age += f" < {lt}"
        elif gt and lt:
            age += f" > {gt} AND age < {lt}"

    # click.echo(where)
    ctx.obj["AGE"] = age


@click.command()
@click.argument("text")
@click.option(
    "-c",
    "--column",
    type=click.Choice(["firstname", "lastname", "email"]),
    required=True,
    help="Column to search string",
)
@click.option(
    "-sw", "--starts-with", "sw", is_flag=True, help="Filter by starting letter(s)."
)
@click.option(
    "-ew", "--ends-with", "ew", is_flag=True, help="Filter by last letter(s)."
)
@click.pass_context
def find(ctx, text, column, sw, ew):
    """Filter results by names or email. Case sensitive."""
    find = f"{column} "
    if sw or ew:
        if sw:
            find += f"LIKE '{text}%'"
        elif ew:
            find += f"LIKE '%{text}'"
    else:
        find += f"= '{text}'"

    # click.echo(find)
    ctx.obj["FIND"] = find


@click.command()
@click.argument(
    "column",
    # default="id",
    type=click.Choice(["id", "firstname", "lastname", "email", "age"]),
)
@click.option("-a", "--ascending", is_flag=True, help="Ascending sort.")
@click.option("-d", "--descending", is_flag=True, help="Descending sort.")
@click.pass_context
def sort(ctx, column, ascending, descending):
    """Sort results by column. Defaults by ascending order."""
    sort = f"ORDER BY {column}"
    if descending:
        sort += " DESC"
    elif ascending:
        sort += " ASC"

    # click.echo(sort)
    ctx.obj["SORT"] = sort


cli.add_command(column)
cli.add_command(age)
cli.add_command(find)
cli.add_command(sort)

if __name__ == "__main__":
    cli(obj={})
