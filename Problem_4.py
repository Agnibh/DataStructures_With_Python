class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    sub_user=group.get_users()              # Get all the users within the group

    if user in sub_user:                    # If user is within the group, return True
        return True

    sub_group=group.get_groups()            # Get all the sub groups within the group

    if len(sub_group)==0:                   # Base case if there are no sub groups within group
        return False

    for item in sub_group:                  # Recursively search within sub groups for the user
        return is_user_in_group(user,item)
    return False
