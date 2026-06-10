#!/usr/bin/env python3


class C:
    H = '\033[95m'  # Header
    B = '\033[94m'  # Blue
    C = '\033[96m'  # Cyan
    G = '\033[92m'  # Green
    W = '\033[93m'  # Warning
    F = '\033[91m'  # Fail
    E = '\033[0m'  # End
    Bo = '\033[1m'  # Bold
    U = '\033[4m'

    def msg(self, color: str, msg: str) -> None:
        print(getattr(self, color) + msg + C.E)


C().msg("W", "LOADING STATUS: Loading programs...")


TOTAL_ERRORS = 0

import sys  # noqa


try:
    plt = None
    import matplotlib as plt  # type: ignore
except (ModuleNotFoundError, ImportError) as error:
    TOTAL_ERRORS += 1
    C().msg("F", f"     -{str(error)}")

try:
    pd = None
    import pandas as pd  # type: ignore
except (ModuleNotFoundError, ImportError) as error:
    TOTAL_ERRORS += 1
    C().msg("F", f"     -{str(error)}")

try:
    np = None
    import numpy as np  # type: ignore
    import numpy.typing as npt
except (ModuleNotFoundError, ImportError) as error:
    TOTAL_ERRORS += 1
    C().msg("F", f"     -{str(error)}")

try:
    requests = None
    import requests  # type: ignore
except (ModuleNotFoundError, ImportError) as error:
    TOTAL_ERRORS += 1
    C().msg("F", f"     -{str(error)}")


def install_instructions() -> None:
    C().msg("Bo", "\nInstallation instructions: ")

    print("With pip -> 'pip -m install <package_name>'")
    print("With poetry -> 'poetry add <package_name>@latest'\n")


def dependencies_info() -> None:
    C().msg("H", "\nChecking dependencies: ")
    if pd:
        print(f" [OK] pandas ({pd.__version__}): Data \
manipulation ready")
    if np:
        print(f" [OK] numpy ({np.__version__}): Numerical \
computation ready")
    if requests:
        print(f" [OK] request ({requests.__version__}): Network \
access ready")
    if plt:
        print(f" [OK] matplotlib ({plt.__version__}): Visualization\
ready")


def generate_matrix_data() -> npt.NDArray:
    if np is None:
        raise ModuleNotFoundError("numpy not available")
    return np.random.randn(5, 10)


if __name__ == "__main__":
    if TOTAL_ERRORS != 0:
        install_instructions()
    dependencies_info()

    if pd and np and requests and plt:
        C().msg("H", "\n=== Testing dependencies ===")
        C().msg("Bo", "This uses numpy to generate an Matrix array")
        print(generate_matrix_data())

        C().msg("Bo", "This uses panda to manipulate data")
        data = generate_matrix_data()
        df = pd.DataFrame(data)
        print(df)

        C().msg("Bo", "\nResults save to: matrix_analysis.png")
        
        import matplotlib.pyplot as plt  # type: ignore
        
        plt.hist(df.values.flatten())
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.savefig('matrix_analysis.png')
