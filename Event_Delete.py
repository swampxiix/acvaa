from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_events import get_event_info, delete_event
from z_forms import hidden, submit

class Event_Delete (Template_Authenticated):
    def title(self):
        return 'Delete Event?'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        id = qs.get('id', {})
        fr = qs.get('fr', '')
        username = self.request().cookies().get('username')
        IS_SITE_ADMIN = is_site_admin(self.request())

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            delete_event(username, id)
            if fr:
                if fr == 'cal':
                    self.response().sendRedirect('Calendar')
                if fr == 'mgt':
                    self.response().sendRedirect('Events')
            else:
                self.response().sendRedirect('Calendar')

        else:
            if id:
                ei = get_event_info(id)
                event_owner = ei.get('username')
                if (username == event_owner) or IS_SITE_ADMIN:
                    wr('<h1>%s</h1>' % (self.title()))
                    wr('<h2>%s</h2>' % (ei.get('title')))
                    wr('<P>')
                    wr('<b>%s</b><br />' % (ei.get('display_date')))
                    wr('%s<br />' % (ei.get('description')))
                    wr('</P>')
                    wr('<P>Are you sure you want to delete this event?</P>')
                    wr('<form method="POST" action="Event_Delete">')
                    wr(hidden('id', id))
                    wr(hidden('fr', fr))
                    wr(hidden('username', username))
                    wr(submit('Yes, delete the event.'))
                    wr('<input type="button" value="Do nothing." onClick="javascript:history.go(-1)">')
                    wr('</form>')
                else:
                    wr('<h1>You are not the owner of this event.</h1>')

            else:
                wr('No event id.')
