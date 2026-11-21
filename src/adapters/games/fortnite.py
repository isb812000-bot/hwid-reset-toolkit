from src.adapters.games.base import GameAdapter


class FortniteAdapter(GameAdapter):
    def __init__(self) -> None:
        super().__init__(
            game_id="fortnite",
            label="Fortnite (EAC)",
            process_names=["FortniteClient-Win64-Shipping.exe"],
            hwid_sources=["registry", "disk_serial", "mac_address"],
        )