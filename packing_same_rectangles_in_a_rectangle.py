import math


Length_of_larger_rectangle = 512
Length_of_smaller_rectangle = 700
Breadth_of_larger_rectangle = 3
Breadth_of_smaller_rectangle = 1000


def pack(Length_of_larger_rectangle, Breadth_of_larger_rectangle, Length_of_smaller_rectangle, Breadth_of_smaller_rectangle):
    if Length_of_larger_rectangle < Breadth_of_larger_rectangle:
        temp = Breadth_of_larger_rectangle
        Breadth_of_larger_rectangle = Length_of_larger_rectangle
        Length_of_larger_rectangle = temp
    if (Length_of_smaller_rectangle < Breadth_of_smaller_rectangle):
        temp2 = Breadth_of_smaller_rectangle
        Breadth_of_smaller_rectangle = Length_of_smaller_rectangle
        Length_of_smaller_rectangle = temp2

    Case1 = math.floor(Length_of_larger_rectangle/Length_of_smaller_rectangle) * \
                       math.floor(Breadth_of_larger_rectangle /
                                  Breadth_of_smaller_rectangle)
    left_length1 = Length_of_larger_rectangle-Length_of_smaller_rectangle * \
        math.floor(Length_of_larger_rectangle/Length_of_smaller_rectangle)
    if (left_length1 > Breadth_of_smaller_rectangle):
        Case1a = math.floor(Breadth_of_smaller_rectangle / left_length1) * \
            math.floor(left_length1/Breadth_of_smaller_rectangle)
        Case1 = Case1+Case1a


    Case2 = math.floor(Breadth_of_larger_rectangle / Breadth_of_smaller_rectangle) * \
                   math.floor(Length_of_larger_rectangle / Length_of_smaller_rectangle)

    Case3 = math.floor(Length_of_larger_rectangle/Breadth_of_smaller_rectangle) * \
                   math.floor(Breadth_of_larger_rectangle /
                              Length_of_smaller_rectangle)
    left_breadth2 = Breadth_of_larger_rectangle-Length_of_smaller_rectangle * \
        math.floor(Breadth_of_larger_rectangle/Length_of_smaller_rectangle)
    if(left_breadth2 > Breadth_of_smaller_rectangle):
        Case3 = Case3+math.floor(Length_of_larger_rectangle/Length_of_smaller_rectangle) * \
            math.floor(left_breadth2/Breadth_of_smaller_rectangle)
    Case4 = math.floor(Breadth_of_larger_rectangle / Length_of_smaller_rectangle) * \
    math.floor(Length_of_larger_rectangle/Breadth_of_smaller_rectangle)

    No_of_cfcs = max(Case1, Case2, Case3,Case4)
    return No_of_cfcs

a = pack(Length_of_larger_rectangle, Breadth_of_larger_rectangle, Length_of_smaller_rectangle,Breadth_of_smaller_rectangle )
print(a)
