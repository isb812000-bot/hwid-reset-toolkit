# Anti-cheat compatibility notes

| Game       | AC         | Registry | Disk serial | MAC | Notes |
|------------|------------|----------|-------------|-----|-------|
| Fortnite   | EAC        | yes      | yes         | yes | spoof before launching launcher |
| Valorant   | Vanguard   | yes      | yes         | no  | requires TPM-aware path |
| CS2        | VAC        | yes      | no          | yes | VAC uses HWID hash of Steam |
| Apex       | EAC        | yes      | yes         | yes | same EAC profile as Fortnite |

Spoof **before** the anti-cheat driver loads. Vanguard in particular
loads at boot — plan a reboot between spoof and launch.