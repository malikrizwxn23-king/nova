from kivymd.theming import ThemeManager


def configure_theme(app):
    app.theme_cls.primary_palette = "BlueGray"
    app.theme_cls.accent_palette = "Teal"
    app.theme_cls.theme_style = "Dark"
    return app
