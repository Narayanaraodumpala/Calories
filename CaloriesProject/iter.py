def div(a,b):
    print('div is=',a/b)

def decorot(function):
    def inner(a,b):
        if a<b:
            a=b
            b=a

        return  function(a,b)
    return inner

d=decorot(div)
div(5,10)