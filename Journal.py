from Template_Authenticated import Template_Authenticated
from z_wiley import get_journal_access, wiley_auth

class Journal (Template_Authenticated):
    def title(self):
        return 'Authenticating with Publisher Website...'

    def writeContent(self):
        wr = self.writeln
        clickusername = self.request().cookies().get('username')
        accesslist = get_journal_access()
        if clickusername in accesslist:
            redir = wiley_auth()
            if redir:
                self.response().sendRedirect(redir)
        else:
            wr('<h2>Sorry, but you do not have access to the Veterinary Anaesthesia and Analgesia journal.</h2>')
