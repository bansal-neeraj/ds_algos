from decouple import config

my_dict = {
    'a':'abc',
    'b':'def'
}

x,*_,y = config(**my_dict)
