# simple example of using a dictionary to store artifact information
# dictionaries store key:value pairs, allowing for efficient data retrieval based on unique keys
artifact = {
    'name': 'Head from a Statue of King Amenhotep I'
    , 'origin': 'Egypt',
    'period': 'New Kingdom, 18th Dynasty',
    'date': 'ca. 1525–1504 B.C.',
    'material': 'Limestone',
    'dimensions': 'Height: 21.6 cm (8 1/2 in)'
}
print(f"Artifact Name: {artifact['name']}")
print(f"Origin: {artifact['origin']}")
print(f"Period: {artifact['period']}")
print(f"Date: {artifact['date']}")
print(f"Material: {artifact['material']}")
print(f"Dimensions: {artifact['dimensions']}")
