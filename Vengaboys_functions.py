'''
Function to return
AlbumName,
ArtistName &
ReleasedYear
and Boolean value
'''


#This function will return AlbumName
def AlbumName():
    return "The Party Album"

#This function will return ArtistName
def ArtistName():
    return "Vengaboys"

#This function will return Released Year
def ReleasedYear():
    return "1998"

#This function will check which year the Album Released
#and if its not this year(2024) then it will return FALSE
def bool_fun():
    if int(ReleasedYear()) == 2024:
        return "True"
    else:
        return "False"


print("Album Name : " + AlbumName())
print("Artist Name : " + ArtistName())
print("Released Year : " + ReleasedYear())
print("This Album released this year : " + bool_fun())