class JNTU:
    def schedule_academic():
        print('scheduling academic')
    def declare_holidays():
        print('summer holidays')
    def results():
        print('go to www.jntuhresults.com')
class SriDevi(JNTU):
    def fees():
        print('3rd year fee is 85k')
sobj=SriDevi
sobj.schedule_academic()
sobj.declare_holidays()
sobj.results()
sobj.fees()