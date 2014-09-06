from Index import Index
from z_cpe import SMFILE, get_html_from

class Summary (Index):
    def title(self):
        return 'Summary of Requirements for Application for ACVAA Endorsement of Education Programs'

    def writeContent (self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))
        self.sidebar(SMFILE)
        wr(get_html_from(SMFILE))
