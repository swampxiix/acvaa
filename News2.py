from Template_Main import Template_Main
from z_account import is_site_admin
from z_news import now_year, get_archive_years, get_news_by_year

# !!! search News2 replace News

class News2 (Template_Main):
    def title(self):
        qs = self.request().fields()
        year = qs.get('yr')
        if not year:
            year = now_year()
        return 'ACVA %s News' % (year)

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        year = qs.get('yr')

        IS_SITE_ADMIN = is_site_admin(self.request())
        if IS_SITE_ADMIN:
            wr('<div class="button">')
            wr('<a href="News_Form">+ Add News Item</a>')
            wr('</div>')

        wr('<h1>%s</h1>' % (self.title()))

        archyrs = get_archive_years()
        wr('<div class="sb"><div class="st">')
        wr('<div class="t12b">News Archives</div>')
        ny = now_year()
        if year and (year != ny):
            wr('<P><a href="News2">Current News (%s)</a></P>' % (ny))
        for ay in archyrs:
            fw = "normal"
            if year == ay:
                fw = "bold"
            wr('<P style="font-weight: %s;"><a href="?yr=%s">%s</a></P>' % (fw, ay, ay))
        wr('</div></div>')

        newsitems = get_news_by_year(year)
        for nd in newsitems:
            wr('<h2>%s</h2>' % (nd.get('headline')))
            wr('<small>Added %s</small>' % (nd.get('added')))
            if IS_SITE_ADMIN:
                wr('<a href="News_Form?id=%s" style="margin-left: 10px;"><img src="/g/edit.png" alt="edit" width="17" height="17" border="0" /></a>' % (nd.get('id')))
                wr('<a href="News_Delete?id=%s"><img src="/g/delete.png" alt="delete" width="17" height="17" border="0" /></a>' % (nd.get('id')))
            wr('<p>%s</p>' % (nd.get('description')))






