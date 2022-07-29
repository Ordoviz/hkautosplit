class Gamestate:
    INACTIVE       = 0
    MAIN_MENU      = 1
    LOADING        = 2
    ENTERING_LEVEL = 3
    PLAYING        = 4
    PAUSED         = 5
    EXITING_LEVEL  = 6
    CUTSCENE       = 7
    PRIMER         = 8


class UIState:
    MENU_HOME = 1
    CUTSCENE  = 3
    PLAYING   = 4
    PAUSED    = 5


class HeroTransitionState:
    WAITING_TO_TRANSITION  = 0
    EXITING_SCENE          = 1
    WAITING_TO_ENTER_LEVEL = 2
    ENTERING_SCENE         = 3
    DROPPING_DOWN          = 4
