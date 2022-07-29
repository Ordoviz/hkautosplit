import sys
import asyncio
import time
import websockets
import hkenums
import hkmem
from timer import Timer
from log import log

REFRESHRATE = 30  # How many times per second should events be checked

HOST = "localhost"
PORT = 50000
URL  = f"ws://{HOST}:{PORT}"
print('Open one.livesplit.org, click on "Connect to Server", and enter ' + URL)

timer = Timer(splitsfile=sys.argv[1] if 1 < len(sys.argv) else '')

connections: set = set()
def on_press(key):
    if key == split_hotkey:
        timer.split()
        websockets.broadcast(connections, "split")
    elif key == reset_hotkey:
        timer.reset()
        websockets.broadcast(connections, "reset")
    elif key == undo_hotkey:
        if timer.undo_split():
            websockets.broadcast(connections, "undo")
    elif key == skip_hotkey:
        timer.skip_split()
        websockets.broadcast(connections, "skip")
    elif key == toggle_autosplit_hotkey:
        timer.toggle_autosplit()

async def autosplitter(websocket, path):
    connections.add(websocket)

    lastgamestate = None   # gamestate in previous loop iteration
    wasloadingmenu = True  # whether player was quitting to menu in prev iteration

    while True:
        try:
            mem = hkmem.HKmem()
            gamestate = mem.gamestate()
            scene_name = mem.scene_name()
            next_scene = mem.next_scene()
        except (OSError, UnicodeDecodeError):
            # reading memory temporarily fails during quitout
            if not wasloadingmenu:
                log.warning("Failed to read memory")
            time.sleep(1 / REFRESHRATE)
            continue

        G  = hkenums.Gamestate
        UI = hkenums.UIState
        H  = hkenums.HeroTransitionState

        try:
            hazard_respawning = mem.hazard_respawning()
            hero_transitionstate = mem.hero_transitionstate()
            ui_state = mem.ui_state()
            teleporting = mem.camera_teleporting()
        except OSError:
            # we are probably on the main menu
            hazard_respawning = False
            hero_transitionstate = 0
            ui_state = 1
            teleporting = False

        # load removal
        loadingmenu = scene_name == "Quit_To_Menu"
        lookforteleporting = False
        if gamestate == G.PLAYING and lastgamestate == G.MAIN_MENU:
            lookforteleporting = True
        if lookforteleporting and (teleporting or gamestate not in {G.PLAYING, G.ENTERING_LEVEL}):
            lookforteleporting = False
        if ((gamestate == G.PLAYING and teleporting and not hazard_respawning)
            or lookforteleporting
            or (gamestate in {G.PLAYING, G.ENTERING_LEVEL} and ui_state != UI.PLAYING)
            or (gamestate != G.PLAYING and not mem.accepting_input())
            or gamestate in {G.EXITING_LEVEL, G.LOADING}
            or hero_transitionstate == H.WAITING_TO_ENTER_LEVEL
            or (ui_state != UI.PLAYING
                and (loadingmenu or (ui_state != UI.PAUSED and (next_scene != "" or scene_name == "_test_charms")))
                and next_scene != scene_name)
            # or (mem.tilemap_dirty() and not mem.uses_scene_transition_routine())
            # above is always false in 1.3+
           ):
            await websocket.send("pausegametime")
        else:
            await websocket.send("resumegametime")

        if timer.running:
            if timer.should_split(mem, scene_name, next_scene, gamestate):
                timer.split()
                await websocket.send("split")
        elif gamestate == G.ENTERING_LEVEL and next_scene == "Tutorial_01":
            timer.start()
            await websocket.send("start")

        lastgamestate = gamestate
        wasloadingmenu = loadingmenu
        time.sleep(1 / REFRESHRATE)

async def main():
    async with websockets.serve(autosplitter, HOST, PORT):
        await asyncio.Future()

# global hotkeys if pynput installed
try:
    from pynput import keyboard
    split_hotkey = keyboard.KeyCode.from_char('1')
    reset_hotkey = keyboard.KeyCode.from_char('3')
    undo_hotkey  = keyboard.KeyCode.from_char('8')
    skip_hotkey  = keyboard.KeyCode.from_char('2')
    toggle_autosplit_hotkey = keyboard.KeyCode.from_char('7')

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
except ModuleNotFoundError:
    log.info("Hotkeys disabled because pynput not installed")
except ImportError as e:
    log.warning("Hotkeys disabled because pynput failed with error message:")
    print(e)

asyncio.run(main())
