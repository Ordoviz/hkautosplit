> [!NOTE]  
> This is unmaintained. Use https://github.com/AlexKnauth/hollowknight-autosplit-wasm instead.

# hkautosplit
[LiveSplit One](https://one.livesplit.org) autosplitter and load remover for Hollow Knight 1.5 (64-bit) on Linux.

**Do not submit runs using this autosplitter to the speedrun.com leaderboards!**

![Screenshot of my speedrunning setup](https://user-images.githubusercontent.com/37733333/181756321-b99dc3d4-07b8-4202-bec0-7feb7541af7e.png)

## Prerequisites
1. If you don't have a LiveSplit splits file already, generate one using [hksplitmaker.com](https://hksplitmaker.com).
2. Run `python --version` to make sure that you have Python 3.10 (or higher) installed
3. Install `python-websockets` with your Linux distribution's package manager.
4. If you are not using Wayland and want to control LiveSplit One with hotkeys, install `python-pip` aswell and run `pip install pynput`.
5. Run `git clone https://github.com/Ordoviz/hkautosplit && cd hkautosplit`

## Usage
1. Start Hollow Knight 1.5
2. Open a terminal and type `./run /path/to/splitsfile.lss`. You will be asked to enter your password because memory reading requires root privileges. If you don't provide a splits file, only load removal will be done.
3. Go to https://one.livesplit.org and connect to `ws://localhost:50000`

Start playing, select "Game Time" in LiveSplit One and see whether entering a room transition pauses the timer.

The timer will automatically start if you enter King's Pass; it will stop if you complete the last split.

If you have pynput installed, you can use the usual hotkeys:
* `1`: split
* `2`: skip
* `3`: reset
* `8`: undo

Press `7` to toggle automatic splitting.

Keybindings can be configured by changing the source code. See the pynput section at the end of `src/main.py`.

## Future plans
Rewrite in Rust and compile to WebAssembly when LiveSplit One provides documentation on how to do that.

## Acknowledgments
This autosplitter is largely based on the [Hollow Knight autosplitter for Windows](https://github.com/ShootMe/LiveSplit.HollowKnight), but uses a modified version of [PyMemLinux](https://guidedhacking.com/threads/python-memory-library-for-linux-game-hacking.18684/) for memory reading. Also thanks to [livesplitone-global-hotkeys](https://github.com/thearst3rd/livesplitone-global-hotkeys) for showing me how to use pynput with websockets.

## Memory reading
This autosplitter tries various pointer paths that were found with pointer scanning in Cheat Engine to get the address of the Unity game manager. The pointer paths are not 100% reliable but there should always be some pointer path that works. I've heard on the [Speedrun Tool development discord](https://discord.com/invite/N6wv8pW) that the "true" pointer path for Unity games is often more than 10 offsets long, which makes it difficult to find. The Windows autosplitter uses a memory signature (`41FFD3E96300000048B8????????????????488B10488BCE488D6424009049BB`) instead.

## Contact
Feel free to [open a GitHub issue](https://github.com/Ordoviz/hkautosplit/issues/new) or talk to `Ordoviz#8328` on Discord.
