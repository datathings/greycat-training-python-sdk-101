from greycat import *

greycat: GreyCat = GreyCat("http://localhost:8080")
greeting: str = greycat.call("project::greet", ["John", "Doe"])
print(greeting)