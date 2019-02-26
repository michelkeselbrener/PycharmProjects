import csv

#with open("Klarf.csv", newline='') as csvfile:
with open("F:\\images\\Michel-Syntetic-DM-Circularity\\2019-02-25-0844\\Michel-Syntetic-DM-2019-02-25-0844\\Results\\Michel-Syntetic-DM-2019-02-25-0844_02_25_19_09_27_15_435.csv", newline='') as csvfile:
#with open("try.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    ss1 = 'Legends,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
    s2 = '1'

    number_of_line = 0
    #number_of_label = 0
    start_label_legend_table_line_number = 0
    end_label_legend_table_line_number = 0
    start_defects_table_line_number = 0
    end_defects_table_line_number = 0


    for row in csvfile:
        number_of_line = number_of_line + 1
        if row[0] == ',' and row[1] == 'L' and row[2] == 'a' and row[3] == 'b':
            print(row)
            start_label_legend_table_line_number = number_of_line + 1

        if row[0] == ',' and row[1] == 'E' and row[2] == 'n' and row[3] == 'd' and row[4] == ' ' and row[5] == 'L' and row[6] == 'a' and row[7] == 'b':
            print(row)
            end_label_legend_table_line_number = number_of_line - 1
        '''
        if row[0] == ',' and row[1] == 'G' and row[2] == 'r' and row[3] == 'o':
            print(row)
            

        if row[0] == ',' and row[1] == 'E' and row[2] == 'n' and row[3] == 'd' and row[4] == ' ' and row[5] == 'G' and \
                row[6] == 'r' and row[7] == 'o':
            print(row)
            
        '''
        if row[0] == 'D' and row[1] == 'E' and row[2] == 'F' and row[3] == 'E':
            print(row)
            start_defects_table_line_number = number_of_line

    end_defects_table_line_number = number_of_line

    print("number_of_line =", number_of_line)

    print()

    print("start_label_legend_table_line_number =" , start_label_legend_table_line_number)
    print("end_label_legend_table_line_number =" ,  end_label_legend_table_line_number)

    print()

    print("start_defects_table_line_number =" , start_defects_table_line_number)
    print("end_defects_table_line_number =" ,  end_defects_table_line_number)

MEASUREMENTNAME=''
ATTRIBUTENAME=''
MEASUREMENTTYPE='Circularity'

# print(type(reader))

