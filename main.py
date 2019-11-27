import sys
import csv
from statistics import mean, median

def main():
    assert len(sys.argv) > 1, "No input file path specified."

    f = input_file = sys.argv[1]
    print(f"Processing input file: {input_file}")

    # TODO: Fill in the actual logic here!
    with open(input_file) as f:
        readcsv = csv.reader(f, delimiter = ',')

        for line in readcsv:
            lst4avg = []
            print(line)
            for item in line:
                lst4avg.append(float(item))
            print(f"The mean of this list is: {mean(lst4avg)}\n")


if __name__ == "__main__":
    main()
