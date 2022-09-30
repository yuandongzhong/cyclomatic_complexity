import ast
from .analyzer import Analyzer


def calculate(file_path):
    """
    Calculate the cyclomatic complexity of a Python file

    :param file_path: The file path of the file
    :return: Return the analyzer
    """
    with open(file_path, "r") as source:
        # Transform the source code to AST
        tree = ast.parse(source.read())
        
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            if isinstance(node, ast.ClassDef):
                child.parent = node
        
    analyzer = Analyzer()
    analyzer.visit(tree)
    analyzer.report()
    return analyzer


if __name__ == '__main__':
    calculate()
