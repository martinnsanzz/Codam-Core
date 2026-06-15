#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return lambda x: x


def spell_transformer(spells: list[str]) -> list[str]:
    return lambda x: x


def mage_stats(mages: list[dict]) -> dict:
    return lambda x: x


if __name__ == "__main__":
    artifacts: list = [
        {"name": "Luis", "power": 4, "type": "Fire"},
        {"name": "Juan", "power": 3, "type": "Water"},
        {"name": "Pedro", "power": 2, "type": "Grass"},
        {"name": "Angel", "power": 1, "type": "Rock"}
    ]
    sorted_list = artifact_sorter(artifacts)
    print(sorted_list)