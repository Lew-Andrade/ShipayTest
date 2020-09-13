from flask import Flask
from flask import request, jsonify
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database/Shipay.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


class TransactionModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    establishment = db.Column(db.String())
    client = db.Column(db.String())
    value = db.Column(db.Integer())
    description = db.Column(db.String())

    def __repr__(self):
        return '<Transaction %s>' % self.establishment


class TransactionSchema(ma.Schema):
    class Meta:
        fields = ("id", "establishment", "client", "value", "description")


class TransactionsResource(Resource):
    @staticmethod
    def get():
        transactions = TransactionModel.query.all()
        return transactions_schema.dump(transactions)

    @staticmethod
    def post():
        new_transaction = TransactionModel(
            establishment=request.json['estabelecimento'],
            client=request.json['cliente'],
            value=request.json['valor'],
            description=request.json['descricao']
        )
        db.session.add(new_transaction)
        db.session.commit()
        return jsonify(aceito=True)


class TransactionResource(Resource):
    @staticmethod
    def get(transaction_id):
        transaction = TransactionModel.query.get_or_404(transaction_id)
        return transaction_schema.dump(transaction)

    @staticmethod
    def put(transaction_id):
        transaction = TransactionModel.query.get_or_404(transaction_id)
        if 'estabelecimento' in request.json:
            transaction.establishment = request.json['estabelecimento']
        if 'cliente' in request.json:
            transaction.client = request.json['cliente']
        if 'valor' in request.json:
            transaction.value = request.json['valor']
        if 'descricao' in request.json:
            transaction.description = request.json['descricao']

        db.session.commit()
        return transaction_schema.dump(transaction)

    @staticmethod
    def delete(transaction_id):
        transaction = TransactionModel.query.get_or_404(transaction_id)
        db.session.delete(transaction)
        db.session.commit()
        return jsonify(deletado=True)


api.add_resource(TransactionsResource, '/api/v1/transacao')
api.add_resource(TransactionResource, '/api/v1/transacao/<int:transaction_id>')

transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)

if __name__ == '__main__':
    app.run()
