# -*- coding: utf-8 -*-

from pyload.plugins.internal.DeadCrypter import DeadCrypter


class MultiuploadCom(DeadCrypter):
    __name__ = "MultiuploadCom"
    __type__ = "crypter"
    __version__ = "0.02"

    __pattern__ = r'http://(?:www\.)?multiupload\.(com|nl)/\w+'

    __description__ = """MultiUpload.com decrypter plugin"""
    __authors__ = [("zoidberg", "zoidberg@mujmail.cz")]