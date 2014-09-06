from Index import Index
from z_cpe import GLFILE, get_html_from

class Guidelines (Index):
    def title(self):
        return 'ACVAA Endorsement Guidelines for Certificate Granting Programs in the Areas of Veterinary Anesthesia and Perioperative Analgesia'

    def writeContent (self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))
        self.sidebar(GLFILE)
        wr(get_html_from(GLFILE))
