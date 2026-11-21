# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 0.9.x   | yes       |
| < 0.9   | no        |

## Reporting

This tool manipulates kernel-visible identifiers (SMBIOS, disk serials,
MAC addresses, registry MachineGuid). Do **not** open public issues for
anything that could be turned into an exploit chain against a user's
machine. Email `security@hwid-reset-toolkit.dev` with:

- affected module path
- reproduction steps
- whether the issue is privilege escalation, data leak, or spoof failure

## Known limitations

- Secure Boot + HVCI environments block several spoof vectors. The toolkit
  warns but does not attempt to bypass them.
- Anti-cheat drivers (Vanguard, EAC, BattlEye) may flag the toolkit itself.
  This is expected and documented in `docs/anti_cheat_notes.md`.