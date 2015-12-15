from acva.Template_Authenticated import Template_Authenticated
from acva.z_account import is_rtc
from z_rtc import get_resources

class Index (Template_Authenticated):

    def addStyleSheet(self):
        self.writeln('''
<link rel="stylesheet" href="/c/bootstrap-sortable.css" type="text/css">
        ''')

    def addJavaScript(self):
        self.writeln('''
<script type="text/javascript" src="/js/moment.min.js"></script>
<script type="text/javascript" src="/js/bootstrap-sortable.js"></script>
        ''')

    def title(self):
        return 'ACVAA Resident Training Resources'

    def writeContent(self):
        wr = self.writeln
        if is_rtc(self.request()):
            wr('<div class="button" style="margin-top: 10px;">')
            wr('<a href="Manage">Resource Mgmt.</a>')
            wr('</div>')
        wr('<h1>%s</h1>' % (self.title()))

        allrez = get_resources()
        if allrez:
            wr('''
<P>
<table class="table-striped sortable">
<thead>
<tr style="border-bottom: 1px solid #CCC;">
<th data-defaultsort="asc">Title</th>
<th>Category</th>
<th>Download</th>
<th>Link</th>
<th class="col-md-4">Description</th>
            ''')
            if is_rtc(self.request()):
                wr('<th></th>')

            wr('''
</tr>
</thead>
<tbody>
            ''')
            for rez in allrez:
                wr('<tr style="border-bottom: 1px solid #CCC;">')
                wr('<td>%s</td>' % (rez.get('title')))
                wr('<td>%s</td>' % (rez.get('category')))
                wr('<td>')
                if rez.get('filename'):
                    fileext = rez.get('filename').split('.')[-1]
                    wr('<a href="files/%s" title="%s">' % (rez.get('filename'), rez.get('filename')))
                    wr(fileext.upper())
                    if rez.get('filesize'):
                        wr(' (%s)</a>' % (rez.get('filesize')))
                else:
                    wr('&nbsp;')
                wr('</td>')
                wr('<td>')
                if rez.get('url'):
                    wr('<a href="%s">Web link</a>' % (rez.get('url')))
                else:
                    wr('&nbsp;')
                wr('</td>')
                wr('<td>%s</td>' % (rez.get('description')))
                if is_rtc(self.request()):
                    wr('<td>')
                    wr('''
<a href=""><i class="fa fa-pencil"></i></a>&nbsp;&nbsp;<a href=""><i class="fa fa-trash"></i></a>
                    ''')

                    wr('</td>')



                wr('</tr>')
            wr('''
</tbody>
</table>
</P>
            ''')

        else:
            wr('<P>No training resources exist at this moment.</P>')

