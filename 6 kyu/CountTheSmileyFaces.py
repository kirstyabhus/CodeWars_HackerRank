#https://www.codewars.com/kata/583203e6eb35d7980400002a/python

# valid faces are either a length of 2 (no nose) or 3 (with nose)
def count_smileys(arr):

    # list of all valid characters
    validChars = [":", ";", "-", "~", ")", "D"]
    # keep count of valid faces
    validCount = 0
    # length of the list
    length = len(arr)

    # iterate through all faces in the list
    for face in arr:
        # find the lenght of the current face
        sizeFace = len(face)
        # if the face has a length of 2
        if sizeFace == 2:
            # if the first character of face is ":" or ";"
            if face[0] in validChars[0:2]:
                # if the second character of face is ")" or "D"
                if face[1] in validChars[4:6]:
                    # increase valid face count
                    validCount += 1

        # if the face has a length of 3
        elif sizeFace == 3:
            # if the first character of face is ":" or ";"
            if face[0] in validChars[0:2]:
                # if the second character of face is "-" or "~"
                if face[1] in validChars[2:4]:
                    # if the third character of face is ")" or "D"
                    if face[2] in validChars[4:6]:
                        validCount += 1
                        # increase valid face count

    return validCount