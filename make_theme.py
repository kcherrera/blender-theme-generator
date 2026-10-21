import bpy

theme = bpy.context.preferences.themes[0]

# colors
PALETTE = {
    "bg_dark": "#5A5475",
    "bg": "#8077A8",
    "panel": "#5A5475",
    "button": "#C5A3FF",
    "button_hover": "#8077A8",
    "border": "#C2FFDF",
    "text": "#F8F8F0",
    "text_dim": "#C5A3FF",
    "text_bright": "#F8F8F0",
    "accent": "#FFB8D1",
    "selected": "#C5A3F5",
    "active": "#C5A3FF"
}

# converting hex colors
def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")    # removes
    red = int(hex_code[0:2], 16) / 255
    green = int(hex_code[2:4], 16) / 255
    blue = int(hex_code[4:6], 16) / 255
    return (red, green, blue)

# simplifying 
def color(name):
    return hex_to_rgb(PALETTE[name])

# some colors needs an alpha value
def alphaColor(name, alpha=1.0):
    return color(name) + (alpha,)

# start fresh
bpy.ops.preferences.reset_default_theme()

# buttons
BUTTON_TYPES = [
    "wcol_regular", "wcol_tool", "wcol_toolbar_item", "wcol_radio",
    "wcol_text", "wcol_option", "wcol_toggle", "wcol_num", "wcol_numslider",
    "wcol_box", "wcol_menu", "wcol_pulldown", "wcol_menu_back",
    "wcol_pie_menu", "wcol_tooltip", "wcol_menu_item", "wcol_scroll",
    "wcol_progress", "wcol_list_item", "wcol_tab", "wcol_curve",
]

for name in BUTTON_TYPES:
    widget = getattr(theme.user_interface, name)
    widget.inner = alphaColor("button")
    widget.inner_sel = alphaColor("button_hover")
    widget.outline = alphaColor("border")
    widget.outline_sel = alphaColor("accent")
    widget.item = alphaColor("accent")
    widget.text = color("text")
    widget.text_sel = color("text_bright")

# editors
EDITORS = [
    "view_3d", "graph_editor", "file_browser", "nla_editor",
    "dopesheet_editor", "image_editor", "sequence_editor", "properties",
    "text_editor", "node_editor", "outliner", "info", "preferences",
    "console", "clip_editor", "topbar", "statusbar", "spreadsheet",
]

for name in EDITORS:
    space = getattr(theme, name).space
    space.header = alphaColor("panel")
    space.header_text = color("text")
    space.text = color("text")

    if hasattr(space, "back"):
        space.back = color("bg")
    else:
        space.gradients.background_type = 'LINEAR'
        space.gradients.high_gradient = color("bg")
        space.gradients.gradient = color("bg_dark")

# panels
theme.user_interface.panel_back = alphaColor("panel")
theme.user_interface.panel_header = alphaColor("panel")
theme.user_interface.editor_border = color("border")

# sidebars
theme.regions.sidebars.back = alphaColor("panel")
theme.regions.sidebars.tab_back = alphaColor("bg_dark")

# selection / syntax
theme.view_3d.object_active = color("accent")
theme.view_3d.face_mode_select = alphaColor("selected", 0.25)
theme.text_editor.syntax_builtin = hex_to_rgb("#FFB8D1")

#save
bpy.ops.wm.save_userpref()