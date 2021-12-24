from nltk.chat.util import Chat,reflections
pairs=[
    [r'hi',['Hi! I am a chat bot....']],
    [r'who is your boss',['My boss is Venkata Ganesh']],
    [r'are you mad',['Nice joke..']],
    [r'sorry',['Machine cannot have feelings! its ok..']],


    [r'what you can do',['I can help with this options please select 1)wanna order dishes 2)issue with recent order 3)order not yet recieved']],

    
    [r'wanna order dishes',['Thats awesome! please select the restaurent you wanna order from avalable options 1)Barbeque Nation 2)Barkaas Arabic Restaurent 3)Nagarjuna Grand 4)Bismillah 5)Hotel Grand Nagarjuna 6)Dominoz']],
    
    
    [r'barbeque nation',['Thats great choice! Please choose available didhes 1)chicken biryani 2)veg biryani 3)mutton biryani']],
    [r'chicken biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'veg biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'mutton biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],


    
    [r'barkaas arabic restaurent',['Thats great choice! Please choose available didhes 1)chicken biryani 2)veg biryani 3)mutton biryani']],
    [r'chicken biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'veg biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'mutton biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    
    
    [r'nagarjuna grand',['Thats great choice! Please choose available didhes 1)chicken biryani 2)veg biryani 3)mutton biryani']],
    [r'chicken biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'veg biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'mutton biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],

    
    [r'bismillah',['Thats great choice! Please choose available didhes 1)chicken biryani 2)veg biryani 3)mutton biryani']],
    [r'chicken biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'veg biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'mutton biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    
    
    [r'hotel grand nagarjuna',['Thats great choice! Please choose available didhes 1)chicken biryani 2)veg biryani 3)mutton biryani']],
    [r'chicken biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'veg biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'mutton biryani',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],


    [r'dominoz',['Thats great choice! Please choose available didhes 1)chicken pizza 2)veg pizza 3)paneer pizza']],
    [r'chicken pizza',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'veg pizza',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    [r'paneer pizza',['Thats great choice! Please choose available payment options 1)cash on delivery 2)upi 3)net banking 4)debit card 5)credit card']],
    
    
    
    [r'cash on delivery',['Thank you for ordering through our services, your order will be delivered shortly, please be patient and ready with cash, Enjoy the meal']],
    [r'upi',['Thank you for choosing prepaid options, please send your bill amount to 1234567891@ybl and let me know after transaction']],
    [r'net banking',['Thank you for choosing prepaid options, please send your bill amount to account no 123456789 with IFSC UBIN000012 and let me know after payment done']],
    [r'debit card',['Thank you for choosing prepaid options, please send your bill amount to account no 123456789 with IFSC UBIN000012 and let me know after payment done']],
    [r'credit card',['Thank you for choosing prepaid options, please send your bill amount to account no 123456789 with IFSC UBIN000012 and let me know after payment done']],




    [r'issue with recent order',['Sorry for inconvenience happened, please select what happened 1)recieved incorrect order 2)order not satisfactory 3)missing items in order']],
    [r'recieved incorrect order',['Sorry for inconvenience happened, We will do our best to neverl happen this again, Thank you for using our services']],
    [r'order not satisfactory',['Sorry for inconvenience happened, I will share your inconvenience with the restaurent and this never happen again, Thank you for using our services']],
    [r'missing items in order',['Sorry for inconvenience happened, I am adding a coupon code in your cart, use that when ordering again at checkout page, Thank you for using our services']],




    [r'order not yet recieved',['Sorry for inconvenience happened, I will check and instruct to deliver as soon as possible, Thank you for being patient']],


    [r'payment done',['Thats great! recieved, your order will be delivered shortly, please be patient, Enjoy the meal']],
    [r'thank you',['I am happy to help you! see you again, have a great day....']],


    
]

chat=Chat(pairs,reflections)
chat.converse()

def quit1():
    print("Hi, I am chatbot")

if __name__=="__main__":
    quit1()