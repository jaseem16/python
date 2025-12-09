import barcode
from barcode.writer import ImageWriter

code = barcode.get_barcode_class('ean13')
ean = code('5901234123457', writer=ImageWriter())
ean.save("barcode")
