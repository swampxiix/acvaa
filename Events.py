from Template_Admin import Template_Admin
#from Template_Authenticated import Template_Authenticated
from z_constants import RESDSTR, DIPLSTR
from z_events import get_user_events, get_event_info

class Events (Template_Admin):
    def title(self):
        return 'Events Management'

    def writeContent(self):
        wr = self.writeln
        username = self.request().cookies().get('username')
        rolestr = self.request().cookies().get('role', '')
        IS_RES = rolestr == RESDSTR
        IS_DIP = rolestr == DIPLSTR
        my_events = get_user_events(username)
        my_events.sort()
        if IS_DIP or IS_RES:
            wr('<div class="button">')
            wr('<a href="Event_Form">+ Add New Event</a>')
            wr('</div>')

        wr('<h1>%s</h1>' % (self.title()))

        if my_events:
            wr('<table id="evmg">')
            for event in my_events:
                ei = get_event_info(event)
                if my_events.index(event) % 2:
                    wr('<tr style="background-color: #d9deed;">')
                else:
                    wr('<tr>')
                wr('<td>')
                wr(ei.get('year'))
                wr('<td>')
                wr(ei.get('month'))
                wr('<td>')
                wr(ei.get('day'))
                wr('<td>')
                wr('<a href="Calendar#%s">%s</a>' % (event, ei.get('title')))
#                wr('<td>')
#                wr(ei)

                wr('<td>')
                wr('<a href="Event_Form?id=%s"><img src="/g/edit.png" alt="edit" width="17" height="17" border="0" /></a>' % (event))
                wr('<td>')
                wr('<a href="Event_Delete?id=%s&fr=cal"><img src="/g/delete.png" alt="delete" width="17" height="17" border="0" /></a>' % (event))


            wr('</table>')
        else:
            wr('<h2 style="margin: 30px 0px 130px 0px;">You have no events to manage.</h2>')
