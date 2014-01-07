from Template_Admin import Template_Admin
from z_forms import hidden, submit
from z_news import get_news_item, delete_news_item

class Action_Delete (Template_Admin):
    def title(self):
        return 'Confirm Action Item Deletion'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        id = qs.get('id')

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = qs
            delete_news_item(id, "actionitem")
            self.response().sendRedirect("Action")

        else:
            wr('<form action="Action_Delete" method="POST">')
            wr(hidden('id', id))
            nii = get_news_item(id)

            wr('<h1>Are you sure you want to delete this action item?</h1>')
            wr('<h3>You cannot undo this operation.</h3>')

            wr('<h2>%s</h2>' % (nii.get('headline')))
            wr('<p>%s</p>' % (nii.get('description')))

            wr(submit('Delete Action Item'))
            wr('</form>')
