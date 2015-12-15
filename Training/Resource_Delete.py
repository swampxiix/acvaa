from Template_RTC import Template_RTC
from acva.z_forms import submit, hidden
from z_rtc import get_resource_by_id, delete_resource

class Resource_Delete (Template_RTC):
    def title(self):
        return 'Confirm Resource Deletion'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()
            if form.get('rm_resource'):
                ERROR = delete_resource(form.get('rm_resource'))
                if ERROR:
                    wr('<h1 class="error">That resource ID does not exist in the database.</h1>')
                    wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')
                else:
                    self.response().sendRedirect('Index')
            else:
                wr('<h1 class="error">You must specify a resource ID to delete.</h1>')
                wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')

        else:
            wr('<h1>%s</h1>' % (self.title()))

            qs = self.request().fields()
            rezid = qs.get('id')
            if rezid:
                pick = get_resource_by_id(rezid)
                wr('<P>Are you sure you want to delete the Resource named: %s?</P>' % (pick.get('title')))
                wr('<form action="Resource_Delete" method="POST">')
                wr(hidden('rm_resource', rezid))
                wr(submit('Yes. Delete it.'))
                wr('<input type="button" value="Never mind. Leave it alone." onclick="javascript:history.go(-1)">')
                wr('</form>')
            else:
                wr('<h1 class="error">You must specify a resource ID to delete.</h1>')
                wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')

