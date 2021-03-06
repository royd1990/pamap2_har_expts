class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        # defining layers
        self.conv1 = nn.Conv1d(3, 2, 3)
        self.conv2 = nn.Conv1d(2, 1, 3)
#         self.conv3 = nn.Conv1d(15, 20, 3)
        self.pamap = nn.Linear(46, 12)
        self.robogame = nn.Linear(46, 4)
#         self.fc2 = nn.Linear(128, 64)
#         self.fc3 = nn.Linear(64, 4)
        
        nn.init.xavier_uniform_(self.conv1.weight, gain = nn.init.calculate_gain('relu'))
        nn.init.xavier_uniform_(self.conv2.weight, gain = nn.init.calculate_gain('relu'))
        nn.init.xavier_uniform_(self.pamap.weight, gain = nn.init.calculate_gain('sigmoid'))
        nn.init.xavier_uniform_(self.robogame.weight, gain = nn.init.calculate_gain('sigmoid'))
        
    # use flag = True during fine-tuning 
    def forward(self, signal, flag = False):
        signal = torch.transpose(signal, 1, 2)
        out = F.relu(self.conv1(signal))
        out = F.relu(self.conv2(out))
        out = torch.transpose(out, 1, 2)
        out = out.reshape(-1, 46)
        if flag : 
            out = F.log_softmax(self.robogame(out), dim = 1)
        else :
            out = F.log_softmax(self.pamap(out), dim = 1)
        return out