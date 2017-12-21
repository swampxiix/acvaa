from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_docmgmt import get_titles, get_document_properties

class DM_Index (Template_Authenticated):

    def title(self):
        return 'Document Management'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % self.title())
        ISA = is_site_admin(self.request())
        if ISA:
            wr('<p><a href="DM_Add_Edit_Doc" class="btn btn-default btn-sm"><i class="fa fa-plus">&nbsp;</i>New Document</a>')
            wr('<a href="DM_Edit_Categories" class="btn btn-default btn-sm"><i class="fa fa-pencil">&nbsp;</i>Edit Categories</a></p>')
            wr('<h2>All Existing Documents</h2>')

            filename_title_dict = get_titles()

            title_filename_dict = {}
            for filename in filename_title_dict.keys():
                title = filename_title_dict.get(filename)
                title_filename_dict[title] = filename
            tfdk = title_filename_dict.keys()
            tfdk.sort()
            wr('<table><tr><th>Title<th>Filename<th>Categories<th>Access<th>Archived')
            count = 0
            for title in tfdk:
                filename = title_filename_dict.get(title)
                pick = get_document_properties(filename)
                self.write('<tr')
                if not count % 2:
                    self.write(' style="background-color: #ECECEC;"')
                self.write('>')
                wr('<td>%s<td>%s' % (title, filename))
                wr('<td>')
                wr('<br>'.join(pick.get('categories')))
                wr('<td>')
                wr('<br>'.join(pick.get('roles')))

                wr('<td style="text-align: right;">')
                if pick.get('is_archived'):
                    wr('Yes <a href="DM_Archiver?fn=%s&action=activate" class="btn btn-default btn-sm" title="Make this doc active"><i class="fa fa-check-circle"></i></a>' % (filename))
                else:
                    wr('<a href="DM_Archiver?fn=%s&action=archive" class="btn btn-default btn-sm" title="Move to archive"><i class="fa fa-archive"></i></a>' % (filename))

                wr('<td><a href="DM_Add_Edit_Doc?fn=%s" class="btn btn-default btn-sm" title="Edit"><i class="fa fa-pencil"></i></a>' % (filename))
                wr('<td><a href="DM_Delete_Doc?fn=%s" class="btn btn-default btn-sm" title="Delete"><i class="fa fa-trash"></i></a>' % (filename))

                count += 1
            wr('</table>')

