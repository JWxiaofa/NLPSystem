from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import ner
import dependency_parse
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)


class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    count = db.Column(db.Integer, default=1)
    # Create a relationship to the Head model, which will contain head words
    heads = db.relationship('Relationship', backref='entity', lazy='dynamic')

class Relationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    head = db.Column(db.String(255), nullable=False)
    count = db.Column(db.Integer, default=1)
    relation = db.Column(db.String(50), nullable=False)
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html', input=open('input.txt').read())
    else:
        text = request.form['text']
        doc = ner.SpacyDocument(text)
        markup = doc.get_entities_with_markup()
        markup_paragraphed = ''
        for line in markup.split('\n'):
            if line.strip() == '':
                markup_paragraphed += '<p/>\n'
            else:
                markup_paragraphed += line

        doc2 = dependency_parse.DependencyParse(text)
        tree = doc2.get_tree_with_br()

        entites_info = doc.get_entities()
        dependencies = doc2.get_tree()

        for start, end, label, entity_text in entites_info:
            entity = Entity.query.filter_by(text=entity_text).first()
            if entity:
                entity.count += 1
            else:
                entity = Entity(text=entity_text, count=1)
                db.session.add(entity)

            for head_text, dep, word_text in dependencies:
                if word_text in entity_text.split():
                    relationship = Relationship.query.filter_by(entity_id=entity.id, text=word_text, head=head_text,
                                                                relation=dep).first()
                    if relationship:
                        relationship.count += 1
                    else:
                        relationship = Relationship(text=word_text, relation=dep, entity_id=entity.id, count=1, head=head_text)
                        db.session.add(relationship)
        db.session.commit()

        return render_template('result.html', markup=markup_paragraphed, tree=tree)

@app.route('/database', methods=['GET'])
def database():
    # Query all entities
    entities = Entity.query.all()
    # Create a dictionary to hold entities and their relationships
    entities_with_heads = {}

    for entity in entities:
        # Query the heads related to this entity
        heads = Relationship.query.filter_by(entity_id=entity.id).all()
        # Create a dictionary of heads and counts
        heads_with_counts = {head.text: (head.head, head.relation, head.count) for head in heads}
        # Sort the heads by count, descending
        sorted_heads = sorted(heads_with_counts.items(), key=lambda x: x[1][2], reverse=True)
        # Add to the dictionary
        entities_with_heads[entity.text] = {
            'count': entity.count,
            'heads': sorted_heads
        }

    # Pass the dictionary to the template
    return render_template('database.html', entities_with_heads=entities_with_heads)

if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5001)
