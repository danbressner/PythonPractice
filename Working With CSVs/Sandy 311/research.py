import os
import csv
from collections import namedtuple
from typing import List


data = []

Record = namedtuple('Record', ('''date NYC311 ACS BPSI CAU CHALL
                               DEP DOB DOE DOF DOHMH DPR FEMA HPD
                               HRA MFANYC MOSE NYCEM NYCHA
                               NYCSERVICE NYPD NYSDOL
                               SBS NYSEMERGENCYMG total'''))


def init():
    '''Read in CSV data and store as a list of namedtuples'''
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'sandy-311-calls-by-day.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)


def parse_row(row):
    '''parse fields by data type, store row as a namedtupled'''
    row['date'] = str(row['date'])
    row['NYC311'] = int(row['NYC311'])
    row['ACS'] = int(row['ACS'])
    row['BPSI'] = int(row['BPSI'])
    row['CAU'] = int(row['CAU'])
    row['CHALL'] = int(row['CHALL'])
    row['DEP'] = int(row['DEP'])
    row['DOB'] = int(row['DOB'])
    row['DOE'] = int(row['DOE'])
    row['DOF'] = int(row['DOF'])
    row['DOHMH'] = int(row['DOHMH'])
    row['DPR'] = int(row['DPR'])
    row['FEMA'] = int(row['FEMA'])
    row['HPD'] = int(row['HPD'])
    row['HRA'] = int(row['HRA'])
    row['MFANYC'] = int(row['MFANYC'])
    row['MOSE'] = int(row['MOSE'])
    row['NYCEM'] = int(row['NYCEM'])
    row['NYCHA'] = int(row['NYCHA'])
    row['NYCSERVICE'] = int(row['NYCSERVICE'])
    row['NYPD'] = int(row['NYPD'])
    row['NYSDOL'] = int(row['NYSDOL'])
    row['SBS'] = int(row['SBS'])
    row['NYSEMERGENCYMG'] = int(row['NYSEMERGENCYMG'])
    row['total'] = int(row['total'])

    record = Record(**row)

    return record


def call_days() -> List[Record]:
    '''Return the days with the highest total call volume'''
    return sorted(data, key=lambda r: r.total, reverse=True)


def fema_calls() -> List[Record]:
    '''Return the days with the highest FEMA-associated call volume'''
    return sorted(data, key=lambda r: r.FEMA, reverse=True)


def day_lookup():
    rep = input('Do you want to look up a specific day? - Y or N: ')
    if rep == 'Y':
        enter_date = input('Enter a date (m/d/yy): ')
        lookup = [row for row in data if row.date == enter_date]
        print(lookup)
    elif rep == 'N':
        print('Ok, exiting the program.')
    else:
        print('Invalid input, exiting the program.')
