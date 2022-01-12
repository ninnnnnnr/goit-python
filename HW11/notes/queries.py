from models import ContactBook


def contacnt_add(name, phone_number, email):
    return ContactBook(name=name, phone_number=phone_number, email=email)


def showall():
    return ContactBook.query.order_by(ContactBook.date.desc()).all()


def delete_contact(id):
    delete = ContactBook.query.get(id)
    return delete


def edit_contact(id):
    contact = ContactBook.query.get(id)
    return contact
