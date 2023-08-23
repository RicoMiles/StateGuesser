from turtle import Turtle, Screen
import pandas as pd

window = Screen()
window.bgpic("blank_states_img.gif")
window.setup(725, 491)

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_state = []

t = Turtle()
t.penup()
t.speed(0)
t.hideturtle()
answer = ""
count = 0
while count < 50:
    answer = window.textinput(f"{count}/50", "Enter State")
    if answer is None:
        break
    answer = answer.title()
    if answer == "Exit":
        break
    for s in states:
        temp = data[data.state == s]
        if s == answer:
            guessed_state.append(answer)
            t.setx(int(temp.x.iloc[0]))
            t.sety(int(temp.y.iloc[0]))
            t.write(answer)
            count += 1
            break

missed_states = []
for s in states:
    flag = 0
    for g in guessed_state:
        if s == g:
            flag = 1
            break
    if flag == 0:
        missed_states.append(s)

df = pd.DataFrame({"Missed States": missed_states})
df.to_csv("./states_to_learn.csv")


window.exitonclick()

