import numpy as np
import csv

def ConvertCsvFileToNumPyTable(csv_name, data_type="int", num_columns=2):
  """
  Converts a CSV file with ints or floats to a NumPy table.

  Default settings:
  - the first line is skipped.
  """
  table = np.zeros([0, num_columns])

  with open(csv_name, newline='') as csvfile:
    values = csv.reader(csvfile)
    first_line = True

    # Iterative loop over each line in the CSV file.
    for row in values:

      if first_line == True:
        first_line = False
        continue

      nums = []

      if data_type == "int":
        
        # Iterative loop over each comma-separated element on an individual line in the CSV file.
        for i in row:
          nums.append(int(i))

        table = np.vstack([table,nums])

      else:
        # Iterative loop over each comma-separated element on an individual line in the CSV file.
        for i in row:
          nums.append(float(i))

        table = np.vstack([table,nums])

  return table

