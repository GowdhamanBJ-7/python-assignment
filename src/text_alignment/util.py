thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



# text = "Hello"
# aligned_text = text.ljust(20,'-') # Pads with spaces to make the total width 20
# print(f"'{aligned_text}'")
#
# text = "Hello"
# aligned_text = text.center(20)  # Pads with spaces to center the text
# print(f"'{aligned_text}'")
#
#
# text = "Hello"
# print(f"'{text:<20}'")  # Left-aligned
# print(f"'{text:>20}'")  # Right-aligned
# print(f"'{text:^20}'")  # Center-aligned
