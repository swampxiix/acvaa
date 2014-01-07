from Template_Main import Template_Main

from z_account import is_site_admin

class Template_Admin (Template_Main):

    def writeBodyParts(self):
        ISA = is_site_admin(self.request())
        wr = self.writeln
        self.writeHeader()
        wr('<div id="doc2" class="yui-t1">')
        wr('<div id="bd" role="main">')
        wr('<div id="yui-main">')
        wr('<div class="yui-b">')
        wr('<div class="yui-g">')

        if ISA:
            self.writeContent()
        else:
            self.writeln('<h1>You must be a site administrator to access this page.</h1>')

        wr('</div><!-- .yui-g -->')
        wr('</div><!-- .yui-b -->')
        wr('</div><!-- #yui-main -->')

        if ISA:
            self.writeNav()

        wr('</div><!-- #bd -->')
        self.writeFooter()
        wr('</div><!-- #doc2 .yui-t1 -->')


