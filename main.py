import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width, screen_height = 80, 50
    
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)
    
    # Load the font, which I for some reason called "assets.png"
    tileset = tcod.tileset.load_tilesheet(
        "assets.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    
    # Out event handler!
    event_handler = EventHandler()
    
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
                x = player_x,
                y = player_y,
                string = "@"
            )
            
            context.present(root_console)
            root_console.clear()
            
            for event in tcod.event.wait():
                action = event_handler.dispatch(event)
                
                print(action)
                
                if action is None:
                    continue
                
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                elif isinstance(action, EscapeAction):
                    raise SystemExit()
                


if __name__ == "__main__":
    main()