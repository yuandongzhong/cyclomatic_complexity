import ast
import sys
from tabulate import tabulate


class Analyzer(ast.NodeVisitor):
    """
    A node visitor class that walks the abstract syntax tree 
    and calls a visitor function for every node found. 
    """
    def __init__(self):
        self.cyclomatic_complexity = 0
        self.total = 0
        self.function_dict = {}

    def visit_If(self, node):
        """ Analyse an 'if' or 'elif' statement """
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_IfExp(self, node):
        """ An expression such as a if b else c. """
        self.cyclomatic_complexity += 1
        self.generic_visit(node)    

    def visit_For(self, node):
        """ A for loop statement """
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        """ A while loop statement """
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_Try(self, node):
        """ try blocks """
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_TryExcept(self, node):
        """ except blocks """
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_With(self, node):
        """ A with block """
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_Assert(self, node):
        """ An assertion statement """
        self.cyclomatic_complexity += 1
        self.generic_visit(node)

    def visit_comprehension(self, node):
        """ Analyse comprehension """

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
        """ A function definition. """
        analyzer = Analyzer()
        for child in node.body:
            analyzer.visit(child)
        function_name = f"{node.parent.name}.{node.name}" if hasattr(node, "parent") else node.name
        # cyclomatic complexity = numbers of decisions + 1
        self.function_dict[function_name] = analyzer.cyclomatic_complexity + 1

    def report(self):
        """
        Print the metrics
        """
        if self.cyclomatic_complexity > 0:
            metrics_dict = {**self.function_dict, **{sys.argv[0]: self.cyclomatic_complexity}}
        else:
            metrics_dict = self.function_dict

        self.total = sum(metrics_dict.values())
        sorted_metrics = sorted(metrics_dict.items(), key=lambda item: item[1], reverse=True)
        print(f"Total: {self.total}")
        print(tabulate(sorted_metrics))