from acva.Template_RTC import Template_RTC
from z_rtc import add_category

class Category_Add (Template_RTC):

    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()
            if form.get('new_category'):
                ERROR = add_category(form.get('new_category'))
                if ERROR:
                    wr('<h1 class="error">That category name already exists.</h1>')
                    wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')
                else:
                    self.response().sendRedirect('Manage')
            else:
                wr('<h1 class="error">You must specify a category name.</h1>')
                wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')



