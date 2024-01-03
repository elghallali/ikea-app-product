import pandas as pd

class Extracts:
    def __init__(self,datasource):
        self.datasource = datasource
        self.extension = self.datasource.split('/')[-1].split('.')[-1]

    def __read_csv_file(self, sep=','):
        df = pd.read_csv(filepath_or_buffer=self.datasource, sep=sep)
        return df
    
    def __read_excel_file(self):
        df = pd.read_excel(io=self.datasource)
        return df
    
    
    
    def load_data(self):
        if self.extension in ['xlsx', 'xls']:
            return self.__read_excel_file()
        elif self.extension in ['csv', 'tsv', 'txt']:
            return self.__read_csv_file()
        elif self.extension == 'tsv':
            return self.__read_csv_file(sep=' ')