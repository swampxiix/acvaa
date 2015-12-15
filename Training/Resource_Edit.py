from Template_RTC import Template_RTC
from acva.z_forms import text, submit, select, hidden
from z_rtc import does_file_exist, get_rtc_name_map, get_resource_by_id, get_category_by_guid, edit_resource

class Resource_Edit (Template_RTC):
    def title(self):
        return 'Edit Training Resource'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()

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

            if form.get('url'):
                pass
            else: # no URL
                if not form.get('filename'): # no upload
                    if form.get('oldfilename'): # previously existed
                        pass
                    else: # no prev. file
                        ERROR.append('You must either upload a file, or specify a web address.')

            if ERROR:
                for line in ERROR:
                    wr('<h1 class="error">%s</h1>' % (line))
                wr('<P>Please <a href="javascript:history.go(-1)">go back</a> &amp; try again.</P>')
            else:
                edit_resource(form)
                self.response().sendRedirect('Index')

        else:
            wr('<h1>%s</h1>' % (self.title()))

            mapdict = get_rtc_name_map()
            rezid = qs.get('id')
            pick = get_resource_by_id(rezid)

            wr('<P><form action="Resource_Edit" method="POST" enctype="multipart/form-data"><table>')
            wr(hidden('id', pick.get('id')))

            catnames = mapdict.values()
            catnames.sort()
            rezcatid = pick.get('category')
            rezcatname = get_category_by_guid(rezcatid)
            wr('<tr><td>Category:<td>')
            wr(hidden('oldcategory', rezcatname))
            wr(select('category', catnames, selected=rezcatname))
            wr('<td class="req">required')
            wr('<tr><td>Title:<td>')
            wr(text('title', pick.get('title')))
            wr('<td class="req">required')
            if pick.get('filename'):
                wr('<tr><td>Current File:<td><a href="files/%s">%s</a>' % (pick.get('filename'), pick.get('filename')))
                wr(hidden('oldfilename', pick.get('filename')))
            wr('<tr><td>Replace File:<td><input type="file" name="datafile"><td class="req">old file will be deleted')
            wr('<tr><td>Web Address:<td>%s' % (text('url', pick.get('url'))))
            wr('<tr><td>Description:<td><textarea name="description">%s</textarea>' % (pick.get('description')))
            wr('<td class="req">optional')
            wr('<tr><td colspan="3">%s' % (submit('Edit Resource')))
            wr('</table></form></P>')
