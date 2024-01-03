import pandas as pd

class Loads:
    def __init__(self,dataset, outputdir,filename):
        self.dataset = dataset
        self.outputdir = outputdir
        self.filename = filename

    def send_to_csv(self):
        self.dataset.to_csv(path_or_buf=self.outputdir + self.filename, index=False)
    
    def send_to_excel(self):
        self.dataset.to_excel(excel_writer=self.outputdir + self.filename, index=False)

    def send_to_pickle(self):
        self.dataset.to_pickle(path=self.outputdir + self.filename, compression='gzip')