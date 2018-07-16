class Car:
  def Getowner(self):
    print("owner is ",self._Name)
  def Setowner(self,Name):
    self._Name=Name


def  main():
    mycar = Car()
    mycar.Setowner("eamon")
    mycar.Getowner()
    janacar=Car
    janacar.Setowner("danya")
    janacar.Getowner()
if __name__ == '__main__': main()