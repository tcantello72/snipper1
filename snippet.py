"""
created by: Toby Cantello
Date created: 9/13/23
Last updated: 9/13/23
""" 


from flask import abort, make_response
from config import db
from model import Snippet, snippet_schema, snippets_schema


def read_all():
    snippets = Snippet.query.all()
    print(snippets)
    return snippets_schema.dump(snippets)

def create(snippet):
    id = snippet.get("id")
    existing_snippet = Snippet.query.filter(Snippet.id == id).one_or_none()

    if existing_snippet is None:
        new_snippet = snippet_schema.load(snippet, session=db.session)
        db.session.add(new_snippet)
        db.session.commit()
        return snippet_schema.dump(new_snippet), 201
    else:
        abort(
            406,
            f"There is already a snippet with id {id} in the database",
        )

def read_one(id):
    snippet = Snippet.query.filter(Snippet.id == id).one_or_none()

    if snippet is not None:
        return snippet_schema.dump(snippet)
    else:
        abort(
            404, f"A snippet with the id of {id} was not found"
        )

def update(id, snippet):
    existing_snippet = Snippet.query.filter(Snippet.id == id).one_or_none()

    if existing_snippet:
        update_snippet = snippet_schema.load(snippet, session=db.session)
        existing_snippet.id = update_snippet.id
        db.session.merge(existing_snippet)
        db.session.commit()
        return snippet_schema.dump(existing_snippet), 201
    else:
        abort(
            404,
            f"A snippet with the id of {id} was not found"
        )

def delete(id):
    existing_snippet = Snippet.query.filter(Snippet.id == id).one_or_none()

    if existing_snippet:
        db.session.delete(existing_snippet)
        db.session.commit()
        return make_response(f"Id {id} successfully deleted", 200)
    else:
        abort(
            404,
            f"A snippet with the id of {id} was not found"
        )