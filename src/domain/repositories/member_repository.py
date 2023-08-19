class MemberRepository:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def find_by_id(self, id):
        return next((member for member in self.members if member.id == id), None)