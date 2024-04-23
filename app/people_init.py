import random
from sqlalchemy import create_engine, text
import time


time.sleep(5)

# randomly generated names to populate db
names = "Susan Mcconnell,Leigh Rasmussen,Hillary Barron,Lewis Pacheco,Neva Blair,Cecilia Norman,Buford Blankenship,Perry Kelley,Edna Lucero,Lula Montgomery,Seth Mercer,Stephan Saunders,Marylou Estes,Connie Flores,Ollie Nunez,Samual Rivera,Darrell Nichols,Eliza Norton,Malcom Cervantes,Raleigh Jensen,Johnnie Middleton,Brandon Colon,Penny Delacruz,Lee Michael,Kirsten Esparza,Lora Estrada,Mollie Petersen,Sue Warren,Colton Golden,Cathryn Evans,Carmine Larson,Irvin Frye,Orville Pierce,Milton Melton,Simon Hinton,Louisa Madden,Hunter Douglas,Jacques Dunn,Robby Henry,Minnie Whitehead,Dewey Gilmore,Genaro Roberson,Nicolas Solis,Clement Macdonald,Jewell Mathews,Murray Tapia,Frederic Randall,Jerome Campos,Lamont Chandler,Tyree Hurley"

people = []
random.seed()

for name in names.split(","):  # parse string as list to insert into our db table
    first, last = name.split(" ")
    people.append(
        {
            "first_name": first,
            "last_name": last,
            "mail": f"{first[0].lower()}{last.lower()}{random.randint(1,999)}@fake.mail",
            "age": f"{random.randint(16,90)}",
        }
    )


engine = create_engine(  # sqlalchemy connection to postgres database
    "postgresql+psycopg2://postgres:postgres@db:5432/DB"
)  # credentials shouldn't be hardcoded like this, but since it's a test with no real data it's not an issue
conn = engine.connect()


tmpstr = ""
for (
    p
) in (
    people
):  # parse values to insert in the table, last item will include an extra comma we can get rid of with slicing
    tmpstr += (
        f"('{p['first_name'] }', '{p['last_name']}', '{p['mail']}', '{p['age']}'), "
    )

result = conn.execute(
    text("INSERT INTO people (FirstName, LastName, Email, Age) VALUES " + tmpstr[:-2])
)
conn.commit()

# print(result.all())
print("done")
