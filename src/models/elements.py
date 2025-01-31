import flet as ft

class myAppBar(ft.AppBar):
    def __init__(self,name:str,*args, **kwargs):
        super().__init__()
        self.leading = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
        content=ft.Text("FF"),
        )
        self.title = ft.Text(name)
        self.actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.Icons.SETTINGS_APPLICATIONS),
        ]
        