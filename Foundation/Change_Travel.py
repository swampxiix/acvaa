from acva.Template_Admin import Template_Admin
from z_found import toggle_travel

class Change_Travel (Template_Admin):
    def writeContent(self):
        toggle_travel()
        self.response().sendRedirect('Index')