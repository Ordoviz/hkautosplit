import sys
from hksplits import autosplit
import xml.etree.ElementTree as ET
from log import log

def parse_splits_file(filename: str):
    """Parses an XML file and returns the splits inside <AutoSplitterSettings> as a list"""
    try:
        root = ET.parse(filename).getroot()
        return [split.text for split in root.find("AutoSplitterSettings/Splits")]
    except FileNotFoundError:
        sys.exit(f"No such file: '{filename}'")
    except (ET.ParseError, TypeError):
        sys.exit("""Invalid splits file: '{}'. A miniminal splits file looks like:
<Run>
  <AutoSplitterSettings>
    <Splits>
      <Split>VengefulSpirit</Split>
    </Splits>
  </AutoSplitterSettings>
</Run>
Such files can be generated using hksplitmaker.com.""".format(filename))

class Timer:
    def __init__(self, splitsfile: str = ''):
        self.running = False
        self.currentsplit = 0

        if splitsfile == '':
            log.warning("Need to give .lss file generated by hksplitmaker.com as first CLI argument for autosplitting")
            self.autosplit_enabled = False
        else:
            self.splits = parse_splits_file(splitsfile)
            self.autosplit_enabled = True

    def split(self):
        self._log("Completed {current}. Next split: {next}")
        self.currentsplit += 1
        if self.currentsplit == len(self.splits):
            self.reset()

    def skip_split(self):
        self._log("Skipped {current}. Next split: {next}")
        self.currentsplit += 1
        if self.currentsplit == len(self.splits):
            self.reset()

    def undo_split(self) -> bool:
        if self.currentsplit > 0:
            self.currentsplit -= 1
            self._log("Undid split. Working on '{current}' again.")
            return True
        return False

    def start(self):
        log.info("Started timer")
        self.running = True

    def reset(self):
        log.info("Resetted run")
        self.currentsplit = 0
        self.running = False

    def toggle_autosplit(self):
        self.autosplit_enabled = not self.autosplit_enabled

    def should_split(self, mem, scene_name, next_scene, gamestate):
        if self.autosplit_enabled:
            splitname = self.splits[self.currentsplit]
            return autosplit(splitname, mem, scene_name, next_scene, gamestate)
        else:
            return False

    def _log(self, fstring: str):
        if self.autosplit_enabled:
            current = self.splits[self.currentsplit]
            try:
                next = self.splits[self.currentsplit + 1]
            except IndexError:
                next = "none"
            log.info(fstring.format(current=current, next=next))