from Template_Main import Template_Main
from z_account import is_site_admin
from z_constants import BASEDIR, rP, wP
import os, time

LINKFILE = os.path.join(BASEDIR, 'links.pick')

class Links (Template_Main):
    def title(self):
        return 'Links to Relevant Websites'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        ISA = is_site_admin(self.request())
        wr('<h1>%s</h1>' % (self.title()))
        linksdict = rP(LINKFILE)

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = qs
            u = form.get('url')
            if not u.startswith('http://'):
                form['url'] = 'http://' + u
            linkid = str(int(time.time()))
            
            linksdict[linkid] = form
            wP(linksdict, LINKFILE)
            self.response().sendRedirect("Links")

        else:
            if qs.get('delete_link_id'):
                timeid = qs['delete_link_id']
                
                del linksdict[qs.get('delete_link_id')]
                wP(linksdict, LINKFILE)
                self.response().sendRedirect("Links")

            else: # display
                if ISA:
                    wr('<P><table>')
                    wr('<form action="Links" method="POST"><tr><td colspan="2"><b>Add Link</b><br>')
                    wr('<tr><td>Title to display:<td><input type="text" name="title" value=""><br>')
                    wr('<tr><td>Web Address:<td><input type="text" name="url" value=""><br>')
                    wr('<tr><td colspan="2"><input type="submit" value="Add Link">')
                    wr('</table></form>')
                    wr('</P>')
                
                if linksdict:
                    titlesandids = []
                    for timeid in linksdict.keys():
                        d = linksdict[timeid]
                        t = (d.get('title'), timeid)
                        titlesandids.append(t)
                    titlesandids.sort()

                    for title, timeid in titlesandids:
                        url = linksdict[timeid].get('url')
                        wr('<P><a href="%s">%s</a>' % (url, title))
                        if ISA:
                            wr('<a href="Links?delete_link_id=%s"><img src="/g/delete.png" alt="delete" width="17" height="17" border="0" /></a>' % (timeid))
                        wr('</P>')
                else:
                    wr('<P>Sorry, there are no links right now.</P>')



