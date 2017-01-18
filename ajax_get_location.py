from WebKit.HTTPContent import HTTPContent
import json
from z_account import get_user_acct

class ajax_get_location (HTTPContent):

    def defaultAction(self):
        wr = self.writeln
        qs = self.request().fields()
        username = qs.get("username")
        d = get_user_acct(username)
        r = self.response()
        r.setHeader('Content-type', 'text/plain')
        self.write(json.dumps(d))

