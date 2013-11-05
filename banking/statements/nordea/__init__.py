# Transaction type mapping for Nordea statement parsers

TRANSACTION_TYPES = {
   "TILISIIRTO": "XFER",
   "PALVELUMAKSU": "FEE",
   "PKORTTIMAKSU": "POS",
   "VIITESIIRTO": "XFER",
   "PIKASIIRTO": "XFER",
   "ETUUS": "XFER",
   "AUTOMAATTINOSTO": "ATM",
   "MAKSUPALVELU": "REPEATPMT",
   "TALLETUSKORKO": "INT",
   "LÄHDEVERO": "FEE",
   "SUORAVELOITUS": "DIRECTDEBIT",
   "PANO": "DEP",
   "VUOKRA": "PAYMENT",
   "VERONPALAUTUS": "DIRECTDEP",
   "PALKKA": "DIRECTDEP",
   "VISA ELECTRON-OSTO": "DIRECTDEBIT", # Added for Nordea
   "ATMOTTO/OTTO.": "ATM", # Added for Nordea
   "PALVELUMAKSU ALV 0%": "FEE",
   "ITSEPALVELU": "ATM",
   "E-MAKSU": "PAYMENT",
}

#   Other types available: 'CREDIT', 'DEBIT', 'INT', 'DIV', 'DEP',
#   'CHECK', 'CASH', 'OTHER'


