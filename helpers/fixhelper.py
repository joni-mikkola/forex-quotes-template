

class FixHelper:
    def get_field_value(fobj, msg):
        if msg.isSetField(fobj.getField()):
            msg.getField(fobj)
            return fobj.getValue()
        else:
            return None

    def get_header_field_value(fobj, msg):
        if msg.getHeader().isSetField(fobj.getField()):
            msg.getHeader().getField(fobj)
            return fobj.getValue()
        else:
            return None
