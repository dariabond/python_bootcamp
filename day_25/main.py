import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")
image = "/Users/dariabondarchuk/programming projects/python/bootcamp/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("/Users/dariabondarchuk/programming projects/python/bootcamp/day-25-us-states-game-start/50_states.csv")
states_data = data["state"]

def get_results_csv(learned_list, to_learn_list):
    results_dict = {
        "Learned": learned_list,
        "To Learn": to_learn_list
    }
    print(to_learn_list)
    new_data = pandas.DataFrame(to_learn_list)
    new_data.to_csv('states_to_learn.csv')
    

answers = []
while len(answers) < 50:
    answer_state = screen.textinput(title = f"{len(answers)}/50 states correct", prompt = "What's another states name").title()
    if answer_state == 'Exit':
        get_results_csv(answers, [x for x in data.state.values if x not in answers])
        break

    if answer_state in data.state.values:
        print("Hooray!")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        answers.append(answer_state)
    else:
        print("Wrong")


turtle.mainloop()
