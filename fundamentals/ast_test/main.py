import ast
from pprint import pprint


def main():
    with open("../01_simple_calculator/main.py", "r") as source:
        tree = ast.parse(source.read())

    summary = {}
    for node in ast.walk(tree):
        node_name = type(node).__name__
        if node_name in summary:
            summary[node_name] = summary[node_name] + 1
        else:
            summary[node_name] = 1
    pprint(summary)


if __name__ == "__main__":
    main()
