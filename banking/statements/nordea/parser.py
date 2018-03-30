from ofxstatement.parser import CsvStatementParser
import csv
from io import StringIO

from . import TRANSACTION_TYPES

# The bank for some reason has varied the column labeling a lot.
# By collecting first lines of known CSV exports as signatures
# we catch any future changes to the CSV export format.

SIGNATURES = (
"Arvop\xe4iv\xe4\tM\xe4\xe4r\xe4\Tapahtuma\tTilinumero\tSaaja/Maksaja\tViite\tViesti",
"Kirjauspäivä	Arvopäivä	Maksupäivä	Määrä	Saaja/Maksaja	Tilinumero	BIC	Tapahtuma	Viite	Maksajan viite	Viesti	Kortinnumero	Kuitti",
)

COLUMNS = 12

class NordeaCsvStatementParser(CsvStatementParser):
    "parser for various variations with common field semantics"
    
    mappings = {
       "date":0, "amount":3, "payee":4, "trntype":7, "refnum":8, "memo":9
    }

    date_format = "%d.%m.%Y"

    def split_records(self):
        return csv.reader(self.fin, delimiter='\t', quotechar='"')

    def parse_record(self, line):
        # The plugin has iterated over the prefix lines for us already
        #if self.cur_record <= 3:
        #    return None

        # Change decimalsign from , to .
        line[3] = line[3].replace(',', '.')

        # Set transaction type
        transaction_type = line[7].upper()
        if transaction_type in TRANSACTION_TYPES:
            line[7] = TRANSACTION_TYPES[transaction_type]
        else:
            line[7] = 'DEBIT' if line[3][0] == '-' else 'CREDIT'

        # the CSV leaves off empty data at the end of record
        # so we fill in some blanks
        missing = COLUMNS - len(line)
        line.extend(missing * [""])

        # fill statement line according to mappings
        sl = super(NordeaCsvStatementParser, self).parse_record(line)
        return sl

