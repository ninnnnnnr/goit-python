from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ContactBook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ContactBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    phone_number = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<ContactBook %r>' % self.id


@app.route('/addcontact', methods=['POST', 'GET'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        contacnt_add = ContactBook(name=name, phone_number=phone_number, email=email)
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
    contacts = ContactBook.query.order_by(ContactBook.date.desc()).all()
    return render_template("showall.html", contacts=contacts)


@app.route('/showall/<int:id>/delete')
def delete_contact(id):
    delete = ContactBook.query.get(id)
    try:
        db.session.delete(delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Delete contact error'


@app.route('/showall/<int:id>/edit', methods=['POST', 'GET'])
def edit_contact(id):
    contact = ContactBook.query.get(id)
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








