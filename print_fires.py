from my_utils import get_column

country='United States of America'
country_column = 0
fires_column = 3
file_name = 'Agrofood_co2_emission.csv'
fires = get_column(file_name,country,country_column,fires_column)
print(fires)
