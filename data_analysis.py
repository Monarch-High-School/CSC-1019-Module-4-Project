"""

Name - Month Year
"""

import csv

def get_records(data_filename: str) -> list[dict]:
  """
  Gets records from a csv data file.
  Parameters:
    data_filename(str): The location and name of the csv file that contains the data
  Return:
    list[record]: a list of dictionaries, each dictionary is a record
  """
  # TODO: explain what I am
  records: list[dict] = []

  # TODO: explain what these 3 lines do
  with open(data_filename, "r", encoding='utf-8-sig') as data_file:
    reader: csv.DictReader = csv.DictReader(data_file)
    for record in reader:
      # TODO: convert any fields to appropriate type
      
      # add record to list
      records.append(record)
  return records


def calculate_avg_value(records: list[dict]) -> float:
  """
  TODO: you will need to change this for your program
  Calculates the average value of a stolen bike
  Parameters:
    records(list[dict]): A list of dictionaries where one of the keys is "PropValue"
  Return:
    float: the average value of a stolen bike
  """
  pass # TODO: remove this line and write the function


def main() -> None:
  # input
  # TODO: upload your data file and set the name in data_filename
  data_filename: str = ""
  records: list[dict] = get_records(data_filename)

  # processing
  # TODO: write functions to analyze data and call them
  avg_value: float = calculate_avg_value(records)

  # output
  # TODO: output the results of your analysis
  print(f"Read in {len(records)} records.")
  print(f"The average value of a stolen bike is: ${avg_value:.2f}")

if __name__ == "__main__":
  main()
