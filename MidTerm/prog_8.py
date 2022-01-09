from pandas import DataFrame
from string import ascii_uppercase
# import string.ascii_uppercase

def main():
    # local variable
    upper_list = list(ascii_uppercase)

    # section 1 
    num_row     = get_num_row()
    num_seats   = get_num_seats()
    seats       = get_seats_list(num_row, num_seats)
    show_table(seats, num_seats, upper_list)

    # section 2
    seats_flatten = sum(seats, [])
    while(bool(seats_flatten.count(AVAIL))):
        req_row, req_col = get_res(num_row, num_seats, upper_list)
        if req_row == None or req_col == None:
            continue
        reserve(seats, req_row, req_col)
        seats_flatten = sum(seats, [])
    print("The reservation if FULL for this flight.")


def get_num_row():
    while(True):
        num_row = input("Enter the number of rows: ")
        if num_row.isdigit() == False or num_row == "":
            print("The number of rows should be an integer")
        elif int(num_row) < 1:
            print("The number of rows should be greater than 0")
        else:
            return int(num_row) 

def get_num_seats():
    while(True):
        output = 0
        num_seats = input("Enter the number of seats per row: ")
        if num_seats.isdigit() == False or num_seats == "":
            print("The number of seats per row should be an integer")
        elif int(num_seats) < 1 or int(num_seats) > 26:
            # otherwise you can't show the table since English alphabet only has 26 characters
            print("The number of seats per row should be greater than 0 or less than 26")
        else:
            return int(num_seats)

def get_seats_list(num_row, num_seats):
    output = []
    for row in range(num_row):
        output.append([AVAIL]*num_seats)
    return output
    # this is problematic, you can go search why does it happen. It helps
    # return [[AVAIL]*num_seats]*num_row 

def show_table(seats, num_seats, upper_list):
    print(f"\n{DataFrame(seats, index=list(range(1,len(seats)+1)), columns=upper_list[:num_seats])}\n")

def get_res(num_row, num_seats, upper_list):
    # I change the used format(like what I did in get_num_row & get_num_seats) here to follow the instruction
    req_row  = None
    req_col  = None
    error_message = ""
    while(True):
        # get row number
        input_row = input(f"Enter a row number (1 to {num_row}): ")
        if input_row.isdigit() == False or input_row=="":
            error_message += "Row number should be an integer"
        elif int(input_row) < 1 or int(input_row) > num_row:
            error_message += f"Row number should be within the range(1 to {num_row})"
        else:
            req_row = int(input_row)-1
        
        # get seat letter
        input_seat = input(f"Enter a seat letter (A to {upper_list[num_seats-1]}): ")
        if input_seat.isalpha == False or input_seat=="":
            error_message += "Seat letter should be the alphabet"
        elif len(input_seat) != 1:
            error_message += "Seat letter should have only one character"
        elif upper_list.index(input_seat.upper()) > num_seats-1:
            error_message += f"Seat letter should be between A and {upper_list[num_seats-1]}"
        else:
            req_col = upper_list.index(input_seat.upper())
        
        if error_message == "":
            print(f"Reservation request converted: ({req_row}, {req_col})")
            return req_row, req_col
        else:
            print(f"\n{error_message}\n")
            return req_row, req_col
        

def reserve(seats, req_row, req_col):
    upper_list = list(ascii_uppercase)
    status_seat = seats[req_row][req_col]
    if status_seat == BOOKED:
        print(f"\nSeat {req_row}{upper_list[req_col]} is not available\n")
        show_table(seats, len(seats[0]), upper_list)
    elif status_seat == AVAIL:
        seats[req_row][req_col] = BOOKED
        print(f"\nSeat {req_row}{upper_list[req_col]} booked.\n")
        show_table(seats, len(seats[0]), upper_list)


def reset_table(seats):
    # Didn't get the point. Due to the name is called "reset", we shouldn't use this function to initialize the seats
    # but there's no way to reset the table if we follow the instruction, so I don't know when will this function be called
    pass  

if __name__ == "__main__":
    AVAIL  = "-"
    BOOKED = "X"
    main()