from acva.Template_Main import Template_Main

from acva.z_constants import JOB_CATS, compnum
from acva.z_account import is_site_admin
from time import strftime
from z_jobs import get_jobs_by_cat, is_expired

synonyms = {'Institution, Industry or Private Practice': ['Institution, Industry or Public Practice']}

class Index (Template_Main):
    def title(self):
        return 'Jobs & Available Positions'

    def writeContent(self):
        wr = self.writeln
        IS_ADMIN = is_site_admin(self.request())
        if IS_ADMIN:
            wr('<div class="button">')
            wr('<a href="Job_Form">+ Add Job</a>')
            wr('</div>')

        wr('<h1>%s</h1>' % (self.title()))
        wr('<div class="sb"><div class="st"><div class="t12b">Job Categories</div>')
        for c in JOB_CATS:
            bookmark = c.split(',')[0].lower()
            wr('<p><a href="#%s">%s</a></p>' % (bookmark, c))
        wr('</div></div>')

        JBC = get_jobs_by_cat()

        if self.request().fields().get('sv'):
            self.render_special_msg('Job saved.')

        for c in JOB_CATS:
            wr('<a name="%s"></a>' % (c.split(',')[0].lower()))
            wr('<h2>%s</h2>' % (c))
            deezjobs = JBC.get(c)

            synlist = synonyms.get(c, [])
            for syn in synlist:
                deezjobs = dict(deezjobs, **JBC.get(syn, {}))

            if deezjobs:
                FOUND_GOOD = False
                for jk in deezjobs.keys():
                    m, d, y = deezjobs.get(jk, {}).get('expires', [0,0,0])
                    if not is_expired(m,d,y):
                        FOUND_GOOD = True
                if FOUND_GOOD:
                    djk = deezjobs.keys()
                    djk.sort(compnum)
                    wr('<ol class="dec">')
                    for id in djk:
                        SHOW = False
                        jd = deezjobs.get(id)
                        m, d, y = jd.get('expires', [0,0,0])
                        EXPIRED = is_expired(m,d,y)
                        if EXPIRED:
                            if IS_ADMIN:
                                SHOW = True
                        else:
                            SHOW = True

                        if SHOW:
                            if EXPIRED:
                                wr('<li style="background-color: #DDD; padding: 10px;">')
                            else:
                                wr('<li>')
                            wr('<a href="Display?jid=%s">%s</a><br />' % (id, jd.get('job_title')))
                            wr(jd.get('job_inst'))
                            if jd.get('job_dept'):
                                wr('<br />%s' % (jd.get('job_dept')))
                            wr('<br /><small style="color: #BBB;">Posted: ')
                            wr(strftime("%b. %d, %Y", jd.get('posted')))
                            wr(' &middot; Expires: ')
                            wr(strftime("%b. %d, %Y", jd.get('exp_tuple')))
                            wr('</small>')
                            if IS_ADMIN:
                                wr('<br />')
                                wr('<a href="Job_Form?jid=%s"><img src="/g/edit.png" alt="edit" width="17" height="17" border="0" /></a>' % (id))
                                wr('<a href="Delete_Job?jid=%s"><img src="/g/delete.png" alt="delete" width="17" height="17" border="0" /></a>' % (id))
                            if EXPIRED:
                                wr('<span style="padding-left: 10px; font-weight: bold; color: #F00;">EXPIRED</span>')

                    wr('</ol>')
                else:
                    wr('<p>No positions available at this time.</p>')
            else:
                wr('<p>No positions available at this time.</p>')

