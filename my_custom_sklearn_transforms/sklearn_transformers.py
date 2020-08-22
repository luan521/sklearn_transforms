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
    
    
class DadosNulos():
    def __init__(self, columns):
        self=None

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
       
        new_data=[[],[],[],[],[],[],[],[],[],[],[]]
        

        for i in range(len(X['REPROVACOES_DE'])):
            if not(X['REPROVACOES_DE'][i] <=0 or X['REPROVACOES_DE'][i] >0) :
                new_data[0].append(0)
            else:
                new_data[0].append(X['REPROVACOES_DE'][i])
            if not(X['REPROVACOES_EM'][i] <=0 or X['REPROVACOES_EM'][i] >0) :
                new_data[1].append(0)
            else:
                new_data[1].append(X['REPROVACOES_EM'][i])
            if not(X['REPROVACOES_MF'][i] <=0 or X['REPROVACOES_MF'][i] >0) :
                new_data[2].append(0)
            else:
                new_data[2].append(X['REPROVACOES_MF'][i])
            if not(X['REPROVACOES_GO'][i] <=0 or X['REPROVACOES_GO'][i] >0) :
                new_data[3].append(40)
            else:
                new_data[3].append(X['REPROVACOES_GO'][i])
            if not(X['NOTA_DE'][i] <=0 or X['NOTA_DE'][i] >0) :
                new_data[4].append(0)
            else:
                new_data[4].append(X['NOTA_DE'][i])
            if not(X['NOTA_EM'][i] <=0 or X['NOTA_EM'][i] >0) :
                new_data[5].append(0)
            else:
                new_data[5].append(X['NOTA_EM'][i])
            if not(X['NOTA_MF'][i] <=0 or X['NOTA_MF'][i] >0) :
                new_data[6].append(0)
            else:
                new_data[6].append(X['NOTA_MF'][i])
            if not(X['NOTA_GO'][i] <=0 or X['NOTA_GO'][i] >0) :
                new_data[7].append(0)
            else:
                new_data[7].append(X['NOTA_GO'][i])
            if not(X['H_AULA_PRES'][i] <=0 or X['H_AULA_PRES'][i] >0) :
                new_data[8].append(0)
            else:
                new_data[8].append(X['H_AULA_PRES'][i])
            if not(X['TAREFAS_ONLINE'][i] <=0 or X['TAREFAS_ONLINE'][i] >0) :
                new_data[9].append(0)
            else:
                new_data[9].append(X['TAREFAS_ONLINE'][i])
            if not(X['FALTAS'][i] <=0 or X['FALTAS'][i] >0) :
                new_data[10].append(0)
            else:
                new_data[10].append(X['FALTAS'][i])
        
        self=new_data
        data = X.copy()
        
        data['REPROVACOES_DE']=new_data[0]
        data['REPROVACOES_EM']=new_data[1]
        data['REPROVACOES_MF']=new_data[2]
        data['REPROVACOES_GO']=new_data[3]
        data['NOTA_DE']=new_data[4]
        data['NOTA_EM']=new_data[5]
        data['NOTA_MF']=new_data[6]
        data['NOTA_GO']=new_data[7]
        data['H_AULA_PRES']=new_data[8]
        data['TAREFAS_ONLINE']=new_data[9]
        data['FALTAS']=new_data[10]
        
        return data
