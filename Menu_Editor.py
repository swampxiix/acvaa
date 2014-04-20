from Template_Admin import Template_Admin
from z_constants import menu_alltop, menu_admin, menu_dips, menu_cands, menu_allbottom, \
    rText, wText

class Menu_Editor (Template_Admin):
    def title(self):
        return "Menu Editor"

    def writeContent(self):
        wr = self.writeln

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()
            for fullpath in form.keys():
                text_to_write = form[fullpath]
                wText(text_to_write, fullpath)
            wr('<h3>Changes saved.</h3>')

        wr('<h1>%s</h1>' % (self.title()))
        wr('<P>Make changes to the various menu sections here.</P>')
        wr('<form action="Menu_Editor" method="POST">')
        wr('<h2>Public Section: Top</h2>')
        wr('<div>Everyone will be able to view this section.</div>')
        file1 = menu_alltop
        menu1 = rText(file1)
        wr('<textarea rows="10" cols="80" name="%s" style="margin-bottom: 30px;">%s</textarea>' % (file1, menu1))

        wr('<h2>Admin Section</h2>')
        wr('<div>Only administrators will be able to view this section.</div>')
        file2 = menu_admin
        menu2 = rText(file2)
        wr('<textarea rows="10" cols="80" name="%s" style="margin-bottom: 30px;">%s</textarea>' % (file2, menu2))

        wr('<h2>Diplomate Section</h2>')
        wr('<div>Administrators &amp; Diplomates will be able to view this section.</div>')
        file3 = menu_dips
        menu3 = rText(file3)
        wr('<textarea rows="10" cols="80" name="%s" style="margin-bottom: 30px;">%s</textarea>' % (file3, menu3))

        wr('<h2>Candidate Section</h2>')
        wr('<div>Administrators, Diplomates &amp; Candidates will be able to view this section.</div>')
        file4 = menu_cands
        menu4 = rText(file4)
        wr('<textarea rows="10" cols="80" name="%s" style="margin-bottom: 30px;">%s</textarea>' % (file4, menu4))

        wr('<h2>Public Section: Bottom</h2>')
        wr('<div>Everyone will be able to view this section.</div>')
        file5 = menu_allbottom
        menu5 = rText(file5)
        wr('<textarea rows="10" cols="80" name="%s" style="margin-bottom: 30px;">%s</textarea>' % (file5, menu5))

        wr('<div><input type="submit" value="Save Menu Sections">')
        wr('<input type="button" value="Cancel" onClick="javascript:history.go(-1)"></div>')

        wr('</form>')
