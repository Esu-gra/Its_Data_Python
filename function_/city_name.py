def city_country(name:str,country:str="Italia"):
   return f"{name},{country}"


print(city_country("Roma"))
print(city_country("Milano"))
print(city_country("Barcellona","Spagna"))
print(city_country("Paris","francia"))
