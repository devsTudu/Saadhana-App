from flet import (Button, Text, Page, Column,ElevatedButton
                  ,View,Container, TextField,FloatingActionButton,
                  BottomSheet,Row, TextButton, Alignment)
from models.elements import myAppBar

class view(View):
    """Design for the new habit adding"""
    def __init__(self,page:Page,*args, **kwargs):
        super().__init__()
        self.name = TextField(label="Title of Habit")
        self.description = TextField(label="Description",
                          multiline=True,
                          min_lines=3)
        
        self.page = page
        
        self.route= "/new"
        self.controls = [Column(
            [
                self.name,
                self.description,
                # self.habits
                Row(
                    [
                        TextButton("Back", on_click=lambda _: page.go('/')),
                        ElevatedButton("Save",on_click=self.save)                        
                    ]
                )

            ]
        )]
        self.appbar = myAppBar("Add Habit")
        
    def save(self,e):
        self.habits = self.page.client_storage.get("habit_list")
        if self.habits is None:
            self.habits = []
        names = [name for name,_ in self.habits]
        print(names)
        if len(self.name.value)<3:
            self.warn_name("Give a good name to this habit")
        elif str(self.name.value) in names:
            print(names)
            self.warn_name("Habit already exists")
        else:
            self.habits.append([self.name.value,self.description.value])
            self.page.client_storage.set('habit_list',self.habits)
            print(self.habits)
    
    def warn_name(self,message:str="Error with the given name"):
        def handle_dismissal(e):
            self.page.close(bs)
            self.name.focus()
        
        bs = BottomSheet(
            on_dismiss=handle_dismissal,
            content=Container(
                padding=20,
                content=Column(
                    tight=True,
                    controls=[
                        Text(message),
                        Row(
                            [TextButton("Go Home",on_click=lambda _:self.page.go("/")),
                            ElevatedButton("Okay", on_click=handle_dismissal),]
                        )
                    ],
                    
                ),
            ),
        )
        self.page.open(bs)