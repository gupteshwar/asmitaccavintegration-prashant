#!/usr/bin/python

from flask import request, redirect, Flask, render_template
from ccavutil import encrypt, decrypt
from ccavResponseHandler import res
from string import Template
import json
app = Flask('ccavRequestHandler')

'''
Please put in the 32 bit alphanumeric key and Access Code in quotes provided by CCAvenues.
'''
accessCode = 'AVAM93HF11CI95MAIC'
workingKey = '607B428BC0C0853381C3A2AC287B1F40'


@app.route('/')
def webprint():
    return render_template('dataFrom.htm')


@app.route('/ccavResponseHandler', methods=['GET', 'POST'])
def ccavResponseHandler():
    plainText = res(request.form['encResp'])
    return plainText


@app.route('/ccavRequestHandler', methods=['GET', 'POST'])
def login():

    p_merchant_id = request.form['merchant_id']
    p_order_id = request.form['order_id']
    p_currency = request.form['currency']
    p_amount = request.form['amount']
    p_redirect_url = request.form['redirect_url']
    p_cancel_url = request.form['cancel_url']
    p_language = request.form['language']
    p_billing_name = request.form['billing_name']
    p_billing_address = request.form['billing_address']
    p_billing_city = request.form['billing_city']
    p_billing_state = request.form['billing_state']
    p_billing_zip = request.form['billing_zip']
    p_billing_country = request.form['billing_country']
    p_billing_tel = request.form['billing_tel']
    p_billing_email = request.form['billing_email']
    p_delivery_name = request.form['delivery_name']
    p_delivery_address = request.form['delivery_address']
    p_delivery_city = request.form['delivery_city']
    p_delivery_state = request.form['delivery_state']
    p_delivery_zip = request.form['delivery_zip']
    p_delivery_country = request.form['delivery_country']
    p_delivery_tel = request.form['delivery_tel']
    p_merchant_param1 = request.form['merchant_param1']
    p_merchant_param2 = request.form['merchant_param2']
    p_merchant_param3 = request.form['merchant_param3']
    p_merchant_param4 = request.form['merchant_param4']
    p_merchant_param5 = request.form['merchant_param5']
    p_promo_code = request.form['promo_code']
    p_customer_identifier = request.form['customer_identifier']


    merchant_data='merchant_id='+p_merchant_id+'&'+'order_id='+p_order_id + '&' + "currency=" + p_currency + '&' + 'amount=' + p_amount+'&'+'redirect_url='+p_redirect_url+'&'+'cancel_url='+p_cancel_url+'&'+'language='+p_language+'&'+'billing_name='+p_billing_name+'&'+'billing_address='+p_billing_address+'&'+'billing_city='+p_billing_city+'&'+'billing_state='+p_billing_state+'&'+'billing_zip='+p_billing_zip+'&'+'billing_country='+p_billing_country+'&'+'billing_tel='+p_billing_tel+'&'+'billing_email='+p_billing_email+'&'+'delivery_name='+p_delivery_name+'&'+'delivery_address='+p_delivery_address+'&'+'delivery_city='+p_delivery_city+'&'+'delivery_state='+p_delivery_state+'&'+'delivery_zip='+p_delivery_zip+'&'+'delivery_country='+p_delivery_country+'&'+'delivery_tel='+p_delivery_tel+'&'+'merchant_param1='+p_merchant_param1+'&'+'merchant_param2='+p_merchant_param2+'&'+'merchant_param3='+p_merchant_param3+'&'+'merchant_param4='+p_merchant_param4+'&'+'merchant_param5='+p_merchant_param5+'&'+'promo_code='+p_promo_code+'&'+'customer_identifier='+p_customer_identifier+'&'

    encryption = encrypt(merchant_data,workingKey)

    html = '''\
<form id="nonseamless" method="post" name="redirect" action="https://secure.ccavenue.com/transaction/transaction.do?command=initiateTransaction"/>
<input type="hidden" id="encRequest" name="encRequest" value="$encReq">
<input type="hidden" name="access_code" id="access_code" value="$xscode">
<script language="javascript">document.redirect.submit();</script>
</form>'
'''

    fin = Template(html).safe_substitute(encReq=encryption,xscode=accessCode)
    return fin


def data_enc(m_data,workingKey):
    encryption = encrypt(merchant_data,workingKey)
    return encryption


