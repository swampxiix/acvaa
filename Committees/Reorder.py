from Comm_Tmpl import Comm_Tmpl
from z_comm import get_committee_order, reorder_committees, \
    get_members_order, reorder_members

class Reorder (Comm_Tmpl):

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        comm_id = qs.get('comm_id')
        mb_id = qs.get('mb_id')
        direction = qs.get('dir')

        if mb_id:
            existing_order = get_members_order(comm_id)
            existing_index = existing_order.index(mb_id)

        else:
            existing_order = get_committee_order()
            existing_index = existing_order.index(comm_id)

        popped = existing_order.pop(existing_index)
        if direction == 'up':
            new_index = existing_index - 1
        else:
            new_index = existing_index + 1
        existing_order.insert(new_index, popped)

        if mb_id:
            reorder_members(comm_id, existing_order)
            self.response().sendRedirect('Edit_Form?comm_id=%s' % (comm_id))
        else:
            reorder_committees(existing_order)
            self.response().sendRedirect('Index')
