from flet import (FloatingActionButton,
                  Page,
                  View,
                  ListView,
                  Icon,
                  FloatingActionButtonLocation)
from models.saadhana import HabitCard
from models.elements import myAppBar


class view_homepage(View):
    """Design elements for the home page"""
    def __init__(self, page:Page,*args, **kwargs):
        super().__init__()
        self.route = "/"
        habits = page.client_storage.get("habit_list")
        if habits is None:
            habits = []
        self.controls = [ListView(
                [
                    HabitCard(name,desc) for name,desc in habits
                ]
            )]
        self.appbar=myAppBar("Debasish")
        self.floating_action_button = FloatingActionButton(text="+")
        self.floating_action_button.on_click = lambda _:page.go('/new')
        self.floating_action_button_location = FloatingActionButtonLocation.CENTER_FLOAT

