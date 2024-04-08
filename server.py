from flask import Flask, render_template;
from flask import request;
from flask import redirect;
import csv;

app = Flask(__name__)

print(__name__)

@app.route("/")
def my_Home():
    return render_template('./index.html')

# @app.route("/works.html")
# def my_Works():
#     return render_template('./works.html')

# @app.route("/about.html")
# def about_me():
#     return render_template('./about.html')

# @app.route("/contact.html")
# def contact_Me():
#     return render_template('./contact.html')

# @app.route("/components.html")
# def components():
#     return render_template('./components.html')

#Lets make it Dynamic

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


#Accesing Request Data ---> Means Whatever user writes in Form -->> need to access that data

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if(request.method == 'POST'):
        data = request.form.to_dict()
        # print("HMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM",data)
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong'