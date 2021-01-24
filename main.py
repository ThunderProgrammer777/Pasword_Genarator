import matplotlib.pyplot as plt
con = [6555,5314]
col = ['pink ','red']
hou = ['Male', 'Female']
plt.title("Gender")
plt.pie(con,colors=col,labels=hou,autopct="%1.1f%%")
plt.show()