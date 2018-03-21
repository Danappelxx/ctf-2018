import json

class DB(object):
    #initialize with a database filename
    def __init__(self, fname = "db.json"):
        self.fname = fname
        self.js_obj = json.load(open(self.fname, 'r'))

    def create_user(self, username, passhash, admin_status = False): #or "admin"
        #create a user if it doesnt exist
        if username in self.js_obj['users']:
            return False

        self.js_obj['users'][username] = {
            'password_hash': passhash,
            'admin_status': "admin" if admin_status is True else "noadmin"
        }

        #write to the database
        f = open(self.fname, 'w')
        f.write( json.dumps(self.js_obj ) )
        f.close()
        return True

    def is_admin(self, username):
        #check admin status
        if username not in self.js_obj['users']:
            return False

        return True if self.js_obj['users'][username]['admin_status'] == "admin" else False

    def get_all_users(self):
        #return all users
        return [str(x) for x in self.js_obj['users'].keys()]

    def get_user(self, username):
        #return user
        try:
            return self.js_obj['users'][username]
        except KeyError:
            return None
