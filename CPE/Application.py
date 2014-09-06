from Index import Index
from z_cpe import APFILE, get_html_from

class Application (Index):
    def title(self):
        return 'ACVAA Program Endorsement Application'

    def writeContent (self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))
        self.sidebar(APFILE)
        wr(get_html_from(APFILE))
