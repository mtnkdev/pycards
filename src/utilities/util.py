import sys

if sys.version_info[0] < 3:
    import __builtin__
else:
    import builtins as __builtin__
import gettext


def localize():

    def ugettext(message):
        # unicoded gettext
        if sys.version_info[0] < 3:
            if not isinstance(message, unicode):
                message = unicode(message, 'utf-8')
        else:
            if not isinstance(message, str):
                message = str(message, 'utf-8')
        domain = gettext._current_domain
        try:
            t = gettext.translation(domain,
                                    gettext._localedirs.get(domain, None))
        except IOError:
            return message
        return t.ugettext(message)

    def ungettext(msgid1, msgid2, n):
        # unicoded ngettext        
        if sys.version_info[0] < 3:
            if not isinstance(msgid1, unicode):
                msgid1 = unicode(msgid1, 'utf-8')
            if not isinstance(msgid2, unicode):
                msgid2 = unicode(msgid2, 'utf-8')
        else:
            if not isinstance(msgid1, str):
                msgid1 = str(msgid1, 'utf-8')
            if not isinstance(msgid2, str):
                msgid2 = str(msgid2, 'utf-8')
        domain = gettext._current_domain
            
        try:
            t = gettext.translation(domain,
                                    gettext._localedirs.get(domain, None))
        except IOError:
            if n == 1:
                return msgid1
            else:
                return msgid2
        return t.ungettext(msgid1, msgid2, n)

    gettext.ugettext = ugettext
    gettext.ungettext = ungettext

    __builtin__._ = gettext.ugettext  # use unicode
    __builtin__.n_ = lambda x: x
