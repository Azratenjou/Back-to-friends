import time

lyrics = [
        "I was scared to take a breath, didn't want you to move your head",
        "How can we go back to being friends",
       "When we just shared a bed? (Yeah)",
 ]
 
 def typing_animation(text, delay=0.08):
         for char in text:
                 print(char, end=' ', flush=True)
                 time,sleep(delay)
         print()
         
    def show_lyrics(lyrics):
            print("")
            
if _name_ == "_main_":
    show_lyric(lyrics)