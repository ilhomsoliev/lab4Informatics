import os
import json
import csv

if __name__ == "__main__":
    '''input_file = os.path.join(os.path.dirname(__file__), "../data/in.json")
    output_file = os.path.join(os.path.dirname(__file__), "../data/out-dop4")

    data = json.loads(open(input_file, "r").read())
    result = convert(data)

    open(output_file, "wb").write(result.SerializeToString())
    print("dop4.main complete!")'''
    # Open the JSON file
    with open('../data/in.json', 'r') as json_file:
        data = json.load(json_file)

    # Open a CSV file for writing
    with open('../data/out-dop4.csv', 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write the header (keys of the JSON object)
        header = data.keys()
        csv_writer.writerow(header)

        # Write the data row
        csv_writer.writerow(data.values())

    print("CSV file has been created.")

