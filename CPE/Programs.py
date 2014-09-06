from Index import Index
from z_cpe import PGFILE, get_html_from

class Programs (Index):
    def title(self):
        return 'List of ACVAA-Endorsed Certificate Programs'

    def writeContent (self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))
        self.sidebar(PGFILE)
        wr(get_html_from(PGFILE))
