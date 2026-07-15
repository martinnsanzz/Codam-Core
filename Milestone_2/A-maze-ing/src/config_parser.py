# Built-in modules
from typing import Any, Self

# Local modules
from pydantic import BaseModel, Field, model_validator
from .utils import CustomError


class MazeConfig(BaseModel):
    width: int = Field(ge=2, le=44)
    height: int = Field(ge=2, le=18)
    entry: tuple
    exit: tuple
    output_file: str
    perfect: bool
    seed: int
    alghorithm: int
    display_mode: int

    @model_validator(mode='before')
    def convert_tuple(cls, data: Any) -> Any:
        temp_entry: list = data["entry"].split(",")
        temp_exit: list = data["exit"].split(",")

        if len(temp_entry) > 2:
            raise CustomError(f"Entry should only have (x,y) values {data["entry"]}"
                               "Update config.txt")

        if len(temp_exit) > 2:
            raise CustomError(f"Exit should only have (x,y) values {data["exit"]}"
                    "Update config.txt")
    
        try:
            for i in range(2):
                temp_entry[i] = int(temp_entry[i])
                temp_exit[i] = int(temp_exit[i])

                if temp_entry[i] < 0 or temp_exit[i] < 0:
                    raise CustomError(f"Entry and exit point must be positive!!. " )
        except ValueError:
            raise CustomError("Entry and exit should be (x, y) format. INT ONLY !!")
        
        if temp_entry == temp_exit:
            raise CustomError("Entry and exit can't be the same !! Update config.txt")
        data["entry"] = tuple(temp_entry)
        data["exit"] = tuple(temp_exit)

        return data

    @model_validator(mode='after')
    def validate_bounds(self) -> Self:
        if self.entry[0] > self.width or self.exit[0] >self.width:
            raise CustomError(f"Entry and exit point must be within maze bounds!! {self.entry[0]} {self.exit[0]}")
        
        if self.entry[1] > self.height or self.exit[1] >self.height:
            raise CustomError(f"Entry and exit point must be within maze bounds!! {self.entry[1]} {self.exit[1]}")
        return self


def _config_parser(file_name: str) -> dict[str, Any]:
    with open(file_name, "r") as file:
        content = file.readlines()
        return _extract_config_data(content)


def _extract_config_data(file_data: list[str]) -> dict[str, Any]:
    maze_config: dict[str, Any] = {}

    for line in file_data:
        if "#" not in line:
            tmp: list[str] = line.split("=")
            maze_config.update({tmp[0].upper(): (tmp[1].strip("\n"))})
    return maze_config


def load_maze_config() -> MazeConfig:
    config_dict = _config_parser("config.txt")
    maze_config: MazeConfig = MazeConfig(
        width=config_dict["WIDTH"],
        height=config_dict["HEIGHT"],
        entry=config_dict["ENTRY"],
        exit=config_dict["EXIT"],
        output_file=config_dict["OUTPUT_FILE"],
        perfect=config_dict["PERFECT"],
        seed=config_dict["SEED"],
        alghorithm=config_dict["ALGHORITHM"],
        display_mode=config_dict["DISPLAY_MODE"]
    )
    return maze_config