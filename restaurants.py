#CS175L
#Gianna Rao
#restaurant

another_search = "yes"
while another_search == "yes":
   #variables
   vegetarian = True
   vegan = True
   gluten_free = True

   #responses
   response_vegetarian = input("Is anyone in your party a vegetarian? ")
   if response_vegetarian == "no" or "No":
      vegetarian = False
   
   response_vegan = input("Is anyone in your party a vegan? ")
   if response_vegan == "no" or "No":
       vegan = False

   response_gluten_free = input("Is anyone in your party gluten-free? ")
   if response_gluten_free == "no" or "No":
       gluten_free = False

   #print
   print ("Here are your restaurant choices: ")

   print ("Corner Cafe \n Chef's Kitchen")

   if vegetarian == False and vegan == False and gluten_free == False:
       print ("Joe's Gourmet Burgers")

   if vegan == False and gluten_free == False:
      print ("Mama's Fine Italian")

   if vegan == False:
       print ("Main Street Pizza")

   another_search = input("Do you want to do another search? ")























