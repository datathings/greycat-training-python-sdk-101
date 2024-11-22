# AUTO-GENERATED FILE PLEASE DO NOT MODIFY MANUALLY
from __future__ import annotations
from ctypes import *
from typing import *
import struct
from greycat import *


@final
class project_lib(GreyCat.Library):
    name_: Final[str] = "project_lib"

    def name(self) -> str:
        return self.name_

    @final
    class project:

        @final
        class Person(GreyCat.Object):
            name_: Final[str] = "project::Person"

            def __init__(self, type: GreyCat.Type, attributes: list[Any] = []) -> None:
                super().__init__(type, attributes)

            def firstName(self) -> str:
                return self._get(self.type_.generated_offsets[0])

            def set_firstName(self, v: str) -> None:
                self._set(self.type_.generated_offsets[0], v)

            def lastName(self) -> str:
                return self._get(self.type_.generated_offsets[1])

            def set_lastName(self, v: str) -> None:
                self._set(self.type_.generated_offsets[1], v)

            @staticmethod
            def create(greycat: GreyCat, firstName: str, lastName: str) -> project_lib.project.Person:
                return project_lib.project.Person(greycat.libs_by_name[project_lib.name_].mapped[0], [firstName, lastName])

        @staticmethod
        def helloWorld(__greycat: Optional[GreyCat] = None) -> str:
            if __greycat is None:
                __greycat  = GreyCat.DEFAULT
            return __greycat.call("project::helloWorld")

        @staticmethod
        def getData(__greycat: Optional[GreyCat] = None) -> std.core.Array:
            if __greycat is None:
                __greycat  = GreyCat.DEFAULT
            return __greycat.call("project::getData")

        @staticmethod
        def greet(firstName: str, lastName: str, __greycat: Optional[GreyCat] = None) -> project_lib.project.Person:
            if __greycat is None:
                __greycat  = GreyCat.DEFAULT
            return __greycat.call("project::greet", [firstName, lastName, ])

    def configure(self, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
        factories[project_lib.project.Person.name_] = lambda type, attributes: project_lib.project.Person(type, attributes)

    def init(self, greycat: GreyCat) -> None:
        self.mapped: list[GreyCat.Type] = [
            greycat.types_by_name[project_lib.project.Person.name_],
        ]
        self.mapped[0].resolve_generated_offsets("firstName", "lastName")
