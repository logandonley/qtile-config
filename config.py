import os
import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Match, Screen

from settings.colors import GruvboxDark
from settings.groups import groups
from settings.keys import keys
from settings.layouts import floating_layout, layouts
from settings.mouse import mouse
from settings.screens import screens

colors = GruvboxDark
widget_defaults = dict(
    font="BlexMono Nerd Font",
    fontsize=13,
    padding=3,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()


dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"


@hook.subscribe.startup_once
def start_once():
    config = os.path.expanduser("~/.config/qtile/")
    subprocess.call([config + "autostart.sh"])
