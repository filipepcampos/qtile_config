from libqtile.config import Group

mod = "mod4"
terminal = "konsole"
font = "Ubuntu Mono"
laptop = False
colors = {"fg": "#ffffff",
          "bg1": "#5c8a5e",
          "bg2": "#303030",
          "bg3": "#101010"}
groups = [Group(i) for i in "123456789"]