@app.route("/get_req_key", methods=["POST"])
def encrypt_key():
    if request.method=='POST':
        api_data = request.form['data']
        req_api_data = json.loads(api_data)
        
        workingKey = '607B428BC0C0853381C3A2AC287B1F40'
        p_merchant_id = "263039"
        p_currency = "INR"
        p_cancel_url ="https://uatasmita.indictranstech.com/api/method/asmita_bazaar.asmita_bazaar.api.api.res"
        p_redirect_url = "https://uatasmita.indictranstech.com/api/method/asmita_bazaar.asmita_bazaar.api.api.res"
        p_order_id = str(req_api_data.get('order_id'))
        p_amount = str(req_api_data.get('amount'))
        p_language = str(req_api_data.get('language'))

        merchant_data='merchant_id='+p_merchant_id+'&'+'order_id='+p_order_id + '&' + "currency=" + p_currency + '&' + 'amount=' + p_amount+'&'+'redirect_url='+p_redirect_url+'&'+'cancel_url='+p_cancel_url+'&'+'language='+p_language

        encryption = encrypt(merchant_data,workingKey)


        return {'encryption':encryption}

@app.route('/example/')
def example():
    return {'hello': 'world'}


@app.route("/get_AsmitaReqKey", methods=["POST"])
def encrypt_key_for_asmita():
    if request.method=='POST':
        workingKey = '607B428BC0C0853381C3A2AC287B1F40'
        p_merchant_id = "263039"
        p_currency = "INR"
        p_cancel_url ="https://asmitabazaar.indictranstech.com/api/method/asmita_bazaar.asmita_bazaar.api.api.res"
        p_redirect_url = "https://asmitabazaar.indictranstech.com/api/method/asmita_bazaar.asmita_bazaar.api.api.res"
        p_order_id = str(request.form.get('order_id'))
        p_amount = str(request.form.get('amount'))
        p_language = str(request.form.get('language'))
        merchant_data='merchant_id='+p_merchant_id+'&'+'order_id='+p_order_id + '&' + "currency=" + p_currency + '&' + 'amount=' + p_amount+'&'+'redirect_url='+p_redirect_url+'&'+'cancel_url='+p_cancel_url+'&'+'language='+p_language
        encryption = encrypt(merchant_data,workingKey)
        
        return encryption


@app.route("/get_uat_AsmitaReqKey", methods=["POST"])
def uat_encrypt_key_for_asmita():
    if request.method=='POST':
        workingKey = '607B428BC0C0853381C3A2AC287B1F40'
        p_merchant_id = "263039"
        p_currency = "INR"
        p_cancel_url ="https://uatasmita.indictranstech.com/api/method/asmita_bazaar.asmita_bazaar.api.api.res"
        p_redirect_url = "https://uatasmita.indictranstech.com/api/method/asmita_bazaar.asmita_bazaar.api.api.res"
        p_order_id = str(request.form.get('order_id'))
        p_amount = str(request.form.get('amount'))
        p_language = str(request.form.get('language'))
        merchant_data='merchant_id='+p_merchant_id+'&'+'order_id='+p_order_id + '&' + "currency=" + p_currency + '&' + 'amount=' + p_amount+'&'+'redirect_url='+p_redirect_url+'&'+'cancel_url='+p_cancel_url+'&'+'language='+p_language
        encryption = encrypt(merchant_data,workingKey)
        
        return encryption


@app.route("/get_string_encryption", methods=["POST"])
def string_encryption():
    if request.method=='POST':
    	ref_no = str(request.form.get('reference_no'))
        workingKey = '607B428BC0C0853381C3A2AC287B1F40'
        merchant_data="|"+ref_no+"|"
        encryption = encrypt(merchant_data,workingKey)
        return encryption

@app.route("/get_json_ecryption", methods=["POST"])
def json_string_encryption():
    if request.method=='POST':
        workingKey = '607B428BC0C0853381C3A2AC287B1F40'
        req_json= request.form.to_dict()
        app_json = json.dumps(req_json)
        json_encryption = encrypt(app_json,workingKey)
        return json_encryption
       


# Host Server and Port Number should be configured here.

if __name__ == '__main__':
    app.run(host = '212.83.155.158', port = 5000, debug=True)
