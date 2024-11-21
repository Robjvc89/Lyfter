
class Head:
    def __init__(self):
        self.eyes = "2 eyes"
        self.nose = "1 nose"
        self.mouth = "1 mouth"


class Hand:
    def __init__(self):
        self.fingers = 5


class Arm:
    def __init__(self, hand):
        self.hand = hand
        self.upper_arm = "upper arm"
        self.lower_arm = "lower arm"


class Leg:
    def __init__(self, feet):
        self.feet = feet
        self.thigh = "thigh"
        self.calf = "calf"


class Feet:
    def __init__(self):
        self.toes = 5
        self.heel = "heel"


class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        self.spine = "spine"
        self.chest = "chest"
        self.stomach = "stomach"


class Human:
    def __init__(self):
        
        self.head = Head()
        self.right_hand = Hand()
        self.left_hand = Hand()

        self.right_arm = Arm(self.right_hand)
        self.left_arm = Arm(self.left_hand)

        self.right_foot = Feet()
        self.left_foot = Feet()

        self.right_leg = Leg(self.right_foot)
        self.left_leg = Leg(self.left_foot)

        
        self.torso = Torso(self.head, self.right_arm, self.left_arm, self.right_leg, self.left_leg)


        self.body = self.torso

    def describe(self):
        return {
            "Head": vars(self.head),
            "Right Arm": vars(self.right_arm),
            "Left Arm": vars(self.left_arm),
            "Right Leg": vars(self.right_leg),
            "Left Leg": vars(self.left_leg),
            "Torso": vars(self.torso)
        }


human = Human()


print(human.describe())
