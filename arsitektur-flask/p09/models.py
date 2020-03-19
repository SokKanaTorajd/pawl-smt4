class lab_model():
    def __init__(self,nama=None, spec=None, jmlh=None):
        self.nama=nama
        self.spec=spec
        self.jmlh=jmlh
    
    def setNama(self,nama):
        self.nama=nama

    def cetakNama(self):
        return self.nama
    
    def setSpec(self,spec):
        self.spec = spec
    
    def cetakSpec(self):
        return self.spec
    
    def setJmlh(self, jmlh):
        self.jmlh = jmlh
        
    def cetakJmlh(self):
        return self.jmlh
