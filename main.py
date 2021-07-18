from datetime import date,timedelta
current_date = date.today().isoformat()

users=[]



class subscriptions:
    def __init__(self):
        self.start_date= current_date

    def subscription_type(self):
      print("Do you want a monthly or annual subscription? (M/A): ")
      self.sub_type=str(input())
     
    def subscription_enddate(self):

      if self.sub_type=='M':
  
        days_after = (date.today()+timedelta(days=30)).isoformat()
        self.end_date= days_after
        print("Your subscription ends on ",days_after)
    
      elif(self.sub_type=='A'):
        days_after = (date.today()+timedelta(days=365)).isoformat()
        self.end_date = days_after
        print("Your subscription ends on ",days_after)
        
      else:
        print('Error! Invalid Format!')

    def add_sub(self):
      print("Enter the service you want to add: ")
      self.sub_name=str(input())
      
      
    def WriteToFile(self, uName):
      
      import json
      f = open('sample.json')
        
      data = json.load(f)

      users_json = []

      dictionary = {
                        "sub_name" : self.sub_name,
                        "sub_type" : self.sub_type,
                        "start_date" : self.start_date,
                        "end_date" : self.end_date
                    }


      flag=False
      for i in data["users"]:
          users_json.append(i)
        

      for user in users_json:
          if (user["username"] == uName):
              user["subscriptions"].append(dictionary)
              flag=True
              break
      if(flag==False):
        subs_list = []
        subs_list.append(dictionary)
        users_dict={'username':uName,'subscriptions':subs_list}
        users_json.append(users_dict)

      newjson = {

        "users": users_json
        }
      json_object = json.dumps(newjson)
              
          
      with open("sample.json", "w") as outfile:
          outfile.write(json_object)


    def ReadFromFile(self,uName):
      import json
      f = open('sample.json')
      users_json = []
      data = json.load(f)

      for i in data["users"]:
        users_json.append(i)
              

      for user in users_json:
        if (user["username"] == uName):
          json_subs=user["subscriptions"]
          print(json_subs)



    def calc_remaining_days(self):    
      
      end_date_string = (self.end_date.split('-'))
      start_date_string = (self.start_date.split('-'))

      endDate=date(int(end_date_string[0]), int(end_date_string[1]), int(end_date_string[2]))
      startDate=date(int(start_date_string[0]), int(start_date_string[1]), int(start_date_string[2]))


      delta = endDate - startDate

      self.remaining_days = delta.days
      print("You have ",self.remaining_days," days remaining in your subscription")
      
    
    def collective_fns(self, uName):
      self.ReadFromFile(uName)
      self.add_sub()
      self.subscription_type()
      self.subscription_enddate()
      self.calc_remaining_days()
      self.WriteToFile(uName)


class Users:
  Subscriptions_list = []
  def login(self):
      name=str(input("Enter Username: "))  
      self.username=name
      if(self.username not in users):
        users.append(self.username)
      else:
        pass
  
  def AddSub(self):
        newsub = subscriptions()
        newsub.collective_fns(self.username)
        self.Subscriptions_list.append(newsub)


  
user1 = Users()
user1.login()
user1.AddSub()

