# -*- coding: utf-8 -*-
"""
this is the helper script that contains useful function to use for datascience
"""

def extract_zip_file(FileName):
    """
    exract data from ZIP file
    """    
    from zipfile import ZipFile
    zip_ref = ZipFile(FileName,"r")
    zip_ref.extractall()
    zip_ref.close()
    