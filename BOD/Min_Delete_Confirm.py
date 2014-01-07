from acva.Template_Admin import Template_Admin
from acva.z_constants import FMONTHS
from acva.z_forms import hidden, submit
from z_board import get_minutes, kill_minutes

class Min_Delete_Confirm (Template_Admin):

    def title(self):
        return 'Confirm Removal of Minutes'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        min_id = qs.get('id')

        wr('<h1>%s</h1>' % (self.title()))

        if not min_id:
            wr('<P>You have not selected minutes for a specific date to delete.</P>')
        else:
            if self.request()._environ.get('REQUEST_METHOD') == 'POST':
                form = self.request().fields()
                kill_minutes(form.get('id'))
                self.response().sendRedirect('Minutes')

            else:
                wr('<h3>Are you sure you want to delete the following?</h3>')
                meet_dict = get_minutes(min_id)
                M, D, Y = meet_dict.get('date')
                wr('<P><b>Date</b>:<br />%s %s, %s</P>' % (FMONTHS.get(int(M)), D, Y))
                wr('<P><b>Summary</b>:<br /> %s</P>' % (meet_dict.get('summary')))
                wr('<P><b>Document</b>:<br /> %s</P>' % (meet_dict.get('datafile')))
                wr('<form method="POST" action="Min_Delete_Confirm">')
                wr(hidden('id', min_id))
                wr(submit('Yes, delete.'))
                wr('<input type="button" value="No, leave everything as it is now." onClick="javascript:history.go(-1)">')
                wr('</form>')
