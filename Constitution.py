from Template_Main import Template_Main
from z_account import is_site_admin
from z_constants import MONTHS, BASEDIR
from z_docs import DOC_CONST_DIR, save_constitution, get_constitution_info
from z_times import getYMD, get_year
import os

class Constitution (Template_Main):
    """
    This effectively allows multiple documents to stack up inside the directory
    /usr/local/wwrun/acva/docs/constitution, but only the latest document is
    referenced in the ".info" file therein, which is read for presentation.
    """
    def writeStyleSheet(self):
        self.writeCalPickCSS()
    def writeJavaScript(self):
        self.writeCalPickJS()

    def title(self):
        return 'ACVAA Constitution & Bylaws'

    def writeContent(self):
        wr = self.writeln
        IS_SITE_ADMIN = is_site_admin(self.request())

        wr('<h1>%s</h1>' % (self.title()))

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            ERROR = None
            form = self.request().fields()
            wr(form)

            fobj = form.get('datafile')
            try:
                filename = fobj.filename
            except:
                ERROR = 'You must select a file to upload.'

            if ERROR:
                self.render_form_error('Constitution Upload Error', ERROR)
            else:
                save_constitution(form)
                self.response().sendRedirect('Constitution')

        else:

            ci = get_constitution_info()
            if ci:
#                effdate = '/'.join(ci.get('date', []))
                effdate = ci.get('date', '')
                filename = ci.get('datafile', '')
                msg = ci.get('message', '')
                fileurl = os.path.join(DOC_CONST_DIR.replace(BASEDIR, ''), filename)
                wr('<p>Here\'s where you\'ll find the latest version of the ACVAA Constitution and Bylaws. Please click the link below to download it to your computer.</p>')
                wr('<h3><a href="%s">%s</a></h3>' % (fileurl, filename))
                wr('<p style="font-weight: bold;">Effective date: %s</p>' % (effdate))
                if msg:
                    wr('<p>%s</p>' % (msg))
            else:
                wr('<p>There is no ACVAA Constitution document available at this time.</p>')

            if IS_SITE_ADMIN:
                wr('<hr>')
                wr('<h2>Upload Constitution Document</h2>')
                wr('<form name="chooseDateForm" id="chooseDateForm" action="Constitution" method="POST" enctype="multipart/form-data">')
                YR, MO, DY = getYMD()
                wr('<P>')
                wr('<b>Effective Date of Constitution</b>')
                wr('<br />')
                wr('Date: <input type="text" id="datepicker" name="date">')
#                self.render_date_picker (YR, MO, DY)
                wr('</P>')

                wr('<P>')
                wr('<b>Message</b> (optional)')
                wr('<br />')
                wr('<textarea name="message" rows="5" cols="40"></textarea>')
                wr('</P>')

                wr('<P>')
                wr('<b>Upload Document</b>')
                wr('<br />')
                wr('<input type="file" name="datafile">')
                wr('</P>')
    
                wr('<P>')
                wr('<input type="submit" value="Save &amp; Upload Constitution">')
                wr('</P>')
                wr('</form>')


