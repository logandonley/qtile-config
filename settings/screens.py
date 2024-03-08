from libqtile import bar
from libqtile.config import Screen
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration

from settings.colors import GruvboxDark

colors = GruvboxDark

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_method="line",
                    inactive=colors[1],
                    active=colors[8],
                    highlight_color=colors[2],
                    this_current_screen_border=colors[7],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[7],
                    other_screen_border=colors[4],
                    margin_x=5,
                ),
                widget.Prompt(),
                widget.Spacer(length=8),
                widget.TaskList(
                    highlight_method="block",
                    rounded=False,
                    max_title_width=400,
                    border=colors[7],
                    margin_y=0,
                ),
                widget.CurrentLayoutIcon(
                    foreground=colors[1],
                    padding=4,
                    scale=0.6,
                ),
                widget.CurrentLayout(
                    foreground=colors[1],
                    padding=5,
                ),
                widget.Spacer(length=12),
                widget.Volume(
                    fmt="v{}",
                    foreground=colors[7],
                    fontsize=12,
                    decorations=[
                        BorderDecoration(
                            colour=colors[7],
                            border_width=[0, 0, 2, 0],
                        )
                    ],
                ),
                widget.Spacer(length=12),
                widget.Clock(format="%a %d %I:%M %p"),
                widget.Spacer(length=12),
                widget.Systray(padding=3),
                widget.Spacer(length=12),
            ],
            24,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_method="line",
                    inactive=colors[1],
                    active=colors[8],
                    highlight_color=colors[2],
                    this_current_screen_border=colors[7],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[7],
                    other_screen_border=colors[4],
                    margin_x=5,
                ),
                widget.Prompt(),
                widget.Spacer(length=8),
                widget.TaskList(
                    highlight_method="block",
                    rounded=False,
                    max_title_width=400,
                    border=colors[7],
                    margin_y=0,
                ),
                widget.CurrentLayoutIcon(
                    foreground=colors[1],
                    padding=4,
                    scale=0.6,
                ),
                widget.CurrentLayout(
                    foreground=colors[1],
                    padding=5,
                ),
                widget.Spacer(length=12),
            ],
            24,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_method="line",
                    inactive=colors[1],
                    active=colors[8],
                    highlight_color=colors[2],
                    this_current_screen_border=colors[7],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[7],
                    other_screen_border=colors[4],
                    margin_x=5,
                ),
                widget.Prompt(),
                widget.Spacer(length=8),
                widget.TaskList(
                    highlight_method="block",
                    rounded=False,
                    max_title_width=400,
                    border=colors[7],
                    margin_y=0,
                ),
                widget.CurrentLayoutIcon(
                    foreground=colors[1],
                    padding=4,
                    scale=0.6,
                ),
                widget.CurrentLayout(
                    foreground=colors[1],
                    padding=5,
                ),
                widget.Spacer(length=12),
            ],
            24,
        ),
    ),
]
