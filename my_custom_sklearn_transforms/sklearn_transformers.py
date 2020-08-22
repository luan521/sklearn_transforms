from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
import numpy as np


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
    
  
class NotaZerada():
    def transform(self, X):

        nota=[[],[],[],[]]

        for i in range(len(X['NOTA_DE'])):
            if (X['REPROVACOES_DE'][i]==0 and X['NOTA_DE'][i]==0):
                nota[0].append(100)
            else:
                nota[0].append(X['NOTA_DE'][i])
            if (X['REPROVACOES_EM'][i]==0 and X['NOTA_EM'][i]==0):
                nota[1].append(200)
            else:
                nota[1].append(X['NOTA_EM'][i])
            if (X['REPROVACOES_MF'][i]==0 and X['NOTA_MF'][i]==0):
                nota[2].append(300)
            else:
                nota[2].append(X['NOTA_MF'][i])
            if (X['REPROVACOES_GO'][i]==0 and X['NOTA_GO'][i]==0):
                nota[3].append(400)
            else:
                nota[3].append(X['NOTA_GO'][i])
        
        self=nota
        
        data = X.copy()
        data['NOTA_DE']=nota[0]
        data['NOTA_EM']=nota[1]
        data['NOTA_MF']=nota[2]
        data['NOTA_GO']=nota[3]

        return data
  


class ReprovacaoBinaria():
    def transform(self, X):
        data=X.copy()
        data['REPROVACOES_DE']=data['REPROVACOES_DE'].map({0:0,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1})
        data['REPROVACOES_EM']=data['REPROVACOES_EM'].map({0:0,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1})
        data['REPROVACOES_MF']=data['REPROVACOES_MF'].map({0:0,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1})
        data['REPROVACOES_GO']=data['REPROVACOES_GO'].map({0:0,1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1})
    
        return data



class CustomScaler(BaseEstimator,TransformerMixin): 
    
    # init or what information we need to declare a CustomScaler object
    # and what is calculated/declared as we do
    
    def __init__(self,columns,copy=True,with_mean=True,with_std=True):
        
        # scaler is nothing but a Standard Scaler object
        self.scaler = StandardScaler(copy,with_mean,with_std)
        # with some columns 'twist'
        self.columns = columns
        self.mean_ = None
        self.var_ = None
        
    
    # the fit method, which, again based on StandardScale
    
    def fit(self, X, y=None):
        self.scaler.fit(X[self.columns], y)
        self.mean_ = np.mean(X[self.columns])
        self.var_ = np.var(X[self.columns])
        return self
    
    # the transform method which does the actual scaling

    def transform(self, X, y=None, copy=None):
        
        # record the initial order of the columns
        init_col_order = X.columns
        
        # scale all features that you chose when creating the instance of the class
        X_scaled = pd.DataFrame(self.scaler.transform(X[self.columns]), columns=self.columns)
        
        # declare a variable containing all information that was not scaled
        X_not_scaled = X.loc[:,~X.columns.isin(self.columns)]
        
        # return a data frame which contains all scaled features and all 'not scaled' features
        # use the original order (that you recorded in the beginning)
        return pd.concat([X_not_scaled, X_scaled], axis=1)[init_col_order]
   

    
class TrainTest():
    def transform(self, X):
        data=X.copy()
        
        #Transformando os dados em numpy.array
        data=np.array(data)
        inputs=data[:,:-1]
        targets=data[:,-1]
        
        #Shuffle the data
        shuffled_indices=np.arange(inputs.shape[0])
        np.random.shuffle(shuffled_indices)
        shuffled_inputs=inputs[shuffled_indices]
        shuffled_targets=targets[shuffled_indices]
        
        #Dividindo os dados em: train, test
        samples_count=inputs.shape[0]
        train_samples_count=int(0.7*samples_count)
        x_train=shuffled_inputs[:train_samples_count]
        y_train=shuffled_targets[:train_samples_count]
        x_test=shuffled_inputs[train_samples_count:]
        y_test=shuffled_targets[train_samples_count:]
            
        
        return x_train, y_train, x_test,y_test
