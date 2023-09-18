from greycat import *

greycat: GreyCat = GreyCat("http://localhost:8080")
greycat.call("project::helloWorld")