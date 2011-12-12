# -*- encoding: utf-8 -*-
import csv
import decimal
from banking.statements.plugin import CSVReaderPlugin
from banking.statements.util import logger, ColumnMismatchError

from banking.statements import AccountEntryRecord as Record

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
   "account": u"Tilinumero", "payee_or_recipient": u"Saaja/Maksaja",
   "reference":u"Viite", "message":u"Viesti"
}


class NordeaReaderPlugin(CSVReaderPlugin):
   ""

   # encoding the statement file is in
   ENCODING = "utf-8"

   def __init__(self, linestream, dialect=NordeaDialect(), debug=False):

      # pop away the two first lines with acc number & newline
      linestream.next()
      linestream.next()

      CSVReaderPlugin.__init__(self, linestream, debug=debug, dialect=dialect)
      self._mapping = MAPPING_V1
      mappedcolumns = [self._mapping[commonfield] for commonfield in Record._fields]
      self._columns = [col.encode(self.ENCODING) for col in mappedcolumns]


   def can_parse(self, stream):
      "return True if this plugin can parse the stream"
      raise NotImplementedError

   def format_record(self, row):
      data = [row[colname] for colname in self._columns]
      data[1] = decimal.Decimal(data[1].replace(',','.'))
      return Record._make(data)


