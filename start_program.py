import argparse
import sys
from reqyml import reqyml


def createParser ():
    """Написать докстринг"""
    parser = argparse.ArgumentParser()
    parser.add_argument ('-f', '--file',default='config.yaml')
    parser.add_argument ('-s', '--script',default='all')
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    instance = reqyml(namespace.file)
    instance.script(namespace.script)
