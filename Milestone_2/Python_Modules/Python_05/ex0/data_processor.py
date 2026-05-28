#!/usr/bin/env python3


from typing import Any
from abc import ABC, abstractmethod


class C:
    H = '\033[95m'  # Header
    B = '\033[94m'  # Blue
    C = '\033[96m'  # Cyan
    G = '\033[92m'  # Green
    W = '\033[93m'  # Warning
    F = '\033[91m'  # Fail
    E = '\033[0m'  # End
    Bo = '\033[1m'  # Bold

    def msg(self, color: str, msg: str):
        print(getattr(self, color) + msg + C.E)


class DataProcessor(ABC):
    def __init__(self):
        super().__init__()
        self.data: list = []

    def output(self) -> tuple[int, str]:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return isinstance(data, (int, float))

    def ingest(self, data: int | float | list[int | float]) -> None:
        ...


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        ...


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(x, dict) and
                all(isinstance(k, str) and
                    isinstance(v, str) for k, v in x.items())
                for x in data
            )
        if isinstance(data, dict):
            return all((isinstance(k, str) and
                        isinstance(v, str))
                    for k, v in data.items())
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        ...


def num_proc_tester(num_inst: NumericProcessor) -> None:
    ...


if __name__ == "__main__":
    num_proc: NumericProcessor = NumericProcessor()
    # text_proc: TextProcessor = TextProcessor()
    log_proc: LogProcessor = LogProcessor()

    C().msg("H", "=== Code Nexus - Data Processor ===")
    print(num_proc.validate([42, 42]))
    print(log_proc.validate())
