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

def func(obj):
    obj.Capital()
    obj.Language()
    obj.type()

obj_IND = India()
obj_USA = USA()

print("INDIA: ")
func(obj_IND)
print("USA: ")
func(obj_USA)