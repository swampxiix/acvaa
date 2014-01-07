from Template_Main import Template_Main
from z_account import is_site_admin
from z_constants import RESDSTR, DIPLSTR
from z_events import get_future_events, get_event_info, get_calendar
import os

class Calendar (Template_Main):
    def title(self):
        return 'ACVAA Events Calendar'

    def writeContent(self):
        wr = self.writeln
        rolestr = self.request().cookies().get('role', '')
        username = self.request().cookies().get('username')
        IS_RES = rolestr == RESDSTR
        IS_DIP = rolestr == DIPLSTR
        SHOWN = 0
        IS_SITE_ADMIN = is_site_admin(self.request())

#        grid = get_calendar()
#        wr('<table id="cal">')
#        for d in ['Su', 'M', 'Tu', 'W', 'Th', 'F', 'Sa']:
#            wr('<th>%s</th>' % (d))
#        for week in grid:
#            wr('<tr>')
#            for thisY, thisM, thisD in week:

#        if IS_DIP or IS_RES:
        if IS_SITE_ADMIN:
            wr('<div class="button">')
            wr('<a href="Event_Form">+ Add New Event</a>')
            wr('</div>')

        wr('<h1>%s</h1>' % (self.title()))
        all = get_future_events()
        all.sort()
        for event in all:
            id = os.path.basename(event)
            ei = get_event_info(id)
            RENDER = False
            if ei.get('visibility') == 'all':
                RENDER = True
            else: # restricted
                if IS_RES or IS_DIP:
                    RENDER = True
            if RENDER:
                SHOWN += 1
                wr('<a name="%s"></a>' % (id)) # bookmark
                wr('<div class="event_head t18b">')
#                if username == ei.get('username') or IS_SITE_ADMIN:
                if IS_SITE_ADMIN:
                    wr('<div class="flt_r">')
                    wr('<a href="Event_Form?id=%s"><img src="/g/edit.png" alt="edit" width="17" height="17" border="0" /></a>' % (id))
                    wr('<a href="Event_Delete?id=%s&fr=cal"><img src="/g/delete.png" alt="delete" width="17" height="17" border="0" /></a>' % (id))
                    wr('</div>')
                wr(ei.get('title'))
                wr('</div>')
                wr('<table align="right"><tr><td class="event_date">')
                wr('<div class="event_dayofweek">%s</div>' % (ei.get('dayofweek')))
                wr('<div class="event_month">%s</div>' % (ei.get('month')))
                wr('<div class="t18b">%s</div>' % (ei.get('day')))
                wr('<div class="event_year">%s</div>' % (ei.get('year')))
                wr('</table>')
    
                wr('<P class="t12">')
                wr(ei.get('display_date'))
                wr('</P>')
                wr('<P class="t12">')
                wr(ei.get('description').replace('\r\n', '<br />'))
                wr('</P>')
                if ei.get('link_url'):
                    wr('<P class="t12">')
                    if ei.get('link_text'):
                        wr('<a href="%s">%s</a>' % (ei.get('link_url'), ei.get('link_text')))
                    else:
                        wr('<a href="%s">%s</a>' % (ei.get('link_url'), ei.get('link_url')))
                    wr('</P>')
                if ei.get('local_doc_link'):
                    wr('<P class="t12">See document: ')
                    if ei.get('local_doc_text'):
                        wr('<a href="%s">%s</a>' % (ei.get('local_doc_link'), ei.get('local_doc_text')))
                    else:
                        wr('<a href="%s">%s</a>' % (ei.get('local_doc_link'), ei.get('local_doc_link')))
                    wr('</P>')

                wr('<br clear="all" />')
        if not SHOWN:
            wr('<h2 style="margin: 30px 0px 130px 0px;">There are no future events scheduled at this time.</h2>')

