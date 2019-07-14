from rasa_nlu.model import Metadata, Interpreter

def run_nlu():
    interpreter = Interpreter.load('./models/current/nlu')
    print(interpreter.parse(u""))


if __name__ == '__main__':
    run_nlu()
