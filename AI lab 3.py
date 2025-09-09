class Model_Reflex_Agent:
    def __init__(self, set_temp):
        self.goal_temp = set_temp
        self.prev_action = None

    def read_temp(self, room_temp):
        self.room_temp = room_temp

    def performance(self):
        action = None
        
        if self.room_temp > self.goal_temp:
            action = "Turn ON the AC"
        else:
            action = "Turn OFF the AC"

        if action == self.prev_action:
            action = "NO change (the model will hold the same state)"
        else:
            self.prev_action = action
        return action
    
    def actuator(self):
        choice = self.performance()
        print(self.room_temp, "=>", choice)


rooms = {
    "Living Room": 20,
    "Kitchen": 34,
    "Drawing Room": 22,
    "Study Room": 20,
    "Guest Room": 26
}

agent = Model_Reflex_Agent(21)

for room, temp in rooms.items():
    print(room, end=" :\t")
    agent.read_temp(temp)
    agent.actuator()


