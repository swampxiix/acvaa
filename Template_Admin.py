from Template_Main import Template_Main

from z_account import is_site_admin

class Template_Admin (Template_Main):

    def writeBodyParts(self):
        ISA = is_site_admin(self.request())
        wr = self.writeln
        self.writeHeader()
        self.writeSubHeader()
        wr('''
<div class="container" id="body-container">
  <div class="row">
    <!-- LEFT MENU COLUMN ###################################################### -->
    <div class="col-md-3" id="side-menu">
            ''')
        self.writeNav()
        wr('''
    </div><!-- .col-md-3 #side-menu -->
    <!-- RIGHT CONTENT COLUMN ###################################################### -->
    <div class="col-md-9" id="main-content">
            ''')

        if ISA:
            self.writeContent()
        else:
            self.writeln('<h1>You must be a site administrator to access this page.</h1>')


        wr('''
    </div><!-- .col-md-9 -->
  </div><!-- .row -->
</div><!-- #body-container -->
            ''')
        self.writeFooter()
