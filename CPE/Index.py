from acva.Template_Main import Template_Main
from z_cpe import INFILE, get_html_from
from acva.z_account import is_site_admin

class Index (Template_Main):
    def title(self):
        return 'ACVAA Certificate Program Endorsement'

    def sidebar(self, filename):
        wr = self.writeln
        wr('<div class="sb"><div class="st">')
        ISA = is_site_admin(self.request())
        if ISA:
            wr('<div class="button">')
            wr('<a href="Edit_Document?fn=%s">Edit this Page</a>' % (filename))
            wr('</div>')
        wr('''
<div class="t12b"><a href="/CPE/Index">Home</a></div>
<P><a href="/CPE/Guidelines">ACVAA Endorsement Guidelines</a></P>
<P><a href="/CPE/Summary">Summary of Endorsement Requirements</a></P>
<P><a href="/CPE/Application">ACVAA Program Endorsement Application</a></P>
<P><a href="/CPE/Programs">List of Endorsed Programs</a></P>
<p><b>Questions?</b> Please feel free to contact us at <a href="mailto:execdir@acvaa.org">execdir@acvaa.org</a>.</p>
</div></div>
            ''')

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))
        self.sidebar(INFILE)
        wr(get_html_from(INFILE))

