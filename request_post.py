import requests
from urllib.parse import urlencode

class UserIDs(object):
    
    def __init__(self):
        
        self.id = None
        self.name = "John Doe"
        self.facebookId = None
        self.facebookAccessToken = None
        self.zip = "94087"
        self.phone = None
        self.contentRating = None
        self.email = None
        self.location = "Sunnyvale, CA 94087"
        self.gender = "male"
        self.ageMin = 21
        self.ageMax = None
        self.imgLocation = None
        self.createdAt = "2018-03-29T22:54:18.771Z"
        self.updatedAt = "2018-3-29T22:54:18.771Z"
        self.accountId = 13
        self.attributes = []
        self.linkedAccounts = []

    def user_change(self):
        
        user_dict = {}
        user_dict['id'] = self.id
        user_dict['name'] = self.name
        user_dict['facebookId'] = self.facebookId
        user_dict['facebookAccessToken'] = self.facebookAccessToken
        user_dict['zip'] = self.zip
        user_dict['phone'] = self.phone
        user_dict['contentRating'] = self.contentRating
        user_dict['email'] = self.email
        user_dict['location'] = self.location
        user_dict['gender'] = self.gender
        user_dict['ageMin'] = self.ageMin
        user_dict['ageMax'] = self.ageMax
        user_dict['imgLocation'] = self.imgLocation
        user_dict['createdAt'] = self.createdAt
        user_dict['updatedAt'] = self.updatedAt
        user_dict['accountId'] = self.accountId
        user_dict['attributes'] = self.attributes
        user_dict['linkedAccounts'] = self.linkedAccounts

        return user_dict



def user_change_alert(userID, monitorID, server_url):

    # add code for devie ID
    userID_change_msg = {
                         "type":"device", 
                         "payload":{"activeProfileId":userID}
                        } 
    print("posting Request")
    print(userID)
    #r = requests.post(url, urlencode(post_fields).encode())
    r = requests.post(url, json = userID_change_msg)
    print("Request posted")
    print(r.status_code)
    print(r.json())
    
    return True



def main():
     
    userID = 25
    #server_url = "http://ce.openznet.com/?deviceID=35&isPC=true"
    #azita 32, so 25
    server_url = "http://products.openznet.com/api/announcer/v1.0/announce/rob" 
    print("changing user to {}".format(userID))
    print(server_url)
    userID_change_msg = {
                         "type":"device", 
                         "payload":{"activeProfileId":userID}
                        }
    print(userID_change_msg)
    print("Posting Request")
    r = requests.post(server_url, json = userID_change_msg)
    print("Request posted")
    print(r.status_code)
    print(r.json())
    
                      

if __name__ == "__main__":
    main()
    









