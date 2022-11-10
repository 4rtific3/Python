import turtle as t
import pandas as pd

FONT = ("Arial", 9, "normal")

data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []

score = 0

state_name = t.Turtle()
state_name.pu()
state_name.hideturtle()
screen = t.Screen()
screen.title("US States Games")
image = "blank_states_img.gif"

screen.addshape(image)
t.shape(image)

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state name?").title()
    if answer_state == "Exit":
        missed_states = [state for state in states_list if state not in guessed_states]
        
        pd.DataFrame(missed_states).to_csv("states_to_learn.csv")
        break
    
    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        score += 1
        state_row = data[data.state == answer_state]
        state_name.goto(int(state_row.x), int(state_row.y))
        state_name.write(answer_state, align="center", font=FONT)



screen.exitonclick()