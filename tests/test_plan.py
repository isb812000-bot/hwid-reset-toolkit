from src.shared.game_registry import GameRegistry
from src.main.session import SpoofSession


def test_plan_includes_all_sources_for_fortnite():
    reg = GameRegistry.load_default()
    sess = SpoofSession(reg, dry_run=True)
    plan = sess.plan(["fortnite"])
    assert plan.targets == ["fortnite"]
    assert set(plan.sources) >= {"registry", "disk_serial", "mac_address"}


def test_unknown_game_raises():
    reg = GameRegistry.load_default()
    import pytest
    with pytest.raises(KeyError):
        reg.get("pubg")