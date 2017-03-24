from Comm_Tmpl import Comm_Tmpl
from acva.z_account import is_site_admin
from z_comm import get_committee_order, get_committee_info, \
    get_members_order, get_members

class Index (Comm_Tmpl):
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
            wr('<a href="Committee_Form">Add Committee</a>')
            wr('</div>')

        wr('<a name="top"></a>')
        wr('<h1>%s</h1>' % (self.title()))

        wr('<table class="comm">')
        comm_order = get_committee_order()
        for comm_id in comm_order:
            comm_info = get_committee_info(comm_id)
            wr('<tr><th colspan="4">%s' % (comm_info.get('name')))

            if IS_SITE_ADMIN:
                wr('&nbsp;&nbsp;<a href="Edit_Form?comm_id=%s"><i class="fa fa-pencil" style="color: #647382;"></i></a>&nbsp;&nbsp;' % (comm_id))
                wr('<a href="Reorder?comm_id=%s&dir=up"><i class="fa fa-arrow-up" style="color: #647382;"></i></a>&nbsp;&nbsp;' % (comm_id))
                wr('<a href="Reorder?comm_id=%s&dir=down"><i class="fa fa-arrow-down" style="color: #647382;"></i></a>' % (comm_id))

            mbo = get_members_order(comm_id)
            mbds = get_members(comm_id)

            for mb_id in mbo:
                mb_dict = mbds.get(mb_id)
                wr('<tr>')
                for k in ['name', 'title', 'email', 'year']:
                    wr('<td>')
                    if k == 'email':
                        wr('<small><a href="mailto:%s">%s</a></small>' % (mb_dict.get(k), mb_dict.get(k)))
                    else:
                        wr(mb_dict.get(k))



        wr('</table>')




