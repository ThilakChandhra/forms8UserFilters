from django import template

register=template.Library()

def swap(value):
    return value.swapcase()

def remove(value,arg):
    return value.replace(arg,'')

def counting(value,arg):
    count=0
    for i in range(len(value)):
        if value[i:i+len(arg):]==arg:
            count+=1
    return count
    
register.filter('counting',counting)
register.filter('swapping',swap)
register.filter('remove',remove)