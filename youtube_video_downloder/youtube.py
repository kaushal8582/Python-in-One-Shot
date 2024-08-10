from pytube import YouTube

link  = input("Enter the video link ")

y_tube = YouTube(link)

print("Title : ",y_tube.title)

stream = y_tube.streams.filter(progressive=True)

video = list(enumerate(stream))

for i in video:
  print(i)

print("""""""""""""""""""""""""")

index = int(input("Give the index of the desire : "))

stream[index].download()

print("Success")


