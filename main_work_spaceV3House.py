# PUMS Data collection package 1.0.
# Created by: Skyler Fetter 4/17/2019
#


import pandas as pd
import numpy as np
import string
import re
import glob
import gc

# pre allocated space for variables

path = []
household_headers = []
people_headers = []
household_vars = []
people_vars = []
on_off = 1
holder_list = []
merged_headerlist = []
household_selection = pd.DataFrame()
people_selection = pd.DataFrame()
household_selectionTwo = pd.DataFrame()
people_selectionTwo = pd.DataFrame()

# first ask for year
selection = input("Please choose a year: 2005, 2017: ")
print('One moment Please.')

# Note: I should change this to searching for file names (will change this when the time comes (time constraints)
if selection == '2017':
    path = glob.glob('D:/PUMS/Contained/2017_*.csv')
else:
    path = glob.glob('D:/PUMS/Contained/2005_*.csv')

# after year is gotten then we get each file

print('Working with first section of data')
# THis is to just cut down on time.
# I dont think I need to get the personal for this. Just focused on household)

    
household_One = pd.DataFrame(pd.read_csv(path[0]))
household_headers = household_One[:0]




# after files are gotten we get the headers for each one




print('--------PART ONE OF DATA-------')

#---------------PART ONE--------------# #NOTE : might use ints in order to save space.
# if they share vars, maybe it would be smart to just not include them in both?
print("Variable selection, please select")
print('to exit, type "exit"')
while on_off == 1:
    var_selection = input('please enter a variable: ')
    if var_selection in household_headers:
            household_vars.append(var_selection)
       
    elif var_selection == 'end':
        on_off = 0
    print('---------Current Variables------')
    print('household: ', household_vars)


#~~~~~~~~~~~~~~~~~~~~~~~~Now to do the selection process.~~~~~~~~~~~~~~~~~~~~~~~

household_selection[household_vars] = household_One.loc[:,household_vars]

#~~~~~~~~~~~~~~~~gonna have to delete part one base items as.~~~~~~~~~~~~~~~~~~~~
del household_One
gc.collect()

print('Dataframe selection done')
print('~~~~~~~~~~~~~~~~~Now merging PART 1~~~~~~~~~~~~~~~')


# ~~~~~~~~~~~~~~~~~if i just merged them....for now~~~~~~~~~~~~~~~~~#
part_One = household_selection

print('Merge one done, now to clean up')
del [household_selection]
gc.collect()

print('done cleaning up')

print('-----Now Working On Part 2 of data------')


household_Two = pd.DataFrame(pd.read_csv(path[1]))



print('------Part 2 data import done--------------')

print('------Now dataframe selection--------------')
household_selectionTwo[household_vars] = household_Two.loc[:,household_vars]


del [household_Two]
gc.collect()

print('------DataFrame Selection Done--------------')

print('-----Now merging Part 2-----')
part_Two = household_selectionTwo

del [household_selectionTwo]
gc.collect()

print('-----Done-----')

print('---merging part one and part 2-----')

part_One.append(part_Two, ignore_index = True)

# once merged, I want to then merge the state and county fips together



print('------Now exporting------')
name_input = input("what do you want to name it? :")

part_One.to_csv(name_input + '.csv')


print('----- Done -----')

exit()










            
    
            
