############################################################################
#                  This file needed to manage user data                    #
#      this file maybe create, delete, check and get all data users        #
# this file work 4 types users data (main admin, admin, manager and users) #
############################################################################

############################################################################
#                           DOCUMENTATION                                  #
# 4 types user data (main admin, admin, manager and users) exits           #
# To work with these data needed you must write:                           #
#                                                                          #
# 1 UserData.main_admin_db() to work with main admin users data            #
# 2 Userdata.admin_db() to work with admin users data                      #
# 3 Userdata.manager_db() to work with manager users data                  #
# 4 Userdata.user_db() to work with users data                             #
#                                                                          #
# and need you save data in a variable to you work with users data         #
# e.g:                                                                     #
# main_admin_data = Userdata.admin_db()                                    #
# To you add users, you need write:                                        #
# main_admin_data.add_user(user_id, user_name, user_full_name)             #
#                                                                          #
# To you delete users, you need write:                                     #
# main_admin_data.delete_user(user_id)                                     #
#                                                                          #
# To you check users, you need write:                                      #
# main_admin_data.check_user(user_id)                                      #
#                                                                          #
# To you get all users, you need write:                                    #
# main_admin_data.get_all_user(user_id)                                    #
#                                                                          #
# To you get all privilege users, you need write:                          #
# UserData.get_all_privilege_user(user_id)                                 #
# And you get list                                                         #
# e.g [main_admin, admin, manager]                                         #
############################################################################

from sqlalchemy import create_engine
from config import user_data_url


class UserData:
    def __init__(self, view_user: str):
        # connect data
        self.engine = create_engine(user_data_url)

        # create table
        self.engine.execute("""CREATE TABLE IF NOT EXISTS {view_user}
        (
        user_id INTEGER UNIQUE NOT NULL,
        user_name VARCHAR(20) NOT NULL,
        user_full_name VARCHAR(50) NOT NULL
        )""".format(view_user=view_user))

        # save view user
        self.view_user = view_user

    # return class main admin to work with these data
    @staticmethod
    def main_admin_db():
        return UserData("main_admin")

    # return class admin to work with these data
    @staticmethod
    def admin_db():
        return UserData("admin")

    # return class manager to work with these data
    @staticmethod
    def manager_db():
        return UserData("manager")

    # return class users to work with these data
    @staticmethod
    def user_db():
        return UserData("users")

    # create all table to work with these data
    @staticmethod
    def create_db() -> None:
        UserData.main_admin_db()  # create main admin table
        UserData.admin_db()  # create admin table
        UserData.manager_db()  # create manager table
        UserData.user_db()  # create user table

    # add user in data
    def add_user(self, user_id: int, user_name: str, full_name: str) -> None:
        # prepare a request
        self.engine.execute("""INSERT INTO {view_user}(user_id, user_name, user_full_name) 
                            VALUES({user_id}, 
                                   '{user_name}', 
                                   '{full_name}')""".format(
                                                          view_user=self.view_user,
                                                          user_id=user_id,
                                                          user_name=user_name,
                                                          full_name=full_name))

    # check user in data
    def check_user(self, user_id: int) -> bool:
        # get user where user_id in data = user_id
        check_admin_id = self.engine.execute("""SELECT user_id FROM {view_user}
                                             WHERE user_id = {user_id}""".format(
                                                                                  view_user=self.view_user,
                                                                                  user_id=user_id)).fetchone()

        if check_admin_id is None:
            return False
        return True

    # delete user in data
    def delete_user(self, user_id: int) -> None:
        # prepare a request
        self.engine.execute("""DELETE FROM {view_user} 
                            WHERE user_id = {user_id}""".format(
                                                                 view_user=self.view_user,
                                                                 user_id=user_id))

    # get all user in data
    def get_all_user(self) -> list:
        # get all users data
        all_admin = self.engine.execute("""SELECT * FROM {view_user}""".format(view_user=self.view_user))
        all_admin_list = [admin for admin in all_admin]  # write in list
        return all_admin_list  # return list

    # get all privilege user
    @staticmethod
    def get_all_privilege_user(user_id: int) -> list:
        return [  # return list privilege
            UserData.main_admin_db().check_user(user_id),  # check user_id in main_admin
            UserData.admin_db().check_user(user_id),  # check user_id in admin
            UserData.manager_db().check_user(user_id)  # check user_id in manager
        ]

    def get_all_information_user(self, view, search):
        return self.engine.execute("""SELECT * FROM {view_user}
                                      WHERE {view_search} = {search} """.format(view_user=self.view_user,
                                                                                view_search=view,
                                                                                search=search)).fetchone()
