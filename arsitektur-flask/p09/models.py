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

data_lab = [
            {
                "nama": "Laboratorium 1",
                "spec": ["Intel Core i3", "RAM 4GB", "500GB HDD", "Monitor 19 inch"],
                "jmlh": "45 PC"
            },
            {
                "nama": "Laboratorium 2",
                "spec": ["Intel Core i5", "RAM 4GB", "1TB HDD", "Monitor 21.5 inch"],
                "jmlh": "50 PC"
            }

]