from greycat import *
from python.greycat.project_lib import project_lib

greycat: GreyCat = GreyCat("http://localhost:8080")
greeting: str = project_lib.project.greet("John", "Doe")
print(greeting)