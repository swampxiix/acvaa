from Template_RTC import Template_RTC
from acva.z_forms import submit, hidden
from z_rtc import delete_category, get_rtc_categories, get_guid_by_name

class Category_Delete (Template_RTC):
    def title(self):
        return 'Confirm Category Deletion'

    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()
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
                CATGUID = get_guid_by_name(catname)
                catdict = get_rtc_categories()
                rezcount = len(catdict.get(CATGUID, []))
                if rezcount > 0:
                    wr('<h1 class="error">Sorry, you can only delete a category with zero Training Resources in it.</h1>')
                    wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')
                else:
                    wr('<h1>%s</h1>' % (self.title()))
                    wr('<P>Are you sure you want to delete the Resource Category named: %s?</P>' % (catname))
                    wr('<form action="Category_Delete" method="POST">')
                    wr(hidden('rm_category', catname))
                    wr(submit('Yes. Delete it.'))
                    wr('<input type="button" value="Never mind. Leave the categories alone." onclick="javascript:history.go(-1)">')
                    wr('</form>')
            else:
                wr('<h1 class="error">You must specify a category name to delete.</h1>')
                wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')


