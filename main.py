"""
A program that runs the hmc5883l compass.
"""
from compass.compassls import get_bearing


def main():
    get_bearing()


if __name__ == "__main__":
    main()
