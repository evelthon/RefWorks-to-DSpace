#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv as csv
from collections import OrderedDict

class SpreadSheet:
    def __init__(self):
        self.di = OrderedDict()
        self.csvRow = None
        return None

    def exportCSV(self):
        return None

    def importCSV(self):
        di = OrderedDict()
        readdata = csv.reader(open("./epa.csv"))
        i=0
        for row in readdata:
            # print (row)
            di[i] = row
            i += 1

        # print (len(di))
        #
        # print(di[0])
        # print(di[1])

        # for key, value in di.items():
        #     print(str(key) + ': ' + value[2])

        oDi = OrderedDict()
        j = 0
        for key, value in di.items():
            oDi[key] = {}
            self.csvRow = value
            # dc.type
            oDi[key][0] = self.generate_repeative_fields([0])
            # dc.contributor.author
            oDi[key][1] = self.generate_repeative_fields([1, 20, 21, 22])
            # dc.title
            oDi[key][2] = self.generate_repeative_fields([2, 16])
            # dc.source
            oDi[key][3] = self.generate_repeative_fields([3, 4])
            # if oDi[key][3]:
            #     print(oDi[key][3])


            # dc.date.issued
            oDi[key][4] = self.generate_repeative_fields([5])
            # dc.date.available
            oDi[key][5] = self.generate_repeative_fields([6])
            # dc.description.volume
            oDi[key][6] = self.generate_repeative_fields([7])
            # dc.description.issue
            oDi[key][7] = self.generate_repeative_fields([8])
            # dc.description.startingpage
            oDi[key][8] = self.generate_repeative_fields([9])
            # dc.description.endingpage
            oDi[key][9] = self.generate_repeative_fields([10])
            # dc.subject
            oDi[key][10] = self.generate_repeative_fields([11])
            # dc.description.abstract
            oDi[key][11] = self.generate_repeative_fields([12])
            # dc.description
            oDi[key][12] = self.generate_repeative_fields([13, 14])
            # dc.description.edition
            oDi[key][13] = self.generate_repeative_fields([17])
            # dc.publisher
            oDi[key][14] = self.generate_repeative_fields([18])
            # dc.coverage.spatial
            oDi[key][15] = self.generate_repeative_fields([19])
            # dc.identifier
            oDi[key][16] = self.generate_repeative_fields([24])
            # dc.identifier.lc
            oDi[key][17] = self.generate_repeative_fields([27, 29, 37])
            # dc.language.iso
            oDi[key][18] = self.generate_repeative_fields([28])
            # dc.title.alternative
            oDi[key][19] = self.generate_repeative_fields([31])
            # dc.source.uri
            oDi[key][20] = self.generate_repeative_fields([32, 33])
            # dc.identifier.doi
            oDi[key][21] = self.generate_repeative_fields([34])
            # dc.source
            oDi[key][22] = self.generate_repeative_fields([38, 39])

            # dc.contributor.editor
            oDi[key][23] = self.generate_repeative_fields([15])

        # for key, value in oDi.items():
        #     print (str(key) + ': ' + value[23])

        with open('export.csv', 'w') as csvfile:
            fieldnames = ['id',
                          'collection',
                          'dc.type',
                          'dc.contributor.author',
                          'dc.title',
                          'dc.source',
                          'dc.date.issued',
                          'dc.date.available',
                          'dc.description.volume',
                          'dc.description.issue',
                          'dc.description.startingpage',
                          'dc.description.endingpage',
                          'dc.subject',
                          'dc.description.abstract',
                          'dc.description',
                          'dc.description.edition',
                          'dc.contributor.editor',
                          'dc.publisher',

                          'dc.coverage.spatial',
                          'dc.identifier',
                          'dc.identifier.lc',
                          'dc.language.iso',
                          'dc.title.alternative',
                          'dc.source.uri',
                          'dc.identifier.doi',
                          'dc.source'
                          ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for key, value in oDi.items():
                writer.writerow({'id': '+',
                                 'collection': '10797/21077',
                                 'dc.type': oDi[key][0],
                                 'dc.contributor.author': oDi[key][1],
                                 'dc.title': oDi[key][2],
                                 'dc.source': oDi[key][3],
                                 'dc.date.issued': oDi[key][4],
                                 'dc.date.available': oDi[key][5],
                                 'dc.description.volume': oDi[key][6],
                                 'dc.description.issue': oDi[key][7],
                                 'dc.description.startingpage': oDi[key][8],
                                 'dc.description.endingpage': oDi[key][9],
                                 'dc.subject': oDi[key][10],
                                 'dc.description.abstract': oDi[key][11],
                                 'dc.description': oDi[key][12],
                                 'dc.description.edition': oDi[key][13],
                                 'dc.contributor.editor': oDi[key][23],
                                 'dc.publisher': oDi[key][14],

                                 'dc.coverage.spatial': oDi[key][15],
                                 'dc.identifier': oDi[key][16],
                                 'dc.identifier.lc': oDi[key][17],
                                'dc.language.iso': oDi[key][18],

                                'dc.title.alternative': oDi[key][19],
                                'dc.source.uri': oDi[key][20],
                                'dc.identifier.doi': oDi[key][21],
                                'dc.source': oDi[key][22]
                                 })
                # print(str(key) + ': ' + value[23])

    def generate_repeative_fields(self, var_list = None):
        # Generate a stringlist of source fields
        # my_list is a list of fields seperated with ';' by RefWorks export. They need to change to '||'
        # this happens in author fields
        my_list = {
                    # authors
                    1, 15, 20, 21, 22,
                    # Subjects
                    11
        }
        temp_list = list()

        for var in var_list:
            if var in my_list:
                self.csvRow[var] = self.replace_greek_questionmark_with_vertical(self.csvRow[var])
            temp_list.append(self.csvRow[var].strip())

        return '||'.join(filter(None, temp_list)).strip()

    def replace_greek_questionmark_with_vertical(self, var):
        return var.replace(';', '||')


if __name__ == "__main__":
    try:
        obj = SpreadSheet()
        obj.importCSV()


    except AttributeError:
        print ("\nUse -h for instructions.\n")