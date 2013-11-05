from ofxstatement.parser import CsvStatementParser
import csv
from io import StringIO

from . import TRANSACTION_TYPES

# The bank for some reason has varied the column labeling a lot.
# By collecting first lines of known CSV exports as signatures
# we catch any future changes to the CSV export format.

SIGNATURES = (
"Arvop\xe4iv\xe4\tM\xe4\xe4r\xe4\Tapahtuma\tTilinumero\tSaaja/Maksaja\tViite\tViesti",
)

class NordeaCsvStatementParser(CsvStatementParser):
    "parser for various variations with common field semantics"
    
    mappings = {
       "date":0, "amount":1, "trntype":2, "acctto":3, "payee":4,
       "refnum":5, "memo":6
    }

    date_format = "%d.%m.%Y"

    def __init__(self, fin):
        sin=StringIO()
        for l in fin:
           # Some versions from 2011 have broken CSV...
           sin.write(l.replace("&amp;amp;", "&"))
        sin.seek(0)
        super().__init__(sin)

    def split_records(self):
        return csv.reader(self.fin, delimiter='\t', quotechar='"')

    def parse_record(self, line):
        #Free Headerlines
        if self.cur_record <= 2:
            return None

        # Change decimalsign from , to .
        line[1] = line[1].replace(',', '.')

        # Set transaction type
        line[2] = TRANSACTION_TYPES[line[2]]

        # fill statement line according to mappings
        sl = super(NordeaCsvStatementParser, self).parse_record(line)
        return sl
