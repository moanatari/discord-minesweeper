# Discord Minesweeper Generator

A simple Python script that generates playable minesweeper grids formatted for Discord using spoiler tags.

## Requirements

- Python 3.6+
- No external dependencies

## Usage

Run the script from your terminal:

```bash
python generate.py
```

You'll be prompted to enter a grid size and the number of bombs. You can also just press Enter to use the defaults (8x8 grid with 3 bombs).

### Example

```text
$ python generate.py
Discord Minesweeper Generator
Press Enter without typing anything to use default values.

Grid size (square, default 8): 5
Number of bombs (default 3): 4

Generated minesweeper grid:

||:one:|| ||:one:|| ||:one:|| ||:white_large_square:|| ||:white_large_square:||
||:one:|| ||:bomb:|| ||:two:|| ||:two:|| ||:one:||
||:two:|| ||:three:|| ||:bomb:|| ||:two:|| ||:bomb:||
||:two:|| ||:bomb:|| ||:three:|| ||:two:|| ||:one:||
||:one:|| ||:one:|| ||:one:|| ||:white_large_square:|| ||:white_large_square:||

---------------------------------------------------------
You can copy the grid above and paste it into Discord!
A copy has also been saved in 'minesweeper.txt'.
```

The script prints the grid to the console so you can copy and paste it directly into Discord. It also saves a copy in `minesweeper.txt` just in case.

1️⃣ 1️⃣ 1️⃣ ⬜ ⬜  
1️⃣ 💣 2️⃣ 2️⃣ 1️⃣  
2️⃣ 3️⃣ 💣 2️⃣ 💣  
2️⃣ 💣 3️⃣ 2️⃣ 1️⃣  
1️⃣ 1️⃣ 1️⃣ ⬜ ⬜  
