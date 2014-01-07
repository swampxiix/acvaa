def text (name, value='', clss='', size='', max='', id=''):
    txt = '<input type="text" name="%s" value="%s"' % (name, value)
    if size:
        txt += ' size="%s"' % (size)
    if clss:
        txt += ' class="%s"' % (clss)
    if max:
        txt += ' maxlength="%s"' % (max)
    if id:
        txt += ' id="%s"' % (id)
    txt += '>'
    return txt

def passwd (name, value='', clss='', size=''):
    txt = '<input type="password" name="%s" value="%s"' % (name, value)
    if clss:
        txt += ' class="%s"' % (clss)
    if size:
        txt += ' size="%s"' % (size)
    txt += '>'
    return txt

def hidden (name, value=''):
    return '<input type="hidden" name="%s" value="%s">' % (name, value)

def select (name='', opts=[], selected='', clss=None):
    txt = '<select name="%s"' % (name)
    if clss:
        txt += ' class="%s"' % (clss)
    txt += '>'
    for opt in opts:
        txt += '<option value="%s"' % (opt)
        if opt == selected:
            txt+=' selected'
        txt += '>%s</option>' % (opt)
    txt += '</select>'
    return txt

def submit (text):
    return '<input type="submit" value="%s">' % (text)

def radio (name, value='', checked=False):
    txt = '<input type="radio" name="%s" value="%s"' % (name, value)
    if checked:
        txt += ' CHECKED'
    txt += '>'
    return txt

def radio_jq (name, value='', clss='', id='', checked=False):
    txt = '<input type="radio" name="%s" value="%s"' % (name, value)
    if clss:
        txt += ' class="%s"' % (clss)
    if id:
        txt += ' id="%s"' % (id)
    if checked:
        txt += ' CHECKED'
    txt += '>'
    return txt

def checkbox (name='', value='', checked=False):
    txt = '<input type="checkbox" name="%s" value="%s"' % (name, value)
    if checked:
        txt += ' CHECKED'
    txt += '>'
    return txt
