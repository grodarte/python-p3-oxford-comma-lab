def oxford_comma(items):
    # joins items with a comma
    # also inserts and before the last item
    if len(items) < 3:
        return " and ".join(items)
    else:
        last_word = items.pop(-1)
        ox_sent = ", ".join(items)
        ox_sent += f", and {last_word}"
        return ox_sent


        

