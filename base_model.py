from abc import ABC, abstractmethod
import pickle


'''
    gives a template for loading a model and making predict.
    every method in the BaseModel uses the abc method.
'''

class BaseModel(ABC):
    # loading it from a path
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self._load_model()
    # 
    @abstractmethod
    def predict(self, input_data):
        pass
    
    # Loads the model from file path
    def _load_model(self):
        with open(self.model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    


