import torch
import torch.utils.data as data
import torch.utils.data.dataset as dataset
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import random
#import pandas as pd
class Nav_Dataset(dataset.Dataset):
    def __init__(self):
        self.data = np.genfromtxt(r'saved/training_data.csv', delimiter=',')
        random.shuffle(self.data)
        #print("data is ",self.data[0])
        
# STUDENTS: it may be helpful for the final part to balance the distribution of your collected data
        # normalize data and save scaler for inference
        self.scaler = MinMaxScaler()
        self.normalized_data = self.scaler.fit_transform(self.data) #fits and transforms
        pickle.dump(self.scaler, open("saved/scaler.pkl", "wb")) #save to normalize at inference
    

    def __len__(self):
# STUDENTS: __len__() returns the length of the dataset
        rows = len(self.data)
        return rows

    def __getitem__(self, idx):
        if not isinstance(idx, int):
            #print(idx.item())
            #print(idx)
            #print("idx is ",idx)
            idx = idx.item()
            #print(idx)
            
            return idx
        #return idx
# STUDENTS: for this example, __getitem__() must return a dict with entries {'input': x, 'label': y}
# x and y should both be of type float32. There are many other ways to do this, but to work with autograding
# please do not deviate from these specifications.


class Data_Loaders():
    def __init__(self, batch_size):
        self.nav_dataset = Nav_Dataset()
        l = round(len(self.nav_dataset)/1.5)
        temp = self.nav_dataset.data[:l]
        temp1 = self.nav_dataset.data[l:]
        
        
          
        #self.train_loader.data = self.train_loader.data
        self.train_loader = list()
        self.test_loader = list()
        for r in temp:
            i = r[0:6]
            o = r[6]
            row = {'input':i,'label':o}
            self.train_loader.append(row)
        for r in temp1:
            i = r[0:6]
            o = r[6]
            row = {'input':i,'label':o}
            self.test_loader.append(row)
        
# STUDENTS: randomly split dataset into two data.DataLoaders, self.train_loader and self.test_loader
# make sure your split can handle an arbitrary number of samples in the dataset as this may vary

def main():
    batch_size = 16
    data_loaders = Data_Loaders(batch_size)
    
    
    # STUDENTS : note this is how the dataloaders will be iterated over, and cannot be deviated from
    #for idx, sample in enumerate(data_loaders.train_loader):
    #    print("IDX",idx)
    #    print("sample: ",sample)
    for idx, sample in enumerate(data_loaders.train_loader):
        _, _ = sample['input'], sample['label']
    for idx, sample in enumerate(data_loaders.test_loader):
        _, _ = sample['input'], sample['label']
    

if __name__ == '__main__':
    main()
