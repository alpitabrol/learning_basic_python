#
# Example file for working with classes
#


class myclass():
  def method1(self):
    print("myclass method1")

  def method2(self,somestring):
    print("myclass method2 "+somestring)

class anotherclass(myclass):
  def method1(self):
    myclass.method1(self)
    print("another class method1")

  def method2(self,somestring):
    print("another class method2 ")

def main():
  c= myclass()
  c.method1()
  c.method2("this is a string") 

  c2= anotherclass()
  c2.method1()
  c2.method2("this is a string") 

if __name__ == "__main__":
  main()
