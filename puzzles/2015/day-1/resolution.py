import sys

def main(input: str):
  number_of_opened_parentheses = input.count("(")
  number_of_closed_parentheses = -input.count(")")

  return number_of_opened_parentheses + number_of_closed_parentheses

if __name__ == "__main__":
    print(main(sys.argv[1]))
