import os.path
from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_constants import DIPLSTR
from z_docs import get_doc_dict

class Testing (Template_Authenticated):
    def title(self):
        return "Documents &amp; Forms"

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        category = qs.get('cat')

        if category:
            ISA = is_site_admin(self.request())
            rolestr = self.request().cookies().get('role', '')
            IS_DIP = rolestr == DIPLSTR
            document_type = 'document'

            page_title = '%s for %s' % (self.title(), category.capitalize())

            fd = {'page_title': page_title, 'category': category}
            wr('<h1>%s</h1>' % (page_title))

            if ISA:
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

            subdir, dd = get_doc_dict(dtype=document_type, dcat=category)
            ddr = {}
            for k in dd.keys():
                v = dd[k]
                ddr[v] = k
            ks = ddr.keys()
            ks = sorted(ks, key=lambda x: (x.isdigit() and float(x)) or x.lower())
            for k in ks:
                v = ddr.get(k)
                wr('<p><h3><a href="docs/%s/%s">%s</a></h3>Filename: %s' % (subdir, v, k, v))
                uri = 'File_Deleter?doctype=%s&category=%s&filename=%s' % (document_type, category, v)
                wr('<a href="%s"><img src="/g/delete.png" alt="delete" width="17" height="17" border="0" /></a>' % (uri))
                if os.path.splitext(v)[-1] in (".doc", ".docx"):
                    wr('<br /><img src="/g/word_icon.png"> Microsoft Word download')
                if os.path.splitext(v)[-1] in (".xls", ".xlsx"):
                    wr('<br /><img src="/g/excel_icon.png"> Microsoft Excel download')
                wr('</p>')

        else:
            wr('<p>No category.</p>')

