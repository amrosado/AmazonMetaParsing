import re

meta_file = open('amazon-meta.txt', 'rb')

# decode the file with utf-8 if you can't open it as an ascii file
meta_file_read = meta_file.read().decode('utf-8')

# look at the file representation in utf.  You can see in this decode that it has what are called carriage
# returns for new lines '\n\r' instead of just '\n'

meta_file_line_split = meta_file_read.split('\n')

#regular expression to determine data type
data_id_type = re.compile('\w+\s?\w*(?=[:])')

# get any numbers from line using this regular expression
data_id_number = re.compile('(\d+)')

data_id_string = re.compile('(?<=[:]\s).+')

result_dicts = []

result_dict = {}
# loop from the line split with some logic

# you can use some simple splits or finds to tell you information about the data
for line in meta_file_line_split:
    identify_comment = line.find('#')
    identify_id = line.find(':')
    if identify_comment >= 0:
        pass
        # skip this line


    if identify_id >= 0:
        #use find all to find regex matches
        result_type = data_id_type.findall(line)
        result_value_number = data_id_number.findall(line)
        result_value_string = data_id_string.findall(line)

        # total items not ueeful unless validation is needed
        if result_type[0] == 'Total items':
            pass

        # do something with specific results
        if result_type[0] == 'Id':
            if len(result_dict) > 0:
                result_dicts.append(result_dict)
                result_dict = {'Id': int(result_value_number[0])}
            else:
                result_dict['Id'] = int(result_value_number[0])
        else:
            if len(result_value_number) > 0:
                result_dict[result_type[0]] = [int(x) for x in result_value_number]
            else:
                result_dict[result_type[0]] = result_value_string[0].strip()

pass

