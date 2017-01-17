from Template_Authenticated import Template_Authenticated
from z_constants import COUNTRY_SELECT

class Testing (Template_Authenticated):

    def addJavaScript(self):
        self.writeln('<script type="text/javascript" src="/js/acvaa_geo.js"></script>')

    def writeContent(self):
        wr = self.writeln
        wr(COUNTRY_SELECT)
        wr('<br>')
        wr('State slot:')
        wr('<div id="state_slot"></div>')
