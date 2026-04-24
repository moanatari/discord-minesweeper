import random

def generate_minesweeper(size=8, num_bombs=3):
    rows = size
    cols = size
    
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    
    bombs_placed = 0
    while bombs_placed < num_bombs:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if grid[r][c] != -1: 
            grid[r][c] = -1
            bombs_placed += 1
            
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == -1:
                continue 
            
            bomb_count = 0
            for i in range(max(0, r-1), min(rows, r+2)):
                for j in range(max(0, c-1), min(cols, c+2)):
                    if grid[i][j] == -1:
                        bomb_count += 1
            grid[r][c] = bomb_count
            
    emoji_map = {
        -1: ":bomb:",
        0: ":white_large_square:",
        1: ":one:",
        2: ":two:",
        3: ":three:",
        4: ":four:",
        5: ":five:",
        6: ":six:",
        7: ":seven:",
        8: ":eight:"
    }
    
    
    lines = []
    for r in range(rows):
        row_emojis = []
        for c in range(cols):
            val = grid[r][c]
            emoji = emoji_map[val]
            row_emojis.append(f"||{emoji}||")
        lines.append(" ".join(row_emojis))
        
    
    return "\n".join(lines)

if __name__ == "__main__":
    print("Discord Minesweeper Generator")
    print("Press Enter without typing anything to use default values.\n")
    
    size_input = input("Grid size (square, default 8): ")
    size = 8
    if size_input.strip():
        try:
            size = int(size_input)
        except ValueError:
            print("Invalid input, using default size (8).")
            
    bombs_input = input("Number of bombs (default 3): ")
    num_bombs = 3
    if bombs_input.strip():
        try:
            num_bombs = int(bombs_input)
        except ValueError:
            print("Invalid input, using default number (3).")
            
    max_bombs = size * size
    if num_bombs > max_bombs:
        print(f"\nWarning: You requested {num_bombs} bombs for a grid of {max_bombs} cells.")
        print("That's a bit tough... The grid will be filled with bombs, too bad for you!")
        num_bombs = max_bombs
        
    result = generate_minesweeper(size=size, num_bombs=num_bombs)
    
    print("\nGenerated minesweeper grid:\n")
    print(result)
    print("\n---------------------------------------------------------")
    print("You can copy the grid above and paste it into Discord!")
    
    with open("minesweeper.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print("A copy has also been saved in 'minesweeper.txt'.")
