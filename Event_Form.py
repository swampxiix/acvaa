from Template_Admin import Template_Admin
#from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_constants import MONTHS
from z_times import get_year
from z_forms import hidden, text, submit
from z_events import get_event_info, ck_new_event, save_event, delete_event

class Event_Form (Template_Admin):
    def title(self):
        id = self.request().fields().get('id')
        if id: return 'Edit Event'
        else: return 'Add New Event'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        id = qs.get('id')
        username = self.request().cookies().get('username')
        IS_SITE_ADMIN = is_site_admin(self.request())

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = qs
            ERROR, ERROR_TYPE = ck_new_event(form)
            if ERROR:
                self.render_form_error(ERROR_TYPE, ERROR)
            else:
                if form.has_key('orig_id'):
                    delete_event(form.get('username'), form.get('orig_id'))
                new_id = save_event(form)
                self.response().sendRedirect('Calendar#%s' % (new_id))
        else:
            ei, event_owner = {}, None
            SHOWFORM = False
            if id: # Event edit
                ei = get_event_info(id)
                event_owner = ei.get('username')
                if (username == event_owner) or IS_SITE_ADMIN:
                    SHOWFORM = True
            else: # Event add
                SHOWFORM = True

            if SHOWFORM:
                wr('<h1>%s</h1>' % (self.title()))
                wr('<form name="chooseDateForm" id="chooseDateForm" action="Event_Form" method="POST">')
                if id:
                    wr(hidden('orig_id', id))
                    wr(hidden('username', event_owner)) # preserve ownership on edit
                else:
                    wr(hidden('username', username)) # assign ownership on add

                wr('<P>')
                wr('<b>Event Title</b>')
                wr('<br />')
                wr(text('title', value=ei.get('title', ''), clss='input'))
                wr('</P>')
    
                # 'date': ['12', '30', '2009']
                eim, eid, eiy = int(ei.get('date', [0,0,0])[0]), int(ei.get('date', [0,0,0])[1]), int(ei.get('date', [0,0,0])[2])
                wr('<P>')
                wr('<b>Event Date</b>')
                wr('<br />')
                self.render_date_picker(eiy, eim, eid)
                wr('</P>')
    
                wr('<P>')
                wr('<b>Who can see this event on the calendar?</b>')
                wr('<br />')
                self.write('<input type="radio" name="visibility" value="all" id="vizall"')
                if (ei.get('visibility') == 'all') or (not id):
                    self.write(' CHECKED ')
                wr('/> <label for="vizall">Everyone</label>')
                wr('<br />')
                self.write('<input type="radio" name="visibility" value="restricted" id="vizres"')
                if ei.get('visibility') == 'restricted':
                    self.write(' CHECKED ')
                wr('/> <label for="vizres">Diplomates &amp; Candidates Only</label>')
                wr('</P>')
    
                wr('<P>')
                wr('<b>Would you like to provide a link to another website?</b>')
                wr('<br />')
                wr('<b>Text to be Linked</b> (e.g., "Visit the association website for more info.")')
                wr('<br />')
                wr(text('link_text', value=ei.get('link_text', ''), clss='input'))
                wr('<br />')
                wr('<b>Link Address</b> (e.g., http://www.example.com/)')
                wr('<br />')
                wr(text('link_url', value=ei.get('link_url', ''), clss='input'))
                wr('</P>')
    
                wr('<P>')
                wr('<b>Description</b>')
                wr('<br />')
                wr('<textarea name="description" class="input" rows="8" cols="48" >%s</textarea>' % (ei.get('description', '')))
                wr('</P>')
    
                wr(submit('Save & Publish Event'))
    
                wr('</form>')

            else: # edit but not owner
                wr('<h1>You are not the owner of this event.</h1>')

    def writeStyleSheet(self):
        self.writeCalPickCSS()
    def writeJavaScript(self):
        self.writeCalPickJS(self.request().fields().get('id', None))
