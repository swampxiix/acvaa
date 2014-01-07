from acva.Template_Main import Template_Main

from acva.z_account import is_site_admin
from time import strftime
from z_jobs import get_job_info

class Display (Template_Main):

    def title(self):
        qs = self.request().fields()
        global jid
        jid = qs.get('jid') or qs.get('id')
        global jd
        jd = get_job_info(jid)
        return 'ACVAA Job: %s' % (jd.get('job_title'))

    def writeContent(self):
        wr = self.writeln
        if jd:
            IS_ADMIN = is_site_admin(self.request())
    
            wr('<div class="sb"><div class="st">')
            wr('<div style="margin: 7px 0px 7px 0px;"><b>Job Category:</b><br />%s</div>' % (jd.get('category')))
            try:
                wr('<div style="margin: 7px 0px 7px 0px;"><b>Posted:</b><br />%s</div>' % (strftime("%b. %d, %Y", jd.get('posted'))))
                wr('<div style="margin: 7px 0px 7px 0px;"><b>Expires:</b><br />%s</div>' % (strftime("%b. %d, %Y", jd.get('exp_tuple'))))
            except TypeError:
                pass
    
            if IS_ADMIN:
                wr('<div style="margin: 7px 0px 7px 0px;">')
                wr('<a href="Job_Form?jid=%s"><img src="/g/edit.png" alt="edit" width="17" height="17" border="0" /></a>' % (jid))
                wr('<a href="Delete_Job?jid=%s"><img src="/g/delete.png" alt="delete" width="17" height="17" border="0" /></a>' % (jid))
                wr('</div>')
    
            wr('</div></div>')
    
            wr('<h1>%s</h1>' % (jd.get('job_title')))
            wr('<h2>%s</h2>' % (jd.get('job_inst')))
            if jd.get('job_dept'):
                wr('<h2>%s</h2>' % (jd.get('job_dept')))
    
            desc = jd.get('description', '')
            desc = desc.replace('\r', '<br />')
            wr('<p>%s</p>' % (desc))
    
            wu, wt = jd.get('web_link_url'), jd.get('web_link_text')
            if wu:
                wr('<div style="margin: 7px 0px 21px 0px;">')
                if wt and wu:
                    wr('<a href="%s">%s</a>' % (wu, wt))
                else:
                    wr('<a href="%s">%s</a>' % (wu, wu))
                wr('</div>')
    
    
            c1n, c1e, c1p = jd.get('contact1_name', 'n/a'), jd.get('contact1_email', 'n/a'), jd.get('contact1_phone', 'n/a')
            c2n, c2e, c2p = jd.get('contact2_name', 'n/a'), jd.get('contact2_email', 'n/a'), jd.get('contact2_phone', 'n/a')
    
            if c1n or c1e or c1p or c2n or c2e or c2p:
                wr('<p>If you have questions, please contact:<br />')
                if c1n:
                    wr(c1n)
                if c1e:
                    if c1n:
                        wr(', ')
                    wr('<a href="mailto:%s">%s</a>' % (c1e, c1e))
                if c1p:
                    if c1n or c1e:
                        wr(', ')
                    wr(c1p)
                if c1n or c1e or c1p:
                    wr('<br />')
                if c2n:
                    wr(c2n)
                if c2e:
                    if c2n:
                        wr(', ')
                    wr('<a href="mailto:%s">%s</a>' % (c2e, c2e))
                if c2p:
                    if c2n or c2e:
                        wr(', ')
                    wr(c2p)
                wr('</p>')
    
            APPLYINFO = False
            for a in ['cv_instructions', 'cv_name', 'cv_title', 'cv_addr1', 'cv_addr2', 'cv_addr3', 'cv_city', 'cv_state', 'cv_zip', 'cv_country', 'cv_email', 'cv_phone', 'cv_fax']:
                if jd.get(a):
                    APPLYINFO = True
    
            if APPLYINFO:
    
                wr('<h2>Where &amp; How to Apply</h2>')
                if jd.get('cv_instructions'):
                    wr('<p><b>Instructions</b>: %s</p>' % (jd.get('cv_instructions')))
                wr('<p>')
                if jd.get('cv_name'):
                    wr('<b>%s</b>' % (jd.get('cv_name')))
                if jd.get('cv_title'):
                    if jd.get('cv_name'):
                        wr(', ')
                    wr(jd.get('cv_title'))
                wr('<br />')
                wr(jd.get('cv_addr1'))
                wr('<br />')
                if jd.get('cv_addr2'):
                    wr(jd.get('cv_addr2'))
                    wr('<br />')
                if jd.get('cv_addr3'):
                    wr(jd.get('cv_addr3'))
                    wr('<br />')
                if jd.get('cv_city'):
                    wr(jd.get('cv_city'))
                if jd.get('cv_state'):
                    if jd.get('cv_city'):
                        wr(', ')
                    wr(jd.get('cv_state'))
                if jd.get('cv_zip'):
                    wr(jd.get('cv_zip'))
                wr('<br />')
                if jd.get('cv_country'):
                    wr(jd.get('cv_country'))
                    wr('<br />')
                if jd.get('cv_email'):
                    wr('Email: <a href="mailto:%s">%s</a>' % (jd.get('cv_email'), jd.get('cv_email')))
                    wr('<br />')
                if jd.get('cv_phone'):
                    wr('Phone: %s' % jd.get('cv_phone'))
                    wr('<br />')
                if jd.get('cv_fax'):
                    wr('Fax: %s' % jd.get('cv_fax'))
                    wr('<br />')
        
                wr('</p>')

        else:
            wr('<h1>Oops!</h1>')
            wr('<p>')
            wr('We just began using our new dynamic Jobs management system. It seems that job ID number is no longer available. Please <a href="/Jobs/Index">visit the main job listing</a> to review available positions.')
            wr('</p>')
