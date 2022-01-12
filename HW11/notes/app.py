from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import queries

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ContactBook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/addcontact', methods=['POST', 'GET'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        contacnt_add = queries.contacnt_add(name, phone_number, email)
        try:
            db.session.add(contacnt_add)
            db.session.commit()
            return redirect('/')
        except:
            return 'Add contact error'
    else:
        return render_template("addcontact.html")


@app.route('/')
@app.route('/showall')
def showall():
    contacts = queries.showall()
    return render_template("showall.html", contacts=contacts)


@app.route('/showall/<int:id>/delete')
def delete_contact(id):
    delete = queries.delete_contact(id)
    try:
        db.session.delete(delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Delete contact error'


@app.route('/showall/<int:id>/edit', methods=['POST', 'GET'])
def edit_contact(id):
    contact = queries.edit_contact(id)
    if request.method == 'POST':
        contact.name = request.form['name']
        contact.phone_number = request.form['phone_number']
        contact.email = request.form['email']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Edit contact error'
    else:
        return render_template("editcontact.html", contact=contact)


if __name__ == "__main__":
    app.run(debug=True)
