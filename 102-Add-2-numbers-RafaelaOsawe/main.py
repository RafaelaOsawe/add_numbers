# import the modules required from guizero
from guizero import App, Text, TextBox, PushButton

def add():
  num1 = enter_num1.value
  num2 = enter_num2.value
  answer = int(num1) + int(num2)
  display_answer.value = answer

def multiply():
  num1 = enter_num1.value
  num2 = enter_num2.value
  answer = int(num1) * int(num2)
  display_answer.value = answer

def divide():
  num1 = enter_num1.value
  num2 = enter_num2.value
  answer = int(num1) / int(num2)
  display_answer.value = answer

def subtract():
  num1 = enter_num1.value
  num2 = enter_num2.value
  answer = int(num1) - int(num2)
  display_answer.value = answer

# create the app with the window title “Add two numbers” 
app = App(title="Add two numbers")
text1 = Text(app, text="Enter a number")
enter_num1 = TextBox(app)
text2 = Text(app, text="Enter another number")
enter_num2 = TextBox(app)
display_answer = Text(app, text="Answer") 
button = PushButton(app, command=add, text="Add")
button = PushButton(app, command=multiply, text="Multiply")
button = PushButton(app, command=divide, text="Divide")
button = PushButton(app, command=subtract, text="Subtract")

# display the app, this should always be last
app.display()


