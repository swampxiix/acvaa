from Template_RTC import Template_RTC
from acva.z_forms import submit, hidden, text
from z_rtc import edit_category

class Category_Edit (Template_RTC):

    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()
            if form.get('new_name'):
                ERROR = edit_category(form.get('old_name'), form.get('new_name'))
                if ERROR:
                    wr('<h1 class="error">That category name does not exist in the database.</h1>')
                    wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')
                else:
                    self.response().sendRedirect('Manage')
            else:
                wr('<h1 class="error">You must specify a new category name.</h1>')
                wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')
        else:
            qs = self.request().fields()
            catname = qs.get('cat')
            if catname:
                wr('<h1>Edit Category Name</h1>')
                wr('<form action="Category_Edit" method="POST">')
                wr('<P>Change category name from %s to:<br>' % (catname))
                wr(hidden('old_name', catname))
                wr(text('new_name'))
                wr('<br>')
                wr(submit('Edit category.'))
                wr('<input type="button" value="Never mind. Leave the category alone." onclick="javascript:history.go(-1)">')
                wr('</form>')
            else:
                wr('<h1 class="error">You must specify a category name to delete.</h1>')
                wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')


