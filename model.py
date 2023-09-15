"""
created by: Toby Cantello
Date created: 9/13/23
Last updated: 9/13/23
""" 

from config import db, ma

class Snippet(db.Model):
    __tablename__ = "snippet"
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(25))
    code = db.Column(db.String(500))

class SnippetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Snippet
        load_instance = True
        sqla_session = db.session

snippet_schema = SnippetSchema()
snippets_schema = SnippetSchema(many=True)