
# try:
#     # a = 1 / 0
#     # l = []
#     # print(l[1.5])
#     assert False
#     a = 1
# except ZeroDivisionError:
#     print('zero division')
# except (ValueError, TypeError):
#     print("value or type error")
# except AssertionError as e:
#     print("assertion error", e)
# except:
#     pass
# else:
#     print('all good')
# finally:
#     print('done')




# # assert 1 + 1 == 2, "Nobody expects the Spanish inquisition!"


# if not (1 + 1 == 2):
#     raise AssertionError("Nobody expects the Spanish inquisition!")


# print('all good')



class MyException(Exception):
    def __str__(self):
        return "But then I took an arrow in the knee"


print("I used to be an adventurer like you")

raise MyException
