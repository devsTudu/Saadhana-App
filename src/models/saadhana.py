import flet as ft

class HabitCard(ft.Card):
    def __init__(self,title: str,subtitle: str, ftIcon:ft.Icons=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.AC_UNIT
                                        if ftIcon is None else ftIcons),
                        title=ft.Text(title),
                        subtitle=ft.Text(subtitle)
                    ),
                    ft.Row(
                        [
                            ft.TextButton("Mark Today"),
                            ft.Button("Write")
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    )
                ]
            )
        )