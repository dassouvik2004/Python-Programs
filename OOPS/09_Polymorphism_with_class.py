class India:
    def Capital(self):
        print("New Delhi is the capital of India.")
    def Language(self):
        print("Hindi is the most widely spoken language in India.")
    def type(self):
        print("India is the developing country.")
class USA:
    def Capital(self):
        print("Washington, D.C is the capital of USA.")
    def Language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is the developed country.")

obj_IND = India()
obj_USA = USA()

for country in (obj_IND,obj_USA):
    country.Capital()
    country.Language()
    country.type()