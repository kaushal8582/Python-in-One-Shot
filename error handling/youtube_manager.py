
import json

fileName = 'youtube.txt'

def load_data():
  try:
    with open(fileName,'r') as file:
        read = file.read()
        if not read.strip():
          return []  
    data= json.loads(read)
    # print(type(data))
    return data
    
  except (FileNotFoundError , json.JSONDecodeError ) :
    return []


def save_data_helper(videos):
  with open(fileName,'w') as file:
    json.dump(videos,file)


def list_all_video(videos):
    print("\n\n")
    print("*" * 70)
    for index,video in  enumerate(videos,start=1):
     print(F"{index}. {video['name']}, Duration : {video['time']}")
    print("\n\n")
    print("*" * 70)

def add_video(videos):
   name =  input("Enter Video name : ")
   time =  input("Enter video time : ")
   videos.append({"name":name,"time":time})
   save_data_helper(videos)
 
def update_video(videos):
  list_all_video(videos)
  index = int(input("Enter the video number to update : "))
  if 1<= index <=len(videos):
    name= input("Enter the new video name : ")
    time = input("Enter new video time : ")
    videos[index-1] ={'name':name,'time':time}
    save_data_helper(videos)
  else:
    print("Enter valid index ")

def delete_video(videos):
  list_all_video(videos)
  index =int(input("Enter the video number to be deleted : "))
  if 1<=index <= len(videos):
    del videos[index-1]
    save_data_helper(videos)
  else:
    print("Enter a valid index")

def main():
  videos = load_data()
  while True:
    print("\n Youtube Manager | Choose an option")
    print("1. List All Youtube Video ")
    print("2. Add a Youtube Video")
    print("3. Update a youtube video details ")
    print("4. Delete a youtube video ")
    print("5. Exit the app")
    choice = input("Enter your choice : ")
    
    # print(videos)

    match choice:
        case '1':
          list_all_video(videos)
        case "2":
          add_video(videos)
        case '3':
          update_video(videos)
        case '4':
          delete_video(videos)
        case '5':
          break
        case _:
          print("Invalid choice")
        

if __name__ =="__main__":
  main()
  