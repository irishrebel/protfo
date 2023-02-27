from flask import Flask, render_template, redirect
from flask import request
import csv
app = Flask(__name__)


@app.route('/')
def my_home():  # put application's code here
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):  # put application's code here
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode ='a')as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')




def write_to_csv(data):
    with open('database.csv',newline='', mode ='a')as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'someting whent wrong try again'



if __name__ == '__main__':
    app.run()
#
# @app.route('/about.html')
# def about():  # put application's code here
#     return render_template('about.html')
#
#
# @app.route('/works.html')
# def works():  # put application's code here
#     return render_template('works.html')
#
#
# @app.route('/contact.html')
# def contact():  # put application's code here
#     return render_template('contact.html')
#
#
# @app.route('/thankyou.html')
# def thankyou():  # put application's code here
#     return render_template('thankyou.html')
#
#
# @app.route('/work.html')
# def work():  # put application's code here
#     return render_template('work.html')
