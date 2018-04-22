'''
Created on 18 Apr 2018
 

@author: neale samways
'''

import os, glob, csv
import numpy as np

# results header index's
correct = 0
font_size = 1
response = 2
response_time = 3
trial_target = 4


# parameter variables
lookback_length = 4
task_target = 3

print("SART Results processor")

path = os.curdir

# do a glob to get the files in the directory *BEFORE* creating the output file
existing_files = glob.glob(os.path.join(path, 'subject_*.csv'))

if len(existing_files) > 0:
    # open outfile
    out_name = open(os.path.join(path, 'processedResults.csv'),'wb') 
    out_handle = csv.writer(out_name)

    # write the headers
    out_handle.writerow(['Participant' , 'Errors', 'FPP W', 'FPP N'])

else:
        print("No raw results files to process")
        
for current_file in existing_files:
  
    print("Now processing" + current_file)
    
    # clear variables and arrays    
    summed_score = 0
    processed_trials = 0
    

    # set up the sliding window
    lookback_list = []

     
    # open CSV and read in line by line
    with open(current_file, 'rb') as f:
        # discard first line, which contains the headers
        next(f)
        # read in the remainder of the file
        read_in = csv.reader(f)
        for curr_row in read_in:
        #  this is at the `row` level        
            summed_score += int(curr_row[correct])
            processed_trials += 1
        
            if (curr_row[target] == target):
                # this is a target trial
                # check if the length of the lookback array is long enough
                if (len(lookback_list) == lookback_length):
                    # do the calculation and push results on to the results stack
                    pass
            else:
                # this is a non-target trial, so just push the relevant data on to the lookback array, and pop off 5th element if necessary
              #  lookback_list.insert(0,[curr_row[]
            
            # write the outfile if the number of errors is acceptable
        
                # calculate percent score    
        per_corr = 100.0*( float(summed_score)/float(processed_trials))

        #write name (clean current file first)
        infilename = current_file[2:]
        linedata = [infilename, diff_score, summed_score, per_corr, processed_trials, lb_count, hb_count] 
        out_handle.writerow(linedata)

print('Processed ' + str(len(existing_files)) + ' results files')
#close the outfile
out_name.close()