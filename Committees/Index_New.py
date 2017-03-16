from acva.Template_Authenticated import Template_Authenticated
from acva.z_account import is_site_admin
from z_comm import get_committee_order

class Index_New (Template_Authenticated):
    def title(self):
        return 'ACVAA Committees'

    def writeJavaScript(self):
        wr = self.writeln
        wr('<script src="https://use.fontawesome.com/034a9c2159.js"></script>')

    def writeContent(self):
        wr = self.writeln
        IS_SITE_ADMIN = is_site_admin(self.request())

        if IS_SITE_ADMIN:
            wr('<div class="button">')
            wr('<a href="Add_Committee">Add Committee</a>')
            wr('</div>')

        wr('<a name="top"></a>')
        wr('<h1>%s</h1>' % (self.title()))
        comm_order = get_committee_order()
        for comm_id in comm_order:
            comm_info = get_committee_info(comm_id)
            wr('<h2>%s' % (comm_id.get('name')))
            if IS_SITE_ADMIN:
                wr('<a href="Edit_Form?id=%s"><i class="fa fa-pencil" style="color: #0000FF;"></i></a>' % (comm_id))
            wr('</h2>')
