from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_news import get_action_items

class Action (Template_Authenticated):
    def title(self):
        return 'ACVAA Action Items'

    def writeContent(self):
        wr = self.writeln

        IS_SITE_ADMIN = is_site_admin(self.request())
        if IS_SITE_ADMIN:
            wr('<div class="button">')
            wr('<a href="Action_Form">+ Add Action Item</a>')
            wr('</div>')

        wr('<h1>%s</h1>' % (self.title()))

        newsitems = get_action_items()

        if newsitems:
            for nd in newsitems:
                ndid = nd.get('id')
                wr('<h2>%s</h2>' % (nd.get('headline')))
                wr('<small>Added %s</small>' % (nd.get('added')))
                if IS_SITE_ADMIN:
                    wr('<a href="../Action_Form?id=%s" style="margin-left: 10px;"><img src="/g/edit.png" alt="edit" width="17" height="17" border="0" /></a>' % (nd.get('id')))
                    wr('<a href="../Action_Delete?id=%s"><img src="/g/delete.png" alt="delete" width="17" height="17" border="0" /></a>' % (nd.get('id')))
                wr('<p>%s</p>' % (nd.get('description')))
        else:
            wr('<h3>Sorry, there aren\'t any action items right now.</h3>')
