
#
# class hole :
#     def __init__(self,hole_id,seeds_num):
#         self.hole_id = hole_id
#         self.seeds_num = seeds_num

class Kalah:
    def __init__(self,holes,seeds):
        self.holes = holes*2+2 #(i,)for i in range(1,holes)]
        self.seeds = seeds*self.holes

    def play(self,hole):
        pass