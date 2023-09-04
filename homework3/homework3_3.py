"""
Написати валідатор для пошти.
Користувач вводить пошту, а програма повинна перевірити, що в пошті є символ '@' і '.',
і якщо це так, вивести "YES", інакше "NO"
"""

email = input("Enter your email: ")

# Через класичний if-else:
if "@" in email and "." in email:
    print("YES")
else:
    print("NO")

# Через тернарний оператор:
result = print("YES") if "@" in email and "." in email else print("NO")
