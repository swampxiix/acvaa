from Template_Authenticated import Template_Authenticated
from z_account import is_diplomate

class Scrubs (Template_Authenticated):

    def title(self):
        return "Order ACVAA Scrubs"

    def writeContent(self):
        wr = self.writeln
        req = self.request()
        IS_DIP = is_diplomate(req)
        if IS_DIP:
            wr('<h1>ACVAA Scrubs</h1>')
            wr('<p>You can buy ACVAA scrubs from <a href="http://www.scrubsandbeyond.com/">Scrubs & Beyond</a>.</p>')




        else:
            wr('<h1>Sorry.</h1><p>Scrubs are only available to ACVAA Diplomates.</p>')

