# -*- encoding: utf-8 -*-
import csv
import decimal
from banking.statements.plugin import CSVReaderPlugin
from banking.statements.config import FIELDS
from banking.statements.util import logger, ColumnMismatchError


class NordeaDialect(csv.Dialect):
   "Definitions for reading information from Nordea account statements"

   delimiter = "\t"
   doublequote = False
   escapechar = None
   lineterminator = "\r\n"
   quotechar = '"'
   quoting = csv.QUOTE_MINIMAL
   skipinitialspace = None


MAPPING_V1 = {
   "date": u'Arvop\xe4iv\xe4', "amount": u'M\xe4\xe4r\xe4' ,"description":u"Tapahtuma",
   "account": u"Tilinumero",
   "reference":u"Viite", "message":u"Viesti"
}


class NordeaReaderPlugin(CSVReaderPlugin):
   ""

   # encoding the statement file is in
   ENCODING = "utf-8"

   def __init__(self, linestream, dialect=NordeaDialect(), debug=False):
      CSVReaderPlugin.__init__(self, linestream, debug=debug, dialect=dialect)
      self._mapping = MAPPING_V1
      self._columns = [col.encode(self.ENCODING) for col in mappedcolumns]


   def format_record(self, row):
      data = [row[colname] for colname in self._columns]
      data[1] = decimal.Decimal(data[1].replace(',','.'))
      return tuple(data)


