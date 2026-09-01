class India:
    def capital(self):
        print("The capital of India is New Delhi ! ")

    def currency(self):
        print("The currency of India is the Indian Rupee!")
class USA:
    def capital(self):
        print("The capital of US is Washington D.C!")

    def currency(self):
        print("The currency for USA is the US Dollar !")



obj_ind=India()
obj_usa=USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.currency()