import pickle


# define class
class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

lists = [123, "中文", [456]]
fn = 'a.pkl'
with open(fn, 'wb+') as f:  # open file with write-mode
    picklestring = pickle.dump(lists, f)  # serialize and save object
