from src.adapters.games.base import GameAdapter


class Cs2Adapter(GameAdapter):
    def __init__(self) -> None:
        super().__init__(
            game_id="cs2",
            label="Counter-Strike 2 (VAC)",
            process_names=["cs2.exe"],
            hwid_sources=["registry", "mac_address"],
        )