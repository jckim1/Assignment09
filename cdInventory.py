#------------------------------------------#
# Title: cdInventory.py
# Desc: Main app module for running CD Inventory
# Change Log: (Who, When, What)
# Jkim, 2022-Dec-11, Created File
# Jkim, 2022-Dec-11, commented code
#------------------------------------------#

import ProcessingClasses as p
import IOClasses as io

lstFileNames = ['albuminventory.txt', 'track_inventory.txt']
lstOfCDObjects = io.FileIO.load_inventory(lstFileNames)

while True:
    io.ScreenIO.print_menu()
    strChoice = io.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = io.FileIO.load_inventory(lstFileNames)
            io.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            io.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = io.ScreenIO.get_CD_info()
        p.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        io.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        io.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        io.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album index: ')
        cd = p.DataProcessor.select_cd(lstOfCDObjects, cd_idx)

        while True:
            io.ScreenIO.print_CD_menu()
            strChoice = io.ScreenIO.menu_CD_choice()
            if strChoice == 'x':
                break
            elif strChoice == 'a':
                track_info = io.ScreenIO.get_track_info()
                p.DataProcessor.add_track(track_info,cd)
                print('Track successfully added to album.')
            elif strChoice == 'd':
                io.ScreenIO.show_tracks(cd)
            elif strChoice == 'r':
                io.ScreenIO.show_tracks(cd)
                track_id = input('Select the track you want removed: ')
                try:
                    track_id = int(track_id)
                    flag = 0
                except:
                    print('Track index must be an integer!')
                cd.rmv_track(track_id)
        else:
            print('Your choice is not one of the options, please choose again.')     

    elif strChoice == 's':
        io.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            io.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')
