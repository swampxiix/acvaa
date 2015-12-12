from acva.Template_RTC import Template_RTC
from acva.z_forms import submit, hidden
from z_rtc import delete_category

class Category_Delete (Template_RTC):

    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()
            wr(form)
            if form.get('rm_category'):
                ERROR = delete_category(form.get('rm_category'))
                if ERROR:
                    wr('<h1 class="error">That category name does not exist in the database.</h1>')
                    wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')
                else:
                    self.response().sendRedirect('Manage')
            else:
                wr('<h1 class="error">You must specify a category name to delete.</h1>')
                wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')


        else:
            qs = self.request().fields()
            catname = qs.get('cat')
            if catname:
                wr('<h1>Confirm Category Deletion</h1>')
                wr('<P>Are you sure you want to delete the Resource Category named: %s?</P>' % (catname))
                wr('<form action="Category_Delete" method="POST">')
                wr(hidden('rm_category', catname))
                wr(submit('Yes. Delete it.'))
                wr('<input type="button" value="Never mind. Leave the categories alone." onclick="javascript:history.go(-1)">')
                wr('</form>')
            else:
                wr('<h1 class="error">You must specify a category name to delete.</h1>')
                wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')


