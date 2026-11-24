from pathlib import Path
from typing import Literal


def load_csv(
    *, path: Path | None = None, csv: str | None = None, sep: Literal[" "] = " "
) -> DecisionTable:
    """
    Very primitive csv* loader. Supports only bools values (encoded as 0s and 1s).
    Allows setting `sep` although only space is officially supported.
    """
    if path is not None:
        with path.open("r") as file:
            txt_rows = file.readlines()
    elif csv is not None:
        txt_rows = csv.splitlines()
    else:
        raise ValueError("Function `load_csv` didn't get `path` or `csv` arguments.")

    X: list[list[bool]] = []
    Y: list[bool] = []

    for row in txt_rows:
        values: list[bool] = []
        if row.find(sep) == -1:
            continue
        for s in row.split(sep):
            val: bool | None = None
            match s.strip():
                case "0":
                    val = False
                case "1":
                    val = True
                case _:
                    raise ValueError(
                        f"Found invalid value when loading csv (when matching '{s}')."
                    )
            values.append(val)

        *x, y = values

        X.append(x)
        Y.append(y)

    return DecisionTable(X, Y)


class DecisionTable:
    def __init__(self, X: list[list[bool]], Y: list[bool]):
        self.X: list[list[bool]] = X
        self.Y: list[bool] = Y

    def attr(self, attr: int) -> list[bool]:
        result: list[bool] = []
        for attrs in self.X:
            v = attrs[attr]
            result.append(v)
        return result

    def n_unique(self, attr: int) -> int:
        # gather attribute
        g = self.attr(attr)
        return len(set(g))

    def count(self, attr: int, val: bool) -> int:
        g = self.attr(attr)
        n = 0
        for i in g:
            if i == val:
                n += 1

        return n
