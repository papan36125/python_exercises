destinations=["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_destination_index(destination):
  destination_index=destinations.index(destination)
  return destination_index

print(get_destination_index("Los Angeles, USA"))
print(get_destination_index("Paris, France"))
#print(get_destination_index("Hyderabad, India"))

def get_traveler_location(traveler):
  traveler_destination=traveler[1]
  traveler_destination_index=get_destination_index(traveler_destination)
  return traveler_destination_index
test_destination_index=get_traveler_location(test_traveler)
print(test_destination_index)
attractions=[]
for i in range(len(destinations)):
  attractions.append([])
print(attractions)
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination=attractions[destination_index]
    attractions_for_destination.append(attraction)
    return
  except ValueError:
    return
  
add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
print(attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)
def find_attractions(destination, interests):
  try:
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest=[]
    for possible_attraction in attractions_in_city:
      attraction_tags=possible_attraction[1]
      for interest in interests:
        if interest in attraction_tags:
          attractions_with_interest.append(possible_attraction[0])
          break
    return attractions_with_interest
  except ValueError:
    return []
  
la_arts=find_attractions("Los Angeles, USA",['art'])
print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination=traveler[1]
  traveler_interests=traveler[2]
  traveler_attractions = find_attractions(traveler_destination,traveler_interests)
  interests_string="Hi "
  interests_string += traveler[0]
  interests_string += ", we think you'll like these places around "
  interests_string += traveler_destination
  interests_string += ": "
  for att in traveler_attractions:
    interests_string += att
    if traveler_attractions.index(att) == len(traveler_attractions) - 1:
      interests_string += "."
    else:
      interests_string += ", "
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
  
  
  
  
  
  
  
  

  