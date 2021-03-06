from Template_Main import Template_Main
from z_constants import RESDSTR, DIPLSTR
from z_events import get_next_event
from z_wiley import get_journal_access

class Index (Template_Main):
    def title(self):
        return 'American College of Veterinary Anesthesia and Analgesia'

    def writeContent(self):
        wr = self.writeln
        rolestr = self.request().cookies().get('role', '')
        IS_RES = rolestr == RESDSTR
        IS_DIP = rolestr == DIPLSTR
        wr('''
<div class="sb"><div class="st">
<div class="t12b">Payments</div>

<p>
You can pay for dues, exam fees and more with your credit card using PayPal.
</p>
<P>
<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="NDCABTKMY694A">
<input type="image" src="http://www.acvaa.org/g/btn_payduesCC_LG.png" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>
</P>

</div></div>
            ''')

        wr('<P class="t14serif">The American College of Veterinary Anesthesia and Analgesia was founded in 1975 to promote the advancement of veterinary anesthesiology and to assist the veterinary profession in providing exceptional service to all animals.</P>')

        wr('<P>The ACVAA is currently composed of over 220 Board Certified Specialists in Veterinary Anesthesia and Analgesia who practice veterinary anesthesia across the globe.</P>')

        wr('<P>The goals of the ACVAA include establishing, evaluating and maintaining the highest standards in the practice of veterinary anesthesiology by promoting the establishment of educational facilities and clinical and research training in veterinary anesthesiology. Additionally, the ACVAA establishes the criteria of fitness for the designation of a specialist in the practice of veterinary anesthesiology.</P>')

        wr('<P>The ACVAA is an AVMA-Recognized Veterinary Specialty Organization. To learn more about specialization in veterinary medicine, see the American Board of Veterinary Specialties of the American Veterinary Medical Association <a href="https://www.avma.org/professionaldevelopment/education/specialties/pages/default.aspx">website</a>.')
        
        wr('''<div style="padding: 25px; border-top: 2px solid #324150; border-bottom: 2px solid #324150;">
<h2>ACVAA Position Statement on Certificate Programs</h2>
<P>The American College of Veterinary Anesthesia and Analgesia (ACVAA) Diplomate is the only recognized credential in North America acknowledging individual expertise and specialization in veterinary anesthesia and peri-operative analgesia. The ACVAA is organized under the authority of the American Board of Veterinary Specialists (ABVS) and the American Veterinary Medical Association (AVMA). All ACVAA Diplomates have undergone multi-year dedicated residency training under the supervision of ACVAA Diplomates, to achieve a high level of knowledge, skill, and competency in providing anesthesia and analgesia care in multiple species. Diplomate status in Anesthesia and Analgesia is granted following a rigorous examination process.</P>
<P>
The ACVAA promotes anesthesia and analgesia continuing education and training programs designed to advance the knowledge and competency of all veterinary care providers. <a href="/CPE/Index">Endorsement of Certificate granting programs</a> can be accomplished by meeting or exceeding minimal ACVAA guidelines. <a href="/CPE/Guidelines">These guidelines</a> are designed to inform the profession and the public by requiring accurate Certificate program description of content, structure, knowledge and the skill level attained by the anesthesia and analgesia care provider. <a href="/CPE/Programs">ACVAA approved Certificate granting programs</a> are identified and listed on the ACVAA website.
</P>
</div>
''')

        wr('<P style="clear: both; margin-top: 25px; ">')

        wr('<span style="margin-right: 40px;">')

        clickusername = self.request().cookies().get('username')
        accesslist = get_journal_access()
        if clickusername in accesslist:
            wr('<a href="Journal" title="Journal"><img src="/g/journal.jpg" width="200" height="169" alt="Journal" border="0" /></a>')
        else:
            wr('<a href="Foundation" title="The ACVAA Foundation"><img src="/g/foundation.jpg" width="200" height="169" alt="The ACVAA Foundation" border="0" /></a>')
        wr('</span>')

        wr('<span style="margin-right: 40px;">')
        wr('<a href="/Annual" title="2011 Annual Meeting"><img src="/g/annual_mtg.jpg" width="200" height="169" alt="2011 Annual Meeting" border="0" /></a>')
        wr('</span>')

        wr('<span style="">')
        wr('<a href="/News" title="ACVAA News"><img src="/g/news.jpg" width="200" height="169" alt="ACVAA News" border="0" /></a>')
        wr('</span>')

        wr('<P>')

        incl_restricted = False
        if IS_RES or IS_DIP:
            incl_restricted = True
        next_event = get_next_event(incl_restricted)

        if next_event:
            wr('<div style="clear: both;">')
            wr('<h1>Upcoming Events</h1>')
            wr('<div>')
            wr('<table align="right"><tr><td class="event_date">')
            wr('<div class="event_dayofweek">%s</div>' % (next_event.get('dayofweek')))
            wr('<div class="event_month">%s</div>' % (next_event.get('month')))
            wr('<div class="t18b">%s</div>' % (next_event.get('day')))
            wr('<div class="event_year">%s</div>' % (next_event.get('year')))
            wr('</table>')
            wr('<h2>%s</h2>' % (next_event.get('title')))
            wr('<P>')
            wr(next_event.get('display_date'))
            wr('</P>')
            wr('<P>')
            wr(next_event.get('description').replace('\r\n', '<br />'))
            wr('</P>')
            if next_event.get('link_url'):
                wr('<P class="t12">')
                if next_event.get('link_text'):
                    wr('<a href="%s">%s</a>' % (next_event.get('link_url'), next_event.get('link_text')))
                else:
                    wr('<a href="%s">%s</a>' % (next_event.get('link_url'), next_event.get('link_url')))
                wr('</P>')
            if next_event.get('local_doc_link'):
                wr('<P class="t12">See document: ')
                if next_event.get('local_doc_text'):
                    wr('<a href="%s">%s</a>' % (next_event.get('local_doc_link'), next_event.get('local_doc_text')))
                else:
                    wr('<a href="%s">%s</a>' % (next_event.get('local_doc_link'), next_event.get('local_doc_link')))
                wr('</P>')

            wr('<a href="Calendar">Full Events Calendar &raquo;</a>')

            wr('</div>')
            wr('</div>')

