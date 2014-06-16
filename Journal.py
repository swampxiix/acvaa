from Template_Authenticated import Template_Authenticated
from z_wiley import wiley_auth

class Journal (Template_Authenticated):
    def title(self):
        return 'Authenticating with Publisher Website...'

    def writeContent(self):
        redir = wiley_auth()
        if redir:
            self.response().sendRedirect(redir)

