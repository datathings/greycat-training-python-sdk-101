from greycat import *

greycat: GreyCat = GreyCat("http://localhost:8080")

data = greycat.call("project::getData")

print(f"# Data: {data}")
print(f"# Type: {type(data)}[{type(data[0])}]")

py_data: list[int] = [i.value for i in data]
print(f"# {py_data}")