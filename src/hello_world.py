from greycat import *
from python.greycat.project_lib import project_lib

greycat: GreyCat = GreyCat("http://localhost:8080", libraries=[project_lib()])
print(project_lib.project.helloWorld())