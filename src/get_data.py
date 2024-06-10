from greycat import *
from python.greycat.project_lib import project_lib

greycat: GreyCat = GreyCat("http://localhost:8080")

data = project_lib.project.getData()

print(f"# Data: {data}")
print(f"# Type: {type(data)}[{type(data[0])}]")

py_data: list[int] = [i.value for i in data]
print(f"# {py_data}")