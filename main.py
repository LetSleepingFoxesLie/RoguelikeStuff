import tcod

def main() -> None:
    screen_width, screen_height = 80, 50
    
    # Load the font, which I for some reason called "assets.png"
    tileset = tcod.tileset.load_tilesheet(
        "assets.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    
    # This creates the screen! Dang
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "Yet Another Crappy Project!",
        vsync = True
    ) as context:
        
        # The console is where we'll draw things to...
        # Also, numpy accesses 2D arrays in [y, x] order, so 'order = "F"' fixes that, which according to the tutorial
        # will be useful once we start adding numpy to the mix. Wild.
        root_console = tcod.console.Console(screen_width, screen_height, order = "F")
        
        # Game loop
        while True:
            
            # Every frame, print the current game state
            root_console.print(
                x = 1,
                y = 1,
                string = "@"
            )
            
            context.present(root_console)
            
            # Event listener?
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()