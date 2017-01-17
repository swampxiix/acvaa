from WebKit.HTTPContent import HTTPContent
import json
from z_geo import DEFAULT, USA_STATES, USA_STATES_ORDER, CAN_STATES, CAN_STATES_ORDER, MEX_STATES, MEX_STATES_ORDER

class ajax_get_states (HTTPContent):

    def defaultAction(self):
        wr = self.writeln
        qs = self.request().fields()
        country = qs.get("country")
        d = {'dict': None, 'order': None}
        if country == DEFAULT:
            d['dict'] = USA_STATES
            d['order'] = USA_STATES_ORDER
        if country == 'Canada':
            d['dict'] = CAN_STATES
            d['order'] = CAN_STATES_ORDER
        if country == 'Mexico':
            d['dict'] = MEX_STATES
            d['order'] = MEX_STATES_ORDER
        r = self.response()
        r.setHeader('Content-type', 'text/plain')
        self.write(json.dumps(d))

