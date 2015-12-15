from Template_RTC import Template_RTC
from z_rtc import does_file_exist, add_resource

class Resource_Add (Template_RTC):
    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            form = self.request().fields()

            ERROR = []
            reqd = ['category', 'title']
            for k in reqd:
                if not form.get(k):
                    ERROR.append('You must specify a %s.' % (k))

            fobj = form.get('datafile')
            try:
                contents, filename = fobj.value, fobj.filename
                form['filename'] = filename
                form['contents'] = contents
            except:
                pass

            del form['datafile']

            if form.get('filename'):
                conflict = does_file_exist(form.get('filename'))
                if conflict:
                    ERROR.append('A resource already exists that points to a local file with the same name.')
            else: # no upload
                if not form.get('url'): # no url
                    ERROR.append('You must either upload a file, or specify a web address.')

            if ERROR:
                for line in ERROR:
                    wr('<h1 class="error">%s</h1>' % (line))
                wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')
            else:
                add_resource(form)
                self.response().sendRedirect('Index')



