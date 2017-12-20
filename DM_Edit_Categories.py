from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_docmgmt import get_all_possible_categories, is_category_empty, \
    reorder_master_category_list, edit_master_category, remove_master_category

class DM_Edit_Categories (Template_Authenticated):

    def title(self):
        return 'Edit Document Categories'

    def writeContent(self):
        wr = self.writeln
        ISA = is_site_admin(self.request())
        if ISA:
            qs = self.request().fields()
            # Processing
            # Form submission
            if self.request()._environ.get('REQUEST_METHOD') == 'POST':
                if 'action' in qs:
                    if qs.get('action') == 'add':
                        edit_master_category (qs.get('new_cat'))
                        self.response().sendRedirect('DM_Edit_Categories')
                    if qs.get('action') == 'edit':
                        edit_master_category (qs.get('new_cat'), qs.get('old_cat'))
                        self.response().sendRedirect('DM_Edit_Categories')
            # Query string
            else:

                if 'action' in qs:
                    if qs.get('action') == 'reorder':
                        wr('reorder ok')
                        reorder_master_category_list(qs.get('cat'), qs.get('dir'))
                        self.response().sendRedirect('DM_Edit_Categories')
                    if qs.get('action') == 'edit':
                        wr('<h3>Edit Category</h3>')
                        wr('<form action="DM_Edit_Categories" method="POST">')
                        wr('<input type="hidden" name="action" value="edit">')
                        wr('<input type="hidden" name="old_cat" value="%s">' % (qs.get('cat')))
                        wr('<input type="text" name="new_cat" value="%s"><br>' % (qs.get('cat')))
                        wr('<input type="submit" value="Edit Category Name">')
                        wr('</form>')
                    if qs.get('action') == 'delete':
                        remove_master_category(qs.get('cat'))
                        self.response().sendRedirect('DM_Edit_Categories')
                # Display
                else:
                    wr('<h1>%s</h1>' % (self.title()))
                    categories = get_all_possible_categories()
                    wr('<p>Note: You can only delete a category if it is empty, i.e., there are no documents assigned to it.</p>')
                    wr('<h3>Existing Categories</h3>')
                    wr('<table><tr><th>Name<th colspan="2">Reorder')
                    for cat in categories:
                        wr('<tr><td>%s' % (cat))
                        if cat != categories[0]:
                            wr('<td><a href="DM_Edit_Categories?action=reorder&cat=%s&dir=up" title="Move up"><i class="fa fa-arrow-up"></i></a>' % (cat))
                        else:
                            wr('<td>&nbsp;')
                        if cat != categories[-1]:
                            wr('<td><a href="DM_Edit_Categories?action=reorder&cat=%s&dir=dn" title="Move down"><i class="fa fa-arrow-down"></i></a>' % (cat))
                        else:
                            wr('<td>&nbsp;')
                        wr('<td><a href="DM_Edit_Categories?action=edit&cat=%s" title="Edit name"><i class="fa fa-pencil"></i></a>' % (cat))
                        if is_category_empty(cat):
                            wr('<td><a href="DM_Edit_Categories?action=delete&cat=%s" title="Delete"><i class="fa fa-trash"></i></a>' % (cat))
                    wr('<form action="DM_Edit_Categories" method="POST">')
                    wr('<tr><td colspan="9"><h3>Add a New Category</h3>')
                    wr('<input type="hidden" name="action" value="add">')
                    wr('<tr><td colspan="9"><input type="text" name="new_cat" value="">')
                    wr('<tr><td colspan="9"><input type="submit" value="+ Add">')
                    wr('</form>')
                    wr('</table>')
