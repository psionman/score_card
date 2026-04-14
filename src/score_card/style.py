from kivy.lang import Builder

Builder.load_string("""
#:set PRIMARY       (0.13, 0.59, 0.95, 1)   # blue
#:set PRIMARY_DARK  (0.09, 0.40, 0.70, 1)   # darker blue
#:set BG            (0.12, 0.12, 0.14, 1)   # dark background
#:set SURFACE       (0.18, 0.18, 0.22, 1)   # card surface
#:set TEXT          (0.95, 0.95, 0.95, 1)   # light text
#:set TEXT_HINT     (0.60, 0.60, 0.65, 1)   # hint text
#:set ACCENT        (0.13, 0.59, 0.95, 1)   # accent

<ScButton@Button>:
    background_color: PRIMARY
    background_normal: ""
    color: TEXT
    size_hint_y: None
    height: dp(48)
    font_size: dp(16)
    bold: True

<ScSecondaryButton@Button>:
    background_color: SURFACE
    background_normal: ""
    color: TEXT
    size_hint_y: None
    height: dp(48)
    font_size: dp(16)

<ScLabel@Label>:
    color: TEXT
    font_size: dp(16)

<ScTitle@Label>:
    color: TEXT
    font_size: dp(24)
    bold: True
    size_hint_y: None
    height: dp(56)
    halign: "center"

<ScInput@TextInput>:
    background_color: SURFACE
    foreground_color: TEXT
    hint_text_color: TEXT_HINT
    cursor_color: PRIMARY
    size_hint_y: None
    height: dp(48)
    padding: dp(12), dp(12)
    font_size: dp(16)
    multiline: False

<ScCard@BoxLayout>:
    orientation: "vertical"
    padding: dp(12)
    spacing: dp(8)
    size_hint_y: None
    canvas.before:
        Color:
            rgba: SURFACE
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(8)]
""")
