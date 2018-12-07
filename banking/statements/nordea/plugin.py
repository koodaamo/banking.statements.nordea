# -*- encoding: utf-8 -*-
import csv
import decimal

from ofxstatement.plugin import Plugin, PluginNotRegistered
from .parser import NordeaCsvStatementParser, SIGNATURES

class NordeaDialect(csv.Dialect):
   "Definitions for reading information from Nordea account statements"

   delimiter = "\t"
   doublequote = False
   escapechar = None
   lineterminator = "\r\n"
   quotechar = '"'
   quoting = csv.QUOTE_MINIMAL
   skipinitialspace = None


class NordeaPlugin(Plugin):
    "Nordea Suomi / Nordea Finland"

    def get_csv_signature(self, csvfile):
        csvfile.readline() # account # line
        csvfile.readline() # first empty
        csvfile.readline() # second empty
        return csvfile.readline().strip()

    def get_parser(self, fin):
        f = open(fin, "r", encoding="1252")
        signature = self.get_csv_signature(f)
        if signature in SIGNATURES:
            parser = NordeaCsvStatementParser(f)
            parser.statement.account_id = self.settings['account']
            parser.statement.currency = self.settings['currency']
            parser.statement.bank_id = self.settings.get('bank', 'Nordea')
            return parser

        # no plugin with matching signature was found
        f.close()
        raise Exception("No suitable Nordea parser found for this statement file.")
