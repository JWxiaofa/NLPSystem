import spacy
from spacy import displacy

# Load the language model
nlp = spacy.load('en_core_web_sm')

class DependencyParse:
    def __init__(self, text: str):
        self.text = text
        self.doc = nlp(text)

    def get_tree(self) -> list:
        structures = []
        for token in self.doc:
            structures.append((token.head.text, token.dep_, token.text))
        return structures

    def get_tree_with_br(self) -> str:
        res = ""
        for token in self.doc:
            res += f'{token.head.text:{12}} {token.dep_:{10}} {token.text}<br>'

        return res

    def get_doc(self):
        return self.doc

if __name__ == '__main__':
    sentence = "Sebastian Thrun started working on self-driving cars at Google in 2007."
    doc = DependencyParse(sentence)

    res = doc.get_tree()
    print(res)