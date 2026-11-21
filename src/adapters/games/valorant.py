from src.adapters.games.base import GameAdapter


class ValorantAdapter(GameAdapter):
    def __init__(self) -> None:
        super().__init__(
            game_id="valorant",
            label="Valorant (Vanguard)",
            process_names=["VALORANT-Win64-Shipping.exe", "vgc.exe"],
            hwid_sources=["registry", "disk_serial"],
        )