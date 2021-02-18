from libqtile import widget, bar
from const import colors


class TopBar:
    size = 0
    widget_sep = widget.Sep(linewidth=3, padding=10, foreground=colors["bg1"])

    left_side = [
        widget.GroupBox(
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=8,
            borderwidth=3,
            active=colors["fg"],
            inactive=colors["bg2"],
            highlight_color=colors["bg1"],
            highlight_method="line",
            this_current_screen_border=colors["fg"]
        ),
        widget.Prompt(padding=10),
        widget.WindowName(show_state=False),
    ]
    right_side = [
        widget.Systray(),
        widget_sep,
        widget.CurrentLayout(),
        widget_sep,
        widget.Clock(format='%H:%M'),
        widget_sep,
        widget.Clock(format="%d/%m/%y %a",
                     padding=10),
        widget_sep,
    ]

    def __init__(self, is_laptop, size):
        self.size = size
        if(is_laptop):
            self.right_side += [widget.Battery(
                format="{percent:2.0%}"), self.widget_sep]
        self.right_side += [widget.QuickExit(default_text='X',
                                             padding=10, countdown_format='{}')]

    def make(self):
        return bar.Bar(self.left_side + self.right_side, self.size)
