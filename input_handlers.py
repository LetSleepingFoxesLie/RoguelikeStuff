from typing import Optional
from actions import Action, EscapeAction, MovementAction

import tcod.event

class EventHandler(tcod.event.EventDispatch[Action]):
    
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        
        # Optional just denotes something could be set to None
        action: Optional[Action] = None
        
        key = event.sym

        match key:
            case tcod.event.KeySym.UP:
                action = MovementAction(dx = 0, dy = -1)
            case tcod.event.KeySym.DOWN:
                action = MovementAction(dx = 0, dy = 1)
            case tcod.event.KeySym.LEFT:
                action = MovementAction(dx = -1, dy = 0)
            case tcod.event.KeySym.RIGHT:
                action = MovementAction(dx = 1, dy = 0)
            case tcod.event.KeySym.ESCAPE:
                action = EscapeAction()
            
        return action