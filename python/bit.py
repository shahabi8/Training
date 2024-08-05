# Two's Complement Representation

#     Positive Numbers: Positive integers are represented in binary as usual. For example,
#     the binary representation of 6 is 0110.

#     Negative Numbers: Negative integers are represented using two's complement.
#     To find the two's complement of a number:
#     Take the binary representation of the positive number.
#     Invert all the bits (change 0 to 1 and 1 to 0).
#     Add 1 to the inverted number.

# Let's apply this to the number 6:

#     Binary representation of 6: 0110.
#     Invert the bits: 1001.
#     Add 1: 1001 + 1 = 1010.

# Distinguishing Positive and Negative Numbers

#   In a fixed-width binary system (e.g., an 8-bit or 16-bit system), 
#   you can distinguish between positive and negative numbers by looking 
#   at the most significant bit (the leftmost bit):

#     Positive numbers have a most significant bit of 0.
#     Negative numbers have a most significant bit of 1.

# For example, in an 8-bit system:

#     00000110 represents 6.
#     11111010 represents -6.

index = 6
print(bin(index))    # Output: 0b110

# Compute -index
neg_index = -index
print(bin(neg_index))  # Output: -0b110

# The operation index & -index isolates the least significant set bit.
# Compute index & -index
result = index & neg_index
print(bin(result))   # Output: 0b10

# 0110 & (-0110 --> 1010) = 10 --> 2 so this gives us the least significant bit
# 110 & (110 - 1 --> 101) = 100 --> 4 --> this unset the least significant bit
result = index & (index - 1)