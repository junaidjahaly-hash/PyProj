class Door():
    def __init__(self,is_open):
        self.is_open=is_open
    def open_door(self):
     if self.is_open == "opened":
      print("door cannot be opened")
     else:
      print("door can be opened")
    def close_door(self):
     if self.is_open == "opened":
      print("door can be closed")
     else:
       print("door cannot be closed")
       myfrontdoor=Door()
       myfrontdoor.open_door()
       myfrontdoor.close_door()

class BlockedDoor(Door):
 def __init__(self, is_open):
   super().__init__(is_open)
   self.open_door="closed"
   self.close_door="opened"

