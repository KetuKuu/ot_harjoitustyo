from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.user_view import UserView
from ui.add_view import AddView
from ui.project_view import ProjectView

class UI:
    #Sovelluksen käyttöliittymästä vastaava luokka
    def __init__(self, root):

        self._root = root
        self._current_view = None
        print("UI.init")

    def start(self):
        self._show_login_view()    
        print("UI.start")
        
    def _hide_current_view(self): 
        if self._current_view:   
            self._current_view.destroy()

        self._current_view = None
    
    def _show_login_view(self):
        self._hide_current_view()

        self._current_view=LoginView(
            self._root,
            self._show_user_view, 
            self._show_create_user_view
            )
        print("_show_login_view method")

        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()
        print(" _show_create_user_view")

        self._current_view = CreateUserView(
            self._root,
            self._show_user_view,
            self._show_login_view
        )
        print(" _show_create_user_view")
        self._current_view.pack()
    
    
        
    def _show_user_view(self,user):
        self._hide_current_view()

        self._current_view=UserView(
            self._root,
            user,
            self._show_add_view,
            self._show_project_view,
            self._show_login_view
            
            
        )
        print(" _show_user_view")
        self._current_view.pack()
    


    def _show_add_view(self, user):
        self._hide_current_view()

        self._current_view=AddView(
            self._root,
            self._show_add_view,
            self._show_project_view,
            self._show_user_view,
            user
            
            )
        print(" _show_user_view")
        self._current_view.pack()


    def _show_project_view(self, user):
        self._hide_current_view()
        
        self._current_view= ProjectView(
            self._root,
            user,
            self._show_login_view, 
            self._show_add_view
            )
        print(" projekt_view")
        self._current_view.pack()
   
    def _handle_logout(self):
        print("Logout handled")
        self._show_login_view


    def _handle_project_summary(self):
        print("Project summary handled")
