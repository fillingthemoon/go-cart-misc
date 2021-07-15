import re
import os

def comma_delimited_handlers():
  for file_in_name in os.listdir('./handlers'):
    # Skip non-Python files
    if file_in_name[-3:] != '.py':
      continue

    file_in = './handlers/' + file_in_name
    file_out = './handlers_new/' + file_in_name

    # Count # of lines in CSV
    num_csv_lines = 0
    with open(file_in, 'r') as f_in:
      with open(file_out, 'w') as f_out:
        for line in f_in:
          if re.search("\d* {} [\w\s]*", line):
            num_csv_lines += 1

    # Parse and update lines in Python file
    with open(file_in, 'r') as f_in:
      with open(file_out, 'w') as f_out:

        csv_line = 1
        for line in f_in:

          # First line of CSV
          if re.search("\s*return \"\"\"\d* {} [\w\s'-]*", line):
            new_return_line = "        return \"\"\"cartogram_id,Region Data,Region Name,Inset\\n"
            
            first_row = re.search("(\d* {} [\w\s'-]*)", line).group(1)
            first_row_with_commas = first_row.replace(" {} ", ",{},")
            first_row_with_commas_n = first_row_with_commas.replace("\n", ",L\\n\n")

            f_out.write(new_return_line + "\n" + first_row_with_commas_n)

            csv_line += 1

          # Last line of CSV
          elif re.search("\d* {} [\w\s'-]*\"\"\"", line):
            last_line_with_commas = line.replace(" {} ", ",{},")
            last_line_with_commas_n = last_line_with_commas.replace("\"\"\"", ",R\\n\"\"\"")
            f_out.write(last_line_with_commas_n)
            
            csv_line += 1

          # The rest of the lines of the CSV
          elif re.search("\d* {} [\w\s'-]*", line):
            line_with_commas = line.replace(" {} ", ",{},")
            
            if csv_line < num_csv_lines / 2: 
              line_with_commas_n = line_with_commas.replace("\n", ",L\\n\n")
            else: 
              line_with_commas_n = line_with_commas.replace("\n", ",R\\n\n")
            f_out.write(line_with_commas_n)
            
            csv_line += 1

          # The rest of the lines of the Python file
          else:
            f_out.write(line)


comma_delimited_handlers()