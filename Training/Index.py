from acva.Template_Authenticated import Template_Authenticated
from acva.z_account import is_rtc

class Index (Template_Authenticated):
    def title(self):
        return 'ACVAA Resident Training Resources'

    def writeContent(self):
        wr = self.writeln
        if is_rtc(self.request()):
            wr('<div class="button" style="margin-top: 10px;">')
            wr('<a href="Manage">Resource Mgmt.</a>')
            wr('</div>')
        wr('<h1>%s</h1>' % (self.title()))

