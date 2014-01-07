from Template_Admin import Template_Admin
from z_forms import hidden, text, submit
from z_news import get_news_item, save_news

class Action_Form (Template_Admin):
    def title(self):
        id = self.request().fields().get('id')
        if id: return 'Edit Action Item'
        else: return 'Add Action Item'

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
            if form.get('actionitem') == 'true':
                redir = "Action"
            save_news(form)
            self.response().sendRedirect(redir)
        else:
            wr('<form action="Action_Form" method="POST">')
            nii = {}
            if id:
                nii = get_news_item(id)
                wr(hidden('id', nii.get('id')))
            wr(hidden('username', username))
            wr(hidden('actionitem', 'true'))
            wr('<P>')
            wr('<b>Headline</b>')
            wr('<br />')
            wr(text('headline', value=nii.get('headline', ''), clss='input'))
            wr('</P>')

            wr('<P>')
            wr('<b>Description</b>')
            wr('<br />')
            wr('<textarea name="description" class="input" rows="8" cols="48" >%s</textarea>' % (nii.get('description', '')))
            wr('</P>')

            wr(submit('Save & Publish Action Item'))

            wr('</form>')

