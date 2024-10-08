from app import pdb

class Customer(pdb.Model):
    __tablename__ = "Customer"

    id = pdb.Column(pdb.Integer, primary_key=True)
    firstName = pdb.Column(pdb.String, nullable=False)
    lastName = pdb.Column(pdb.String, nullable=False)
    mail = pdb.Column(pdb.String, nullable=False)
    phoneNumber = pdb.Column(pdb.String, nullable=False)
    address = pdb.Column(pdb.Text, nullable=False)
