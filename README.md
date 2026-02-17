# the ivy gate initative — Ren'Py project

Small Ren'Py visual-novel project containing a phone UI and several minigames.
Web demo: https://ordinarydairy.itch.io/the-ivy-gate-initiative

## Requirements
- Ren'Py (recommended latest stable release)
- Python (bundled with Ren'Py; no separate install required)

## Quick start
1. Place this repository in your Ren'Py projects folder (e.g., `RenPy-*/projects/`).
2. Launch the Ren'Py launcher and open the project named `hypsm`.
3. Click "Launch Project".

## Project layout (important files)
- `script.rpy`, `screens.rpy`, `gui.rpy` — main story, UI screens and GUI.
- `phone/` — phone app logic and subapps (`apps/`, `characters.rpy`, etc.).
- `minigames.rpy` — minigames and matching/puzzle logic.
- `images/` — art assets (cards, pieces, etc.).
- `saves/` — example save files and `persistent`.
- `tl/` — translations/localization files.
- `cache/`, `gui/`, `overlay/` — runtime/GUI assets and caches.

Compiled bytecode (`*.rpyc`, `.rpyb`) and backup files may be present; source `.rpy` files are the ones to edit.
