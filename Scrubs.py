from Template_Authenticated import Template_Authenticated
from z_account import is_diplomate

class Scrubs (Template_Authenticated):

    def title(self):
        return "Order ACVAA Scrubs"

    def writeContent(self):
        wr = self.writeln
        req = self.request()
        wr(str(req))
