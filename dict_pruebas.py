animales = {"mamifero":{"gorila":1,"elefante":2},"reptiles":{"iguana":3,"cocodrilo":4},"aves":{"aguila":5,"gaviota":6}}

animales["mamifero"]["zebra"] = 3

animales["reptiles"]["iguana"] = 0

animales["aves"].pop("gaviota")

print(animales)