import sys
import os
from input_parser import InputParser


class IOParser:
    def __init__(self):
        pass

    def try_load(self, name):
        if not os.path.exists(name):
            return None
        with open(name) as f:
            try:
                return [line.strip() for line in f]
            finally:
                f.close()

    def load_input(self, name) -> InputParser:
        lines = self.try_load(name)
        if (lines is None):
            return None
        else:
            return InputParser(lines)

    def write_output(self, name, data):
        with open(name, 'w') as fs:
            for line in data:
                fs.write('%s\n' % line)


if __name__ == '__main__':
    places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

    p = IOParser()
    #p.write_output("test.txt", places)
    input_data = p.load_input('input/1.txt')
    print("Test parser")
