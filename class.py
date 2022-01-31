class Car (object):
    def __init__(self,Model,Color,TopSpeed,Company):
        self.Modle=Model
        self.Color=Color
        self.TopSpeed=TopSpeed
        self.Company=Company
    def Start (self):
        print('started')
    def Stop (self):
        print('stopped')
audi=Car('Q7','crimson','300Kmph','Audi')
print(audi.Start())