from prsaw import RandomStuffV2
import time
import wikipedia
import webbrowser

rs = RandomStuffV2()


while True:
      input_user=input(">>")
      
      response =rs.get_ai_response(input_user)
      print(response)
      if "bye bye" in input_user:
            break
      if "see you later" in input_user:
            break
      if "bye" in input_user:
            break
      if "exit" in input_user:
            break
      if "time" in input_user:
            time=time.ctime()
            print("time is",time)
      if "website" in input_user:
            inpu=input("Enter website :")
            webbrowser.open(inpu)
      if "search" in input_user:
            inp=input("{what do you want to search ?} :")
            result=wikipedia.search(inp)
            
            for search in result:
                  print(search)
                  print(wikipedia.page(search).summary)
                  
      
      
      
      
            

rs.close()