#!/usr/bin/python3.4

def quicksort(liste):
    
    if liste == []:
        return []

    pivot = liste.pop(0)    
    bigger = list(filter(lambda x: x > pivot, liste))
    smaller = list(filter(lambda x: x <= pivot, liste))

    return (quicksort(smaller) + [pivot] + quicksort(bigger))

