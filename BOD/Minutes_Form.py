from acva.Template_Admin import Template_Admin
from acva.z_times import getYMD, get_year
from acva.z_constants import MONTHS
from z_board import check_minutes_datafile, save_minutes

# what date was the meeting? create unix ID for that
# this will be the filename for the pickle
# inside, store the summary (provided)
# and the location of the file (uploaded)
# post-process the word document - make sure perms are read-only

class Minutes_Form (Template_Admin):

    def writeStyleSheet(self):
        self.writeCalPickCSS()
    def writeJavaScript(self):
        self.writeCalPickJS()

    def title(self):
        return 'Add Minutes'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            ERROR = None
            form = self.request().fields()
            if not form.get('summary'):
                ERROR = 'You must provide a meeting summary.'
            if not ERROR:
                fobj = form.get('datafile')
                try:
                    filename = fobj.filename
                except:
                    ERROR = 'You must select a file containing meeting minutes to upload.'

            if not ERROR:
                ERROR = check_minutes_datafile(form)

            if ERROR:
                self.render_form_error('Minutes Upload Error', ERROR)
            else:
                save_minutes(form)
                self.response().sendRedirect('Minutes')

        else:
            wr('<form name="chooseDateForm" id="chooseDateForm" action="Minutes_Form" method="POST" enctype="multipart/form-data">')
            wr('<div class="req">All form fields are required.</div>')
            YR, MO, DY = getYMD()
            wr('<P>')
            wr('<b>Meeting Date</b>')
            wr('<br />')
            self.render_date_picker (YR, MO, DY)
            wr('</P>')

            wr('<P>')
            wr('<b>Meeting Summary</b>')
            wr('<br />')
            wr('<textarea name="summary" rows="5" cols="40"></textarea>')
            wr('</P>')

            wr('<P>')
            wr('<b>Upload Document</b>')
            wr('<br />')
            wr('<input type="file" name="datafile">')
            wr('</P>')

            wr('<P>')
            wr('<input type="submit" value="Save &amp; Upload Minutes">')
            wr('</P>')
            wr('</form>')

