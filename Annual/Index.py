from acva.Template_Main import Template_Main
from acva.z_account import is_site_admin
from acva.z_news import get_annual_news

class Index (Template_Main):
    def title(self):
        return 'ACVAA Annual Meeting'

    def writeContent(self):
        wr = self.writeln

        IS_SITE_ADMIN = is_site_admin(self.request())
        if IS_SITE_ADMIN:
            wr('<div class="button">')
            wr('<a href="../News_Form?annual=1">+ Add News Item</a>')
            wr('</div>')

        wr('<h1>%s</h1>' % (self.title()))

        newsitems = get_annual_news()

        wr('''
            <div class="flt_r">
            <img src="/g/annual_mtg.jpg" width="200" height="169" alt="2011 ACVAA Annual Meeting" border="0" />
            </div>
            ''')

        if newsitems:
            for nd in newsitems:
                ndid = nd.get('id')
                wr('<h2>%s</h2>' % (nd.get('headline')))
                if ndid != '9999999999': # we use 9999999999 to pin the details item to the top of the page
                    wr('<small>Added %s</small>' % (nd.get('added')))
                if IS_SITE_ADMIN:
                    wr('<a href="../News_Form?id=%s&annual=1" style="margin-left: 10px;"><img src="/g/edit.png" alt="edit" width="17" height="17" border="0" /></a>' % (nd.get('id')))
                    wr('<a href="../News_Delete?id=%s&annual=1"><img src="/g/delete.png" alt="delete" width="17" height="17" border="0" /></a>' % (nd.get('id')))
                wr('<p>%s</p>' % (nd.get('description')))
        else:
            wr('<h3>Sorry, there aren\'t any news items for the annual meeting yet.</h3>')

