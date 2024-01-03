import pandas as pd

class Transforms:
    def __init__(self,dataset,param0='',param1='',how='inner'):
        self.dataset = dataset
        self.param0 = param0
        self.param1 = param1
        self.how = how

    def transform_state(self):
        df = pd.merge(self.dataset, self.param0, on=self.param1, how=self.how)
        return df