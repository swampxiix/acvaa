from Comm_Tmpl import Comm_Tmpl
from acva.z_account import is_site_admin
from z_comm import delete_committee, rename_committee, add_committee, get_committee_info

class Committee_Form (Comm_Tmpl):
    def title(self):
        return 'Add a Committee'

    def writeContent(self):
        wr = self.writeln
        IS_SITE_ADMIN = is_site_admin(self.request())
        wr('<h1>%s</h1>' % (self.title()))
        if IS_SITE_ADMIN:
            if self.request()._environ.get('REQUEST_METHOD') == 'POST':

                form = self.request().fields()

                if form.get('delete') == '1':
                    comm_id = form.get('comm_id')
                    delete_committee(comm_id)
                    self.response().sendRedirect('Index')
                elif form.get('rename') == '1':
                    comm_id = form.get('comm_id')
                    rename_committee(comm_id, form.get('comm_name'))
                    self.response().sendRedirect('Index')
                else:
                    newname = form.get('comm_name')
                    if newname:
                        this_id = add_committee(newname)
                        redirURL = 'Index'
                    else:
                        redirURL = 'Add_Committee'
                    self.response().sendRedirect(redirURL)

            else:
                qs = self.request().fields()
                comm_id = qs.get('comm_id')
                is_delete = qs.get('delete')
                if comm_id:
                    comm_info = get_committee_info(comm_id)
                    comm_name = comm_info.get('name')
                    if is_delete:
                        wr('<p>Are you sure you want to delete Committee: %s</p>' % (comm_name))
                        wr('<form method="POST" action="Committee_Form">')
                        wr('<input type="hidden" name="comm_id" value="%s">' % (comm_id))
                        wr('<input type="hidden" name="delete" value="1">')
                        wr('<p><input type="submit" value="Yes.">')
                        wr('<input type="button" value="No! Leave this nice Committee alone." onClick="javascript:history.go(-1)"></p>')
                        wr('</form>')
                    else:
                        wr('<form method="POST" action="Committee_Form">')
                        wr('<p><input type="text" name="comm_name" value="%s"></p>' % (comm_name))
                        wr('<input type="hidden" name="comm_id" value="%s">' % (comm_id))
                        wr('<input type="hidden" name="rename" value="1">')
                        wr('<p><input type="submit" value="Rename Product"></p>')
                        wr('</form>')
                else:
                    wr('<form method="POST" action="Committee_Form">')
                    wr('<p><i class="fa fa-plus-circle" style="color: #00CC00;"></i> <input type="text" name="comm_name" value=""></p>')
                    wr('<p><input type="submit" value="Add Committee"></p>')
                    wr('</form>')


        else:
            wr('You must be logged in as an administrator to view this page.')
