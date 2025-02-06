"""

Team Member Names - Month Year
"""

"""
PRIMM: Python Data Processing
In this PRIMM Activity, you'll learn how to process a 
CSV file and complete some basic extraction techniques.

name - date
"""

import csv
from typing import Union

# set up a type hint for the record type
record = dict[str, Union[str, int, float]]

def get_records(data_filename: str) -> list[record]:
  """
  Gets records from a csv data file.
  Parameters:
    data_filename(str): The location and name of the csv file that contains the data
  Returns:
    list[record]: a list of records where each 
        record is a dictionary where the keys are strings 
        and the values can be int or str
  """
  records: list[record] = []
  with open(data_filename, "r", encoding='utf-8-sig') as data_file:
    reader: csv.DictReader = csv.DictReader(data_file)
    for record in reader:      
      records.append(record)

  return records

def convert_fields(records: list[record]) -> None:
    """
    Converts fields to the appriopriate data type
    Parameters:
        records(list[record]): A list of records
    """
    for record in records:
            # todo, you will need to modify this code
        record[""] = int(record[""])



def main() -> None:
  data_filename: str = "resources/stolen_bikes.csv"
  records: list[record] = get_records(data_filename)

  convert_fields(records)


if __name__ == "__main__":
  main()
