from Template_Authenticated import Template_Authenticated
from z_constants import COUNTRY_SELECT

class Testing (Template_Authenticated):

    def writeContent(self):
        wr = self.writeln
        wr(COUNTRY_SELECT)
