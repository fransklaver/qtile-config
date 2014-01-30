from libqtile.config import Key, Screen, Group
from libqtile.command import lazy
from libqtile import layout, bar, widget

mod = "mod1"
bar_font_color = "#3985a4"
color_unfocus = "#888888"
color_focus = "#eeeeee"

keys = [
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up()),
    Key([mod], "l", lazy.layout.grow()),
    Key([mod], "h", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    #Key([mod, "shift"], "space", lazy.layout.flip()),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "Tab",
        lazy.layout.down()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key([mod], "i",      lazy.to_screen(1)),
    Key([mod], "u",      lazy.to_screen(0)),
    Key([mod], "Return", lazy.spawn("urxvt")),
    Key([mod, "shift"], 'u', lazy.spawn("urxvt")),

    # Toggle between different layouts as defined below
    Key([mod], "space",    lazy.nextlayout()),
    Key([mod], "w",      lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod], "r", lazy.spawncmd()),
]

groups = [
    Group("F1"),
    Group("F2"),
    Group("F3"),
    Group("F4"),
    Group("F5"),
    Group("F6"),
    Group("F7"),
    Group("F8"),
]
for i in groups:
    # mod1 + letter of group = switch to group
    keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )

dgroups_key_binder = None
dgroups_app_rules = []

layouts = [
    layout.MonadTall(border_focus=color_focus, border_normal=color_unfocus, border_width=1),
    layout.Max(),
    layout.Stack(stacks=2)
]

screens = [
    Screen(
        top = bar.Bar(
                    [
                        widget.Prompt(foreground=bar_font_color),
                        widget.WindowName(foreground=bar_font_color),
                        widget.Volume(foreground=bar_font_color),
                        widget.Battery(foreground=bar_font_color),
                        widget.Systray(foreground=bar_font_color),
                        widget.Clock('%a %d %b %Y %H:%M',foreground=bar_font_color),
                    ],
                    15,
                ),
    ) for x in range(2)
]

main = None
follow_mouse_focus = True
cursor_warp = False
floating_layout = layout.Floating()
mouse = ()
auto_fullscreen = True
widget_defaults = {}
