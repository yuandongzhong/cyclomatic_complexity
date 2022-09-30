import sys

import ast
from tabulate import tabulate

class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.cyclomatic_complexity = 0
        self.total = 0
        self.function_dict = {}

    def visit_If(self, node):
        """ Analyse an 'if' or 'elif' statement """
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_IfExp(self, node):
        self.cyclomatic_complexity += 1
        self.generic_visit(node)    

    def visit_For(self, node):
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_Try(self, node):
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_TryExcept(self, node):
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_With(self, node):
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_Assert(self, node):
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_comprehension(self, node):
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_And(self, node):
        """ Analyse boolean operator 'and' """
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_Or(self, node):
        """ Analyse boolean operator 'or' """
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        analyzer = Analyzer()
        for child in node.body:
            analyzer.visit(child)
        function_name = f"{node.parent.name}.{node.name}" if hasattr(node, "parent") else node.name
        # cyclomatic complexity = numbers of decisions + 1
        self.function_dict[function_name] = analyzer.cyclomatic_complexity + 1

    def report(self):
        metrics_dict = {**self.function_dict, **{sys.argv[0]: self.cyclomatic_complexity}}
        self.total = sum(metrics_dict.values())
        sorted_metrics = sorted(metrics_dict.items(), key=lambda item: item[1], reverse=True)
        
        print(f"Total: {self.total}")
        print(tabulate(sorted_metrics))


def calculate():
    with open("birds.py", "r") as source:
        # Transform the source code to AST
        tree = ast.parse(source.read())
        
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            if isinstance(node, ast.ClassDef):
                child.parent = node
        
    analyzer = Analyzer()
    analyzer.visit(tree)
    analyzer.report()


if __name__ == '__main__':
    calculate()
