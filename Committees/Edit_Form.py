from Comm_Tmpl import Comm_Tmpl
from acva.z_account import is_site_admin
from z_comm import get_committee_info, get_members, add_member, \
    get_members_order, delete_member

class Edit_Form (Comm_Tmpl):

    def title(self):
        return 'Committee Editor'

    def writeContent(self):
        wr = self.writeln
        IS_SITE_ADMIN = is_site_admin(self.request())
        wr('<h1>%s</h1>' % (self.title()))
        if IS_SITE_ADMIN:
            wr('<div class="button">')
            wr('<a href="Index_New">Committees Page</a>')
            wr('</div>')

            if self.request()._environ.get('REQUEST_METHOD') == 'POST':
                form = self.request().fields()
                comm_id = form.get('comm_id')

                if form.get('add_member') == '1':
                    wr(form)
                    mb_name = form.get('member_name')
                    mb_title = form.get('member_title')
                    mb_email = form.get('member_email')
                    mb_year = form.get('member_year')
                    mb_id = add_member(comm_id, mb_title, mb_name, mb_email, mb_year)
                    self.response().sendRedirect('Edit_Form?comm_id=%s' % (comm_id))
                if form.get('delete_member') == '1':
                    comm_id, mb_id = form.get('comm_id'), form.get('mb_id')
                    delete_member(comm_id, mb_id)
                    self.response().sendRedirect('Edit_Form?comm_id=%s' % (comm_id))

            else:
                qs = self.request().fields()
                if qs.get('delete_member') == '1':
                    mbrs = get_members(qs.get('comm_id'))
                    mbr = mbrs.get(qs.get('mb_id')).get('name')
                    wr('<h2>Confirm Deletion</h2>')
                    wr('<form method="POST" action="Edit_Form">')
                    wr('<p>Are you sure that you\'d like to remove %s from this committee?<br><br>' % (mbr))
                    wr('<input type="submit" value="Yes">')
                    wr('<input type="hidden" name="delete_member" value="1">')
                    wr('<input type="hidden" name="comm_id" value="%s">' % (qs.get('comm_id')))
                    wr('<input type="hidden" name="mb_id" value="%s">' % (qs.get('mb_id')))
                    wr('<input type="button" value="No. Leave this person on the committee." onClick="javascript:history.go(-1)">')
                    wr('</p></form>')
                else:
                    comm_id = qs.get('comm_id')
                    comm_info = get_committee_info(comm_id)
                    comm_name = comm_info.get('name')

                    # ==============================================================
                    # Title

                    wr('<h1>%s ' % (comm_name))
                    if IS_SITE_ADMIN:
                        wr('<a href="Committee_Form?comm_id=%s"><i class="fa fa-pencil" style="color: #647382;"></i></a>' % (comm_id))
                        wr('<a href="Committee_Form?comm_id=%s&delete=1"><i class="fa fa-trash" style="color: #647382;"></i></a>' % (comm_id))
                    wr('</h1>')

                    # ==============================================================
                    # Add form

                    wr('<h2>Add a Member</h2>')
                    wr('<form method="POST" action="Edit_Form">')
                    wr('<input type="hidden" name="comm_id" value="%s">' % (comm_id))
                    wr('<input type="hidden" name="add_member" value="1">')
                    wr('<table>')
                    wr('<tr><td>Name: <td><input type="text" name="member_name" value="">')
                    wr('<tr><td>Title: <td><input type="text" name="member_title" value="">')
                    wr('<tr><td>Email: <td><input type="text" name="member_email" value="">')
                    wr('<tr><td>Year: <td><input type="text" name="member_year" value="">')
                    wr('<tr><td><input type="submit" value="Add"></p>')
                    wr('</table>')
                    wr('</form>')
                    mfs = get_members(comm_id)
                    mo = get_members_order(comm_id)
                    if mfs:
                        wr('<h3>Current Members</h3>')
                        wr('<table><th>Name<th>Title<th>Email<th>Year')
                        for mb_id in mo:
                            m_dict = mfs.get(mb_id)
                            wr('<tr>')
                            for k in ['name', 'title', 'email', 'year']:
                                wr('<td>%s' % (m_dict.get(k)))
                            wr('<td><a href="Reorder?comm_id=%s&mb_id=%s&dir=up"><i class="fa fa-arrow-up" style="color: #647382;"></i></a>' % (comm_id, mb_id))
                            wr('<td><a href="Reorder?comm_id=%s&mb_id=%s&dir=down"><i class="fa fa-arrow-down" style="color: #647382;"></i></a>' % (comm_id, mb_id))
                            wr('<td><a href="Edit_Form?comm_id=%s&mb_id=%s&delete_member=1"><i class="fa fa-trash" style="color: #647382;"></i></a>' % (comm_id, mb_id))
                        wr('</table>')

        else:
            wr('You must be logged in as an administrator to view this page.')
