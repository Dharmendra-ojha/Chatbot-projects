from prsaw import RandomStuffV2

# initiate the object
rs = RandomStuffV2() 



while True:
      input_user=input("> ")
      
      response =rs.get_ai_response(input_user)
      print(response)

# close the object once done (recommended)
rs.close()