from Template_Admin import Template_Admin
from z_forms import hidden, text, submit
from z_news import get_news_item, save_news

class News_Form (Template_Admin):
    def title(self):
        id = self.request().fields().get('id')
        if id: return 'Edit News Item'
        else: return 'Add News Item'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        id = qs.get('id')
        username = self.request().cookies().get('username')
        wr('<h1>%s</h1>' % (self.title()))

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = qs
            redir = "News"
            if form.get('annualnews') == 'true':
                redir = "Annual"
            save_news(form)
#            wr(form)
            self.response().sendRedirect(redir)
        else:
            wr('<form action="News_Form" method="POST">')
            nii = {}
            if id:
                nii = get_news_item(id)
                wr(hidden('id', nii.get('id')))
            wr(hidden('username', username))
            wr('<P>')
            wr('<b>Headline</b>')
            wr('<br />')
            wr(text('headline', value=nii.get('headline', ''), clss='input'))
            wr('</P>')
            wr('<P>')
            wr('<lable for="annewsck"><input type="checkbox" name="annualnews" value="true" id="annewsck"')
            if qs.get('annual') == '1':
                wr(' CHECKED')
            wr('> Check this box if this is for the Annual Meeting.</label>')
            wr('</P>')

#             wr('<P>')
#             wr('<b>Who can view this news item?</b>')
#             wr('<br />')
#             self.write('<input type="radio" name="visibility" value="all" id="vizall"')
#             if (nii.get('visibility') == 'all') or (not id):
#                 self.write(' CHECKED ')
#             wr('/> <label for="vizall">Everyone</label>')
#             wr('<br />')
#             self.write('<input type="radio" name="visibility" value="restricted" id="vizres"')
#             if nii.get('visibility') == 'restricted':
#                 self.write(' CHECKED ')
#             wr('/> <label for="vizres">Diplomates &amp; Candidates Only</label>')
#             wr('</P>')

#             wr('<P>')
#             wr('<b>Website</b>')
#             wr('<br />')
#             wr('Is there another website you\'d like this news item linked to? If so, provide its URL here.')
#             wr('<br />')
#             wr(text('url', value=nii.get('url', ''), clss='input'))
#             wr('</P>')

            wr('<P>')
            wr('<b>Description</b>')
            wr('<br />')
            wr('<textarea name="description" class="input" rows="8" cols="48" >%s</textarea>' % (nii.get('description', '')))
            wr('</P>')

            wr(submit('Save & Publish News Item'))

            wr('</form>')

