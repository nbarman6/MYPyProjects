import plotly.express as px
import random

def get_face_counts(num_rolls):
    rolls = []
    for i in range(num_rolls):
        rolls.append(random.randint(1, 6))
        
    face_counts = {}
    for i in range(1, 7):
        face_counts[i] = rolls.count(i)
    return face_counts

face_counts_100 = get_face_counts(100)
face_counts_50 = get_face_counts(50)

# Creating the list x_labels
x_labels = []
for x in face_counts_100.keys():
    x_labels.append(str(x))
    
# Create a bar chart of the results using plotly
fig1 = px.bar(list(face_counts_100.items())), x = x_labels, y = face_counts_50.values(),
fig2 = px.bar(list(face_counts_50.items())), x = x_labels, y = face_counts_50.values(),

fig1.add_trace(fig2.data[0])
fig1.update_layout(width=800, height=500, xaxis_title="Face", yaxis_title="Count",xaxis_tickangle=-45, title="Results of rolling one die 100 times and 50 times")

fig1.show()