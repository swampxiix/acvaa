from Template_Admin import Template_Admin
from z_forms import hidden, submit
from z_news import get_news_item, delete_news_item

class News_Delete (Template_Admin):
    def title(self):
        return 'Confirm News Item Deletion'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        id = qs.get('id')

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = qs
            ntype, redir = 'news', "News"
            if form.get('annual') == '1':
                ntype, redir = 'annual', "Annual"
            delete_news_item(id, ntype)
            self.response().sendRedirect(redir)

        else:
            wr('<form action="News_Delete" method="POST">')
            wr(hidden('id', id))
            if qs.get('annual') == '1':
                wr(hidden('annual', '1'))
            nii = get_news_item(id)

            wr('<h1>Are you sure you want to delete this news item?</h1>')
            wr('<h3>You cannot undo this operation.</h3>')

            wr('<h2>%s</h2>' % (nii.get('headline')))
            wr('<p>%s</p>' % (nii.get('description')))

            wr(submit('Delete News Item'))
            wr('</form>')
