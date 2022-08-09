import random

data_stream = ""
stream_length = 10_000_000

r = 3.56994567187094490184220051513864989367638369115
x0 = 0.477
x = x0
transient = 100_000

def logistic_map(x):
  return r*x*(1-x)

for i in range(transient):
  x = logistic_map(x)

for i in range(stream_length):
  x = logistic_map(x)
  if 0 <= x < 0.5:
    data_stream += "0"
  elif 0.5 <= x <= 1:
    data_stream += "1"

with open(f"log_data_r{3569945671}.txt", "w") as file:
  file.write(data_stream)
