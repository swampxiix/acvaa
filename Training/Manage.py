import urllib
from acva.Template_RTC import Template_RTC
from acva.z_forms import text, submit
from z_rtc import get_rtc_categories, get_rtc_name_map

class Manage (Template_RTC):
    def title(self):
        return 'Resident Training Resource Management'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>Resource Categories</h1>')

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
        else:
            wr('<P>There are currently no resource categories.</P>')
