import os.path
from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_constants import DIPLSTR
from z_docs import get_doc_dict, get_archive_list

class Documents (Template_Authenticated):
    def title(self):
        qs = self.request().fields()
        show_archives = qs.get('archive')
        if show_archives:
            return "Archived Documents"
        else:
            return "Documents &amp; Forms"

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        category = qs.get('cat')
        show_archives = qs.get('archive')

        if category:
            ISA = is_site_admin(self.request())
            rolestr = self.request().cookies().get('role', '')
            IS_DIP = rolestr == DIPLSTR
            document_type = 'document'

            # THIS IS A HACK - SHOULD BE CLEANED UP
            if category == 'candidates':
                category = 'residents'
            page_title = '%s for %s' % (self.title(), category.capitalize())
            wr('<h1>%s</h1>' % (page_title))
            # RESET THE STUPID HACK
            if category == 'residents':
                category = 'candidates'

            if not show_archives:
                wr('''
<div class="sb"><div class="st">
<a href="Documents?cat=%s&archive=true">Archived Documents</a>
</div></div>
                ''' % (category))

            if ISA:
                if not show_archives:
                    thispath = self.request().environ().get('REQUEST_URI')
                    wr('<h2>Add a Document</h2>')
                    wr('<form method="POST" action="File_Uploader" enctype="multipart/form-data">')
                    wr('<table>')
                    wr('<input type="hidden" name="filetype" value="document">')
                    wr('<input type="hidden" name="redir" value="%s">' % (thispath))
                    wr('<input type="hidden" name="category" value="%s">' % (category))
                    wr('<tr><td>Title:<td><input type="text" name="title" value=""><br />')
                    wr('<tr><td>File:<td><input type="file" name="datafile"><br />')
                    wr('<tr><td><td><input type="submit" value="Upload">')
                    wr('</table>')
                    wr('</form>')

            VIEW_OK = False
            if category == 'candidates':
                VIEW_OK = True
            if category == 'diplomates':
                if IS_DIP:
                    VIEW_OK = True

            if VIEW_OK:
                if not show_archives:
                    if category == 'diplomates':
                        wr('<h3><a href="/Constitution">ACVAA Constitution &amp; Bylaws</a></h3>')

                subdir, dd = get_doc_dict(dtype=document_type, dcat=category)
                archive_list = get_archive_list(document_type, category)
                ddr = {}

                for k in dd.keys():
                    if show_archives: # include only archived file names
                        if k in archive_list:
                            v = dd[k]
                            ddr[v] = k
                    else: # include only non-archived file names
                        if k not in archive_list:
                            v = dd[k]
                            ddr[v] = k
                ks = ddr.keys()
                ks = sorted(ks, key=lambda x: (x.isdigit() and float(x)) or x.lower())
                for k in ks:
                    v = ddr.get(k)
                    wr('<p><h3><a href="/docs/%s/%s">%s</a></h3>Filename: %s' % (subdir, v, k, v))
                    uri1 = 'File_Deleter?doctype=%s&category=%s&filename=%s' % (document_type, category, v)
                    uri2 = 'File_Archiver?doctype=%s&category=%s&filename=%s' % (document_type, category, v)
                    uri3 = 'File_Archiver?doctype=%s&category=%s&filename=%s&restore=true' % (document_type, category, v)
                    if ISA:
                        if show_archives:
                            wr('<span style="margin-left: 10px;"><a href="%s" title="Restore"><i class="fa fa-check-circle fa-fw"></i></a>' % (uri3))
                        else:
                            wr('<span style="margin-left: 10px;"><a href="%s" title="Archive"><i class="fa fa-archive fa-fw"></i></a>' % (uri2))
                        wr('<a href="%s" title="Delete"><i class="fa fa-trash fa-fw"></i></a></span>' % (uri1))
                    if os.path.splitext(v)[-1] in (".doc", ".docx"):
                        wr('<br /><img src="/g/word_icon.png"> Microsoft Word')
                    if os.path.splitext(v)[-1] in (".xls", ".xlsx"):
                        wr('<br /><img src="/g/excel_icon.png"> Microsoft Excel')
                    if os.path.splitext(v)[-1] in (".pdf"):
                        wr('<br /><img src="/g/pdf_icon.png"> Adobe PDF')
                    wr('</p>')
            else:
                wr('You are not logged in as a diplomate.')
        else:
            wr('<p>No category.</p>')
