
class Hole :
    def __init__(self,hole_id,seeds_num):
        self.hole_id = hole_id
        self.seeds_num = seeds_num

class Kalah:
    def __init__(self,holes,seeds):
        self.holes_number = holes*2+2 #(i,)for i in range(1,holes)]
        self.seeds_number = seeds * self.holes_number
        self.holes = [Hole(i,seeds) for i in range(1,self.holes_number+1)]


    def play(self,hole):
        pass


# k = Kalah(6,4)
# # print(k.holes)
#
# for i in range(len(k.holes)):
#     print(k.holes[i].hole_id,k.holes[i].seeds_num)