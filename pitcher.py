class Pitcher: 
    
    def __init__(self, data):
        self.data = data
        row = data[0].split(",")
        self.pos = str(row[1])
        self.name = str(row[2])
        self.wins = int(row[4])
        self.losses = int(row[5])
        self.era = float(row[7])
        self.saves = int(row[13])
        self.ip = float(row[14])
        self.hits = int(row[15])
        self.bb = int(row[19])
        self.so = int(row[21])