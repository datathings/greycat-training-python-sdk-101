from greycat import *
from python.greycat.project_lib import project_lib

greycat: GreyCat = GreyCat("http://localhost:8080", libraries=[project_lib()])
person: project_lib.project.Person = project_lib.project.greet("John", "Doe")
print(f"Hello, {person.firstName()} {person.lastName()}!")