#contoh model utk Flask

class contohModel():
	"""docstring for contohModel"""
	def __init__(self, text=None):
		self.text = text

	def cetakTeks(self,text):
		return self.text


class modelBerita():
	"""docstring for modelBerita"""
	def __init__(self, judul=None, tanggal=None, isi=None):
		self.judul = judul
		self.tanggal = tanggal
		self.isi = isi

	def setJudul(self,judul):
		self.judul = judul

	def cetakJudul(self):
		return self.judul

	def setTanggal(self,tanggal):
		self.tanggal = tanggal

	def cetakTanggal(self):
		return self.tanggal

	def setIsi(self, isi):
		self.isi = isi

	def cetakIsi(self):
		return self.isi