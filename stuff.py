class IntuitiveListe(list):
    def __sub__(self, other):
        new_list = IntuitiveListe(self)
        if isinstance(other, list):
            for i in other:
                new_list.remove(i)
        else:
            new_list.remove(other)
        return new_list

    def __add__(self, other):
        new_list = IntuitiveListe(self)
        if isinstance(other, list):
            for i in other:
                new_list.append(i)
        else:
            new_list.append(other)
        return new_list


l = IntuitiveListe([0, 1, 2, 3, 4, 5])
print(l - [0,3,5])

print(l + [12,345,56])