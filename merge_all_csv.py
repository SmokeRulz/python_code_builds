
#needed this for a simple merging of CSV files 
import os
import glob
import pandas as pd
cwd = os.getcwd()
print(cwd)
os.chdir("..\..\..\excel_file") #added this for windows system since my working directory was C: drive. Change this accordingly
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')





