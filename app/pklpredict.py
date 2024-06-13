from ..base_model import BaseModel

'''
    def client model class - def a concrete implemt of the BM abc class
'''

class PredictClass(BaseModel):
    # this class takes from BM and provides an implementation for the abc predict method.
    def predict(self, input_data):
        return self.model.predict(input_data)
