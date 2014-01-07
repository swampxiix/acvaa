from acva.Template_Admin import Template_Admin

from acva.z_constants import JOB_CATS
from acva.z_forms import hidden, select, text, submit
from z_jobs import ck_job_info, save_job, get_job_info

class Job_Form (Template_Admin):

    def title(self):
        return "Add/Edit Job"

    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()
            ERROR, ERROR_TYPE = ck_job_info(form)
            if ERROR:
                self.render_form_error(ERROR_TYPE, ERROR)
            else:
                save_job(form)
                self.response().sendRedirect('Index?sv=1')

        else:
            qs = self.request().fields()
            IS_EDIT = JOB_ID = qs.get('jid')

            jp = {}
            if IS_EDIT:
                wr('<h1>Edit Job</h1>')
                jp = get_job_info(JOB_ID)
            else:
                wr('<h1>Add New Job</h1>')

            wr('<form method="POST" action="Job_Form">')

            if JOB_ID:
                wr(hidden('id', JOB_ID))

            # ------------------------------------------------------
            wr('<h2>Provide Details about the Job</h2>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Category</b><br />')
            wr(select(name='category', opts=JOB_CATS, selected=jp.get('category'), clss='input'))
            wr('<span class="req">required</span>')
            wr('</div>')

            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Expiration Date</b><br />')
            expm, expd, expy = int(jp.get('expires', [0,0,0])[0]), int(jp.get('expires', [0,0,0])[1]), int(jp.get('expires', [0,0,0])[2])
            self.render_date_picker(expy, expm, expd, dname="expires")
            wr('<span class="req">required</span>')
            wr('</div>')

            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Job Title</b><br />')
            wr(text('job_title', value=jp.get('job_title', ''), clss='input'))
            wr('<span class="req">required</span>')
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Institution/Organization</b><br />')
            wr(text('job_inst', value=jp.get('job_inst', ''), clss='input'))
            wr('<span class="req">required</span>')
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Department</b><br />')
            wr(text('job_dept', value=jp.get('job_dept', ''), clss='input'))
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Job Description</b> <span class="req">required</span><br />')
            wr('<textarea name="description" class="input" cols="72" rows="6">%s</textarea>' % (jp.get('description', '')))
            wr('</div>')

            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('Would you like to include a link to another website?')
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Text to be Linked</b><br />')
            wr(text('web_link_text', value=jp.get('web_link_text', ''), clss='input'))
            wr('<small>e.g., visit our website for more information</small>')
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Link Address</b><br />')
            wr(text('web_link_url', value=jp.get('web_link_url', ''), clss='input'))
            wr('<small>e.g., http://www.example.com/job_listing</small>')
            wr('</div>')
            # ------------------------------------------------------
            wr('<h2>C.V. Submission</h2>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('Where and how should prospective job candidates submit their information for consideration?')
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Instructions</b><br />')
            wr('<textarea name="cv_instructions" class="input" cols="72" rows="4">%s</textarea>' % (jp.get('cv_instructions', '')))
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Contact Name</b><br />')
            wr(text('cv_name', value=jp.get('cv_name', ''), clss='input'))
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Title</b><br />')
            wr(text('cv_title', value=jp.get('cv_title', ''), clss='input'))
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Address</b><br />')
            wr(text('cv_addr1', value=jp.get('cv_addr1', ''), clss='input'))
            wr('<br />')
            wr(text('cv_addr2', value=jp.get('cv_addr2', ''), clss='input'))
            wr('<br />')
            wr(text('cv_addr3', value=jp.get('cv_addr3', ''), clss='input'))
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>City, State, ZIP</b><br />')
            wr(text('cv_city', value=jp.get('cv_city', ''), clss='input'))
            wr(text('cv_state', value=jp.get('cv_state', ''), clss='input', size='3'))
            wr(text('cv_zip', value=jp.get('cv_zip', ''), clss='input', size='9'))
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Country</b><br />')
            wr(text('cv_country', value=jp.get('cv_country', ''), clss='input'))
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Email</b><br />')
            wr(text('cv_email', value=jp.get('cv_email', ''), clss='input'))
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Phone</b><br />')
            wr(text('cv_phone', value=jp.get('cv_phone', ''), clss='input'))
            wr('</div>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<b>Fax</b><br />')
            wr(text('cv_fax', value=jp.get('cv_fax', ''), clss='input'))
            wr('</div>')

            # ------------------------------------------------------
            wr('<h2>Contacts (optional)</h2>')
            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<em>This is different from where candidates will send their CVs.</em> If the candidate has questions about this job listing, who should they contact and how?')
            wr('</div>')

            wr('<div style="margin: 7px 0px 7px 0px;">')
            wr('<table><tr><td>')

            wr('<table><tr><th colspan="2">Contact 1')
            wr('<tr><td>Name')
            wr('<td>%s' % (text('contact1_name', value=jp.get('contact1_name', ''), clss='input')))
            wr('<tr><td>Email')
            wr('<td>%s' % (text('contact1_email', value=jp.get('contact1_email', ''), clss='input')))
            wr('<tr><td>Phone')
            wr('<td>%s' % (text('contact1_phone', value=jp.get('contact1_phone', ''), clss='input')))
            wr('</table>')

            wr('<td>')

            wr('<table><tr><th colspan="2">Contact 2')
            wr('<tr><td>Name')
            wr('<td>%s' % (text('contact2_name', value=jp.get('contact2_name', ''), clss='input')))
            wr('<tr><td>Email')
            wr('<td>%s' % (text('contact2_email', value=jp.get('contact2_email', ''), clss='input')))
            wr('<tr><td>Phone')
            wr('<td>%s' % (text('contact2_phone', value=jp.get('contact2_phone', ''), clss='input')))
            wr('</table>')

            wr('</table></div>')

            # ------------------------------------------------------
            wr('<div style="margin: 21px 0px 7px 0px;">')
            wr(submit('Save &amp; Post Job Info'))
            wr('</div>')

            wr('</form>')

    def writeStyleSheet(self):
        self.writeCalPickCSS()
    def writeJavaScript(self):
        self.writeCalPickJS(self.request().fields().get('jid', None))
