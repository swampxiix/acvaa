from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_docmgmt import get_all_possible_categories, MASTER_ROLES_LIST, \
    save_doc_file

class Testing (Template_Authenticated):

    def title(self):
        return 'Testing'

    def writeContent(self):
        wr = self.writeln
        wr('''
<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="NDCABTKMY694A">
<input type="image" src="http://www.acvaa.org/g/btn_payduesCC_LG.png" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
<img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
</form>

        ''')
