from acva.Template_Main import Template_Main

from acva.z_account import is_rtc

class Template_RTC (Template_Main):

    def writeBodyParts(self):
        ISRTC = is_rtc(self.request())
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

        if ISRTC:
            self.writeContent()
        else:
            self.writeln('<h1>You must be a member of the Resident Training Committee to access this page.</h1>')


        wr('''
    </div><!-- .col-md-9 -->
  </div><!-- .row -->
</div><!-- #body-container -->
            ''')
        self.writeFooter()
