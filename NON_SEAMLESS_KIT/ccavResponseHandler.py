#!/usr/bin/python

from ccavutil import encrypt,decrypt
from string import Template

def res(encResp):
	'''
	Please put in the 32 bit alphanumeric key in quotes provided by CCAvenues.
	'''
	workingKey = '607B428BC0C0853381C3A2AC287B1F40'
	decResp = decrypt(encResp,workingKey).decode("utf-8")
	data = '<table border=1 cellspacing=2 cellpadding=2><tr><td>'
	data = data + decResp.replace('=','</td><td>')
	data = data.replace('&','</td></tr><tr><td>')
	data = data + '</td></tr></table>'

	html = '''\
	<html>
		<head>
			<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
			<title>Response Handler</title>
		</head>
		<body>
			<center>
				<font size="4" color="blue"><b>Response Page</b></font>
				<br>
				$response
			</center>
			<br>

		</body>
	</html>
	'''


	fin = Template(html).safe_substitute(response=data)
	return fin


def data_enc(m_data,workingKey):
    encryption = encrypt(m_data,workingKey)
    return encryption

