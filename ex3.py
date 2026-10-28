book_name=input("enter the book name:")
quantity=int(input("enter the quantity:"))
one_book=300
total=one_book*quantity
gst=7
gst_amount=total*gst/100
total_amount=total+gst_amount
print(f"The total amount for {quantity} {book_name} is: {total_amount}including GST")