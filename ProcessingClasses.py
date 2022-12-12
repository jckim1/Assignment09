#------------------------------------------#
# Title: Processing Classes
# Desc: Module to process data classes
# Change Log: (Who, When, What)
# Jkim, 2022-Dec-11, Created File
# Jkim, 2022-Dec-11, Extended functionality to add tracks
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as dc

class DataProcessor:
    """Processing app data"""
    @staticmethod
    def add_CD(cdInfo, table):
        """Adds CD information to inventory.
        Args:
            cdInfo (tuple): Holds data about the cd to be added to inventory (ID, CD Title, CD Artist).
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        Returns:
            None.
        """

        cdId, title, artist = cdInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = dc.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> dc.CD:
        """selects a CD object out of table that has the ID cd_idx
        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return
        Raises:
            Exception: If id is not in list.
        Returns:
            row (dc.CD): CD object that matches cd_idx
        """

        try:
            cd_idx = int(cd_idx)
        except ValueError as e:
            print('ID must be an integer.')
            print(e.__doc__)
        for row in table:
            if row.cd_id == cd_idx:
                return row
        raise Exception('The ID you gave does not exist in inventory.')

    @staticmethod
    def add_track(track_info: tuple, cd: dc.CD) -> None:
        """adds a Track object with attributes in track_info to cd
        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (dc.CD): cd object the tarck gets added to.
        Raises:
            Exception: DESCraised in case position is not an integer.
        Returns:
            None: DESCRIPTION.
        """

        position, title, length = track_info
        try:
            position = int(position)
        except:
            raise Exception('Position must be an integer.')
        track = dc.Track(position, title, length)
        cd.add_track(track)