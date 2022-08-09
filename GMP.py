import random

data_stream = ""
stream_length = 100_000

for i in range(stream_length):
  if data_stream and data_stream[-1] == "0":
    data_stream += str(1)
  else:
    data_stream += str(random.randint(0,1))

with open("GMP_data.txt", "w") as file:
  file.write(data_stream)
