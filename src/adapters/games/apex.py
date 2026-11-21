from src.adapters.games.base import GameAdapter


class ApexAdapter(GameAdapter):
    def __init__(self) -> None:
        super().__init__(
            game_id="apex",
            label="Apex Legends (EAC)",
            process_names=["r5apex.exe"],
            hwid_sources=["registry", "disk_serial", "mac_address"],
        )