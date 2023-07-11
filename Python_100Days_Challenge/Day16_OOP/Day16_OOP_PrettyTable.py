
from prettytable import PrettyTable

table = PrettyTable() # do not forget to add paranthesis

table.add_column("Pokemaon name", ["Pika", "Charmander", "Squirtle"])
table.add_autoindex()
print(table)