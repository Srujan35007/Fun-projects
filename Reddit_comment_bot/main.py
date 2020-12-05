# this is a test for sjn_test_bot_1
import time 
b = time.time()
import praw
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np 
import matplotlib.pyplot as plt 
a = time.time()
print(f'Imports complete in {a-b} seconds.')

class Small_net(nn.Module):
    def __init__(self, word_window = 10):
        super(Small_net, self).__init__()
        self.window = word_window
        self.layers = nn.Sequential(
        nn.Linear(word_window, 100),
        nn.ReLU(True),
        nn.Linear(100, 50),
        nn.ReLU(True),
        nn.Linear(50, 1),
        nn.Sigmoid()
        )
    
    def forward(self, x):
        x = x.view(-1,self.window)
        return self.layers(x)

net = Small_net()
print(net)

session = praw.Reddit(
    user_agent = "Session Test 1",
    client_id = "CLIENT_ID",
    client_secret = "CLIENT_SECRET",
    username = 'sjn_test_bot_1'
)

subreddit = session.subreddit("Jokes")
print('Test okay')
