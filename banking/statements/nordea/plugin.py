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
    "Suomen Osuuspankki / Finnish Osuuspankki"

    def get_parser(self, fin):
        f = open(fin, "r", encoding='UTF-8')
        signature = f.readline().strip()
        f.seek(0)
        if signature in SIGNATURES:
            parser = NordeaCsvStatementParser(f)
            parser.statement.account_id = self.settings['account']
            parser.statement.currency = self.settings['currency']
            parser.statement.bank_id = self.settings.get('bank', 'Nordea')
            return parser

        # no plugin with matching signature was found
        raise Exception("No suitable Nordea parser found for this statement file.")
