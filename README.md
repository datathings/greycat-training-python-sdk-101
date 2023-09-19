# Python SDK 101

This introductory training will guide you through the basics of the GreyCat Python SDK.

## Prerequisites

### Python

- Python >= 3.8
- pip

In some operating systems python executable is exposed as `python3` and others `python`. Please adapt the examples below according to your system.

### GreyCat setup

- GreyCat runtime: https://get.greycat.io/
- Python SDK: 
  - For the impatients:
    ```bash
    python3 -m pip install https://get.greycat.io/files/sdk/python/testing/greycat-latest-py3-none-any.whl
    ```
  - For picking a specific version, necessary for requirements to not fail with every greycat update (as the latest wheel changes, its checksum with it):
    ```bash
    python3 -m pip install https://get.greycat.io/files/sdk/python/testing/6.1/greycat-6.1.32+testing-py3-none-any.whl
    ```
    As the version above is doomed to be outdated, more recent versions can be checked at https://get.greycat.io/files/sdk/python/testing/

## GreyCat server application

The server consists of an example dataset (a `nodeList` of 10 integers) and three endpoints.

- The GreyCat server is started with:
  ```bash
  greycat serve --user=1
  ```
- In Python, the following code instantiates a client to the GreyCat server:
  ```py
  from greycat import *

  greycat: GreyCat = GreyCat("http://localhost:8080")
  ```

### Hello, World!

- Providing an endpoint is as simple as annotating any function with `@expose`:
  ```gcl
  @expose
  fn helloWorld() {
    println("Hello, World!");
  }
  ```
- Then you can call the endpoint in Python with the following code, considering the helloWorld function is stored in `project.gcl`:
  ```py
  greycat.call("project::helloWorld")
  ```
- Expectedly, this call results in a greeting printed on GreyCat server logging stack.

### Getting data

- Endpoints may yield results, for instance the following returns the dataset as an array:
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
- Expectedly, in Python data can be easily gathered with:
  ```py
  data = greycat.call("project::getData")
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

### Sending data

- Conversely, GreyCat endpoints may also accept any number of parameters:
  ```gcl
  @expose
  fn greet(firstName: String, lastName: String): String {
    var greeting = "Hello, ${firstName} ${lastName}!";
    println(greeting);
    return greeting;
  }
  ```
- In Python, the call method of the GreyCat class accepts a second optional parameter, which is a list of the parameters to be send to the GreyCat endpoint:
  ```py
  greeting: str = greycat.call("project::greet", ["John", "Doe"])
  print(greeting)
  ```
- This code will greet John Doe both on GreyCat server and Python client sides.