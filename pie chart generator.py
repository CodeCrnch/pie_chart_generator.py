import matplotlib.pyplot as plt

Partition = "A","B","C","D"
sizes = [5, 3, 9, 10]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=Partition, autopct="%1.1f%%", startangle=90)         
ax1.axis("equal")
plt.show()
