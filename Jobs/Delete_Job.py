from acva.Template_Admin import Template_Admin
from acva.z_forms import hidden, submit
from z_jobs import get_job_info, delete_job

class Delete_Job (Template_Admin):

    def title(self):
        return "Confirm Job Deletion"

    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()
            delete_job(form.get('jid'))
            self.response().sendRedirect('Index')

        else:
            qs = self.request().fields()
            jid = qs.get('jid')
            if jid:
                jd = get_job_info(jid)
                wr('<h1>%s</h1>' % (self.title()))
                wr('<form method="POST" action="Delete_Job">')
                wr(hidden('jid', jid))
                wr('<p>Are you sure you want to delete this job?</p>')
                wr('<P>%s</P>' % (jd.get('job_title')))
                wr('<input type="button" value="No, leave this job listing alone." onClick="javascript:history.go(-1)">')
                wr(submit('Yep.'))
                wr('</form>')
            else:
                'Nothing to do.'

