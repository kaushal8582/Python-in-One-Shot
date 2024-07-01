import sqlite3

conn = sqlite3.connect("youtube.db")
cursor = conn.cursor()
cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS videos(
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 time TEXT NOT NULL
               )
''')


def list_videos():
  
 cursor.execute("SELECT * FROM videos")
 for row in cursor.fetchall():
  print(f"{row[0]}: {row[1]} - Video Duration is : {row[2]}")

def add_video(name,time):
  cursor.execute("INSERT INTO videos (name ,time) VALUES (?, ?)",(name,time))
  conn.commit()

def update_video(id,name,time):
  cursor.execute("UPDATE videos SET name = ?, time =? WHERE id =?",(name,time,id))
  conn.commit()

def delete_video(id):
  cursor.execute("DELETE FROM videos WHERE id =?",(id,))
  conn.commit()


def main():
  while True:
    print("\n Youtube Manager | With Database ")
    print("1. List All Youtube Video ")
    print("2. Add a Youtube Video")
    print("3. Update a youtube video details ")
    print("4. Delete a youtube video ")
    print("5. Exit the app")
    choice = input("Enter your choice : ")
    
    if choice =="1":
      print("\n\n\n")
      print("*" * 70)
      list_videos()
    elif choice=="2":
      name =input("Enter the video name : ")
      time = input("Enter the video time : ")
      add_video(name,time)
    elif choice=="3":
      id = input("Enter video ID to update : ")
      name =input("Enter the video name : ")
      time = input("Enter the video time : ")
      update_video(id,name,time)
    elif choice=="4":
      id = input("Enter video ID to delete : ")
      delete_video(id)
    elif choice=="5":
      break
    else:
      print("Enter a valid choice ")
  conn.close()  
      
  


if __name__ == "__main__":
  main();