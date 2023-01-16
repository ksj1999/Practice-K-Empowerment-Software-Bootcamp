# 연습문제 5-4
salutation = 'mr'
name = 'kwon'
product = 'gun'
verbed = 'exploded'
room = 'chamber'
animals = 'birds'
amount = 'quantity'
percent = '30'
spokesman  = 'joe'
job_title = 'CEO'



letter = '\f\fDear {0} {1},\n\n\f\fThank you for your letter. ' \
         'We are sorry that our {2} {3} in your {4}. ' \
         'Please note that it should never be used in a {4}, ' \
         'especially near any {5}\n\n\f\fSend us your receipt and {6} for shipping and handling. ' \
         'We will send you another {2} that, in our tests, is {7}% less likely to have {3}\n\n\f\f' \
         'Thank you for your support.' \
         '\n\f\fSincerly,\n\f\f{8}\n\f\f{9}'.format(salutation, name, product, verbed, room, animals, amount, percent, spokesman, job_title)

print(letter)


# letter =         Dear {salutation} {name},
#
#         Thank you for your letter. We are sorry that our {product} {verbed} in your
# {room}. Please note that it should never be used in a {room}, especially near any {animals}
#
#         Send us your receipt and {amount} for shipping and handling.
# We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}
#
#         Thank you for your support.
#         Sincerly,
#         {spokesman}
#         {job_title}
