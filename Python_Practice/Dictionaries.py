#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates

monthConvertions = {"Jan": "January", "Feb": "February", "Mar": "March"}

print(monthConvertions["Mar"])

print(monthConvertions.get("Jan"))

##default value is "none"
print(monthConvertions.get("Bom", "not valid"))
print(monthConvertions.get("a"))

monthConverterNumber = {1: "Tammi", 2:"Helmi", 3:"Maalis"}
print(monthConverterNumber.get(3))