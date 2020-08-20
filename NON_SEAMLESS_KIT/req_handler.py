from ccavutil import encrypt, decrypt
from ccavResponseHandler import res
from string import Template

def data_enc(m_data,workingKey):
    encryption = encrypt(m_data,workingKey)
    return encryption
