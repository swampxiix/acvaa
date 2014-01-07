from acva.Template_Authenticated import Template_Authenticated
from acva.z_account import is_site_admin
from acva.z_docs import get_doc_dict
from acva.z_times import get_year
import os.path

class Index (Template_Authenticated):
    def title(self):
        return 'ACVAA Annual Reports'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        category = qs.get('cat', '')
        viewyear = qs.get('yr', str(get_year()))
        ISA = is_site_admin(self.request())
        document_type = 'report'

        subdir, dd = get_doc_dict(dtype=document_type, dcat='')
        ddr = {}
        for k in dd.keys():
            v = dd[k]
            ddr[v] = k

        startyear, years = 2009, {}
        for y in range(startyear, get_year()+1):
            year = str(y)
            years[year] = {}
            for k in ddr.keys():
                if year in k:
                    years[year][k] = ddr[k]
        yks = years.keys()
        yks = sorted(yks, key=lambda x: (x.isdigit() and float(x)) or x.lower())
        yks.reverse()
        wr('<div class="sb"><div class="st">')
        wr('<div class="t12b">Report Archives</div>')
        for yr in yks:
            wr('<P class="t12"><a href="Index?yr=%s">%s</a>: %s reports</P>' % (yr, yr, len(years.get(yr))))
        wr('</div></div>')


        wr('<h1>%s</h1>' % (self.title()))

        if ISA:
            thispath = self.request().environ().get('REQUEST_URI')
            wr('<h3>Add a Document</h3>')
            wr('<form method="POST" action="../File_Uploader" enctype="multipart/form-data">')
            wr('<table>')
            wr('<input type="hidden" name="filetype" value="report">')
            wr('<input type="hidden" name="redir" value="%s">' % (thispath))
            wr('<tr><td>Title:<td><input type="text" name="title" value=""><br />')
            wr('<tr><td>File:<td><input type="file" name="datafile"><br />')
            wr('<tr><td><td><input type="submit" value="Upload">')
            wr('</table>')
            wr('</form>')

        wr('<h2 style="margin-top: 20px;">%s</h2>' % (viewyear))

        viewyear_reports =  years.get(viewyear, {})
        if viewyear_reports:
            ks = viewyear_reports.keys()
            ks = sorted(ks, key=lambda x: (x.isdigit() and float(x)) or x.lower())
    
            for k in ks:
                v = ddr.get(k)
                wr('<p><h3><a href="/docs/%s/%s">%s</a></h3>Filename: %s' % (subdir, v, k, v))
                uri = '/File_Deleter?doctype=%s&category=%s&filename=%s' % (document_type, category, v)
                if ISA:
                    wr('<a href="%s"><img src="/g/delete.png" alt="delete" width="17" height="17" border="0" /></a>' % (uri))
                if os.path.splitext(v)[-1] in (".doc", ".docx"):
                    wr('<br /><img src="/g/word_icon.png"> Microsoft Word download')
                if os.path.splitext(v)[-1] in (".xls", ".xlsx"):
                    wr('<br /><img src="/g/excel_icon.png"> Microsoft Excel download')
                wr('</p>')
        else:
            wr('<h3>Sorry there aren\'t any reports for this year.</h3>')
