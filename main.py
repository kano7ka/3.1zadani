import matplotlib.pyplot as plt

def line_graph(data):
  x = range(len(data))
  plt.plot(x, data)
  plt.show()