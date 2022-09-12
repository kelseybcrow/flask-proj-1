def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake['name'] == name:
            return cupcake
        return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, 'a', newline='\n') as csvfile:
        fieldnames = ['size', 'name', 'price', 'flavor', 'frosting', 'sprinkles', 'filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)