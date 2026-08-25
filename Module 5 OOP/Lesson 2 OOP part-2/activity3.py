#TWO-ELEMENT SUM PROBLEM
class Pairsum:
    def __init__(self, numbers_list):
        self.numbers_list=numbers_list
        self.target=int(input("Enter the target sum: "))

    def find_elements(self):
        #empty dictionary
        lookup={}

        #loop through the numbers_list
        for index, number in enumerate(self.numbers_list):
            if self.target- number in lookup:
                return (lookup [self.target-number],index)

            lookup[number]= index

    def answer(self):
        print(f"The 2 numbers thet add up to {self.target} are")
        index1, index2,=self.find_elements()
        print(self.numbers_list[index1])
        print(self.numbers_list[index2])
#_____________________________________________________

numbers_list=[3, 5, 1, 7, 10, 2]

        
two_sum=Pairsum(numbers_list)
print("The 2 elements theat ad up to")

two_sum.answer()