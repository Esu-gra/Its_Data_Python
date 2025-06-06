from my_project.weather import check_weather
# passed
def test_check_weather():
   assert check_weather(21.00) == "hot", 'temperatures greater than 20 degree \
        must be considered as hot'
def test_check_weather():
   assert check_weather(5.00) == "average", 'temperatures between 10 and 20 degree must be considered as average temperature'
def test_check_weather():
   assert check_weather(5.00) == "cold", 'temperatures lower than 10 degree must be considered as cold'
      
def test_check_weather():
   assert check_weather(13.00) == "average", 'temperatures between 10 and 20 degree must be considered as average temperature'