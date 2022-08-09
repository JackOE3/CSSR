import random

data_stream = ""
stream_length = 10_000

state = "a"

for i in range(stream_length):
  if state == "a":
    data_stream += str(random.randint(0,1))
    state = "b"
  if state == "b":
    s = random.randint(0,1)
    data_stream += str(s)
    if s == 1:
      state = "c"
  if state == "c":
    data_stream += "1"
    state = "b"


with open("EP_data.txt", "w") as file:
  file.write(data_stream)
