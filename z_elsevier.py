import time, base64, pyDes, urllib

# These constants are provided by Elsevier.
TPSHOSTNAME = 'www.acvaa.org'
TPSSOCIETYID = '315'
TPSMEMBERLEVEL = 'memberaccess'
TPSENCRYPTKEY = 'c2bfcd4d5488947ec2bfcd4d5488947e'

def get_token ():
    key_decoded = base64.b64decode( TPSENCRYPTKEY )
    enc_obj = pyDes.triple_des( key=key_decoded,
                                mode=pyDes.ECB, 
                                padmode=pyDes.PAD_PKCS5 )
    ms_since_epoch = str( int( time.time() ) * 1000 ) # ms, not just time.time() in s
    plaintext_token = '%s|%s|%s' % ( TPSHOSTNAME, ms_since_epoch, TPSMEMBERLEVEL )
    encrypted_obj = enc_obj.encrypt( plaintext_token )
    encoded_obj = base64.b64encode( bytes( encrypted_obj ) )
    urlencoded_obj = urllib.quote_plus( encoded_obj )
    return urlencoded_obj

def get_query_string ():
    return 'TPSTOKEN=%s.%s' % ( TPSSOCIETYID, get_token() )



