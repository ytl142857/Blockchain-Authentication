
from client.common import transaction_common
from flask import Flask, request, render_template

app = Flask(__name__)

tx_client = transaction_common.TransactionCommon("0x2d1c577e41809453c50e7e5c3f57d06f3cdd90ce", "contracts", "HelloWorld")

@app.route('/index/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        new_str = request.form['new_str']
        tx_client.send_transaction_getReceipt("set", (new_str,))
    get_str = tx_client.call_and_decode("get")
    return render_template("index.html", get_str=get_str)


if __name__ == '__main__':
    app.debug = True
    app.run()