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
        pass
        @staticmethod
        def helloWorld(__greycat: Optional[GreyCat] = None) -> None:
            if __greycat is None:
                __greycat  = GreyCat.DEFAULT
            return __greycat.call("project::helloWorld")

        @staticmethod
        def getData(__greycat: Optional[GreyCat] = None) -> std.core.Array:
            if __greycat is None:
                __greycat  = GreyCat.DEFAULT
            return __greycat.call("project::getData")

        @staticmethod
        def greet(firstName: str, lastName: str, __greycat: Optional[GreyCat] = None) -> str:
            if __greycat is None:
                __greycat  = GreyCat.DEFAULT
            return __greycat.call("project::greet", [firstName, lastName, ])

    def configure(self, loaders: dict[str, GreyCat.Loader], factories: dict[str, GreyCat.Factory]) -> None:
        pass

    def init(self, greycat: GreyCat) -> None:
        self.mapped: list[GreyCat.Type] = [
        ]
