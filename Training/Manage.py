import urllib
from acva.Template_RTC import Template_RTC
from acva.z_forms import text, submit, select
from z_rtc import get_rtc_categories, get_rtc_name_map

class Manage (Template_RTC):
    def title(self):
        return 'Resident Training Resource Management'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))

        wr('<h2>Resource Categories</h2>')
        wr('<form action="Category_Add" method="POST">')
        wr('<b>Add Category</b>:')
        wr(text('new_category'))
        wr(submit('Add New Category'))
        wr('</form>')

        catdict = get_rtc_categories()
        mapdict = get_rtc_name_map()

        if catdict and mapdict:
            catguids = catdict.keys()
            wr('<P><table>')
            wr('<tr><th>Category<th>Count<th><th>')
            for guid in catguids:
                catname = mapdict.get(guid, '')
                # Guard against weird characters in URL
                querystring = urllib.urlencode({'cat':catname})
                rezlist = catdict.get(guid, [])
                rezcount = len(rezlist)
                wr('<tr><td>%s' % (catname))
                wr('<td>%s' % (rezcount))
                wr('<td><a href="Category_Edit?%s" title="Edit"><i class="fa fa-pencil"></i></a>' % (querystring))
                wr('<td>')
                if rezcount > 0:
                    pass
                else:
                    wr('<a href="Category_Delete?%s" title="Delete"><i class="fa fa-trash"></i><a>' % (querystring))
            wr('</table></P>')
            wr('<h2>Add a Training Resource</h2>')
            wr('<form action="Resource_Add" method="POST" enctype="multipart/form-data"><table>')
            catnames = mapdict.values()
            catnames.sort()
            wr('<tr><td>Category:<td>')
            wr(select('category', catnames))
            wr('<td class="req">required')
            wr('<tr><td>Title:<td>')
            wr(text('title'))
            wr('<td class="req">required')
            wr('<tr><td colspan="6" class="req">You must either upload a file, or provide a web address for this resource.<br>You can do both.')
            wr('<tr><td>File Upload:<td><input type="file" name="datafile">')
            wr('<tr><td>Web Address:<td>%s' % (text('url')))
            wr('<tr><td>Description:<td><textarea name="description"></textarea>')
            wr('<td class="req">optional')
            wr('<tr><td colspan="3">%s' % (submit('Add Resource')))
            wr('</table></form>')
            
        else:
            wr('<P>There are currently no resource categories.</P>')
            wr('<P>You cannot add a resource without first creating a category for it.</P>')
