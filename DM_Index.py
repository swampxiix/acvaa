from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_docmgmt import get_archived, get_categories, get_access, get_titles, \
    get_all_possible_categories, MASTER_ROLES_LIST


class DM_Index (Template_Authenticated):

    def title(self):
        return 'Document Management'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % self.title())
        ISA = is_site_admin(self.request())
        if ISA:
            wr('<a href="DM_Edit_Categories" class="btn btn-default btn-sm"><i class="fa fa-pencil">&nbsp;</i>Edit Categories</a>')
            wr('<h2>All Existing Documents</h2>')

            filename_title_dict = get_titles()
            cat_filelist_dict = get_categories()
            role_filelist_dict = get_access()
            arch_filelist = get_archived()

            title_filename_dict = {}
            for filename in filename_title_dict.keys():
                title = filename_title_dict.get(filename)
                title_filename_dict[title] = filename
            tfdk = title_filename_dict.keys()
            tfdk.sort()
            wr('<table><tr><th>Title<th>Filename<th>Categories<th>Access<th>Archived')
            count = 1
            for title in tfdk:
                filename = title_filename_dict.get(title)
                self.write('<tr')
                if not count % 3:
                    self.write(' style="background-color: #ECECEC;"')
                self.write('>')
                wr('<td>%s<td>%s' % (title, filename))

                my_cats = []
                for C in get_all_possible_categories():
                    filelist = cat_filelist_dict.get(C, [])
                    if filename in filelist:
                        my_cats.append(C)
                my_cats.sort()
                wr('<td>')
                wr(', '.join(my_cats))

                my_rols = []
                for R in MASTER_ROLES_LIST:
                    filelist = role_filelist_dict.get(R, [])
                    if filename in filelist:
                        my_rols.append(R)
                my_rols.sort()
                wr('<td>')
                wr(', '.join(my_rols))

                wr('<td style="text-align: right;">')
                if filename in arch_filelist:
                    wr('Yes <a href="DM_Archiver?fn=%s&action=activate" class="btn btn-default btn-sm" title="Make this doc active"><i class="fa fa-check-circle"></i></a>' % (filename))
                else:
                    wr('<a href="DM_Archiver?fn=%s&action=archive" class="btn btn-default btn-sm" title="Move to archive"><i class="fa fa-archive"></i></a>' % (filename))

                wr('<td><a href="" class="btn btn-default btn-sm" title="Edit"><i class="fa fa-pencil"></i></a>')
                wr('<td><a href="" class="btn btn-default btn-sm" title="Delete"><i class="fa fa-trash"></i></a>')

                count += 1
            wr('</table>')

