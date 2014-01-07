from WebKit.Page import Page

class Template_Dummy(Page):
    def writeDocType(self):
        self.writeln('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"'
            '"http://www.w3.org/TR/html4/strict.dtd">')

    def writeStyleSheet(self):
        self.writeln('<link rel="shortcut icon" href="/g/favicon.ico" type="image/x-icon" />')
        self.writeln('<link rel="stylesheet" href="/c/acvasplash.css" type="text/css">')

    def writeBodyParts(self):
        self.writeHeader()
        self.writeMenu()
        self.writeContent()
        self.writeNav()
        self.writeFooter()

    def writeContent(self):
        pass

    def writeNav(self):
        pass

    def writeHeader(self):
        pass

    def writeMenu(self):
        pass

    def writeFooter(self):
        pass
