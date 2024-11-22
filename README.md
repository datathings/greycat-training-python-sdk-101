# Python SDK 101

This introductory training will guide you through the basics of the GreyCat Python SDK.

## Prerequisites

### Python

- Python >= 3.8
- pip

In some operating systems Python executable is exposed as `python3` and others `python`. Please adapt the examples below according to your system.

### GreyCat setup

- GreyCat `stable` runtime: https://get.greycat.io/
- Python SDK:
  ```bash
  python -m pip install https://get.greycat.io/files/sdk/python/stable/$(curl -s https://get.greycat.io/files/sdk/python/stable/latest | sed 's#/#/greycat-#')-py3-none-any.whl
  ```

### Clone repository

```bash
git clone https://github.com/datathings/greycat-training-python-sdk-101.git
cd greycat-training-python-sdk-101/
```

## GreyCat server application

The server consists of an example dataset (a `nodeList` of 10 integers) and three endpoints.

- The GreyCat server is started with:
  ```bash
  greycat serve --user=1
  ```
- To be able to access endpoints and types from Python, you will first want to generate the binding call, *e.g.* with `python` as your target directory:
  ```bash
  greycat codegen --target=python python
  ```
  This will generate a `python/greycat/project_lib.py` source file you can then import in your application.
- In Python, the following code instantiates a client to the GreyCat server:
  ```py
  from greycat import *
  from python.greycat.project_lib import project_lib

  greycat: GreyCat = GreyCat("http://localhost:8080", libraries=[project_lib()])
  ```

### Hello, World!

- Providing an endpoint is as simple as annotating any function with `@expose`:
  ```gcl
  @expose
  fn helloWorld(): String {
    return "Hello, World!";
  }
  ```
- Then you can call the endpoint in Python with the following code, considering the helloWorld function is stored in `project.gcl`:
  ```py
  project_lib.project.helloWorld()
  ```
- Expectedly, this call results in a greeting printed on Python client logging stack; the code can be tested with `python -m src.hello_world`.

### Getting data

- Endpoints may access stored data, for instance the following returns the whole dataset as an array:
  ```gcl
  @expose
  fn getData(): Array<int> {
    var res = Array<int>::new(data!!.size());
    for (index, value in data?) {
      res[index] = value;
    }
    return res;
  }
  ```
- After a codegen, in Python data can be easily gathered with:
  ```py
  data = project_lib.project.getData()
  ```
- GreyCat integers, as they are stored on 64 bits, are inherently smaller than Python integers; the SDK does not hide that:
  ```py
  print(f"# Data: {data}")
  # Data: [c_long(0),c_long(1),c_long(2),c_long(3),c_long(4),c_long(5),c_long(6),c_long(7),c_long(8),c_long(9)]
  print(f"# Type: {type(data)}[{type(data[0])}]")
  # Type: <class 'greycat.std.std.core.Array'>[<class 'ctypes.c_long'>]
  ```
- However an Array of GreyCat bound integers is easily transformed into a list of Python unbound integers:
  ```py
  py_data: list[int] = [i.value for i in data]
  print(f"# {py_data}")
  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```
- This code can be tested with `python -m src.get_data`.

### Sending data and dealing with custom types

- Conversely, GreyCat endpoints may also accept any number of parameters:
  ```gcl
  type Person {
    firstName: String;
    lastName: String;
  }

  @expose
  fn greet(firstName: String, lastName: String): Person {
    var person = Person {
      firstName: firstName,
      lastName: lastName,
    };
    println("Hello, ${firstName} ${lastName}!");
    return person;
  }
  ```
- We instantiate and return here a custom type Person: this type is accessible in Python after a codegen, with getters and setters for its attributes; additionally, generated functions accept the same parameters as the exposed functions they bind to:
  ```py
  person: project_lib.project.Person = project_lib.project.greet("John", "Doe")
  print(f"Hello, {person.firstName()} {person.lastName()}!")
  ```
- This code will greet John Doe both on GreyCat server and Python client sides; it can be tested with `python -m src.greet`