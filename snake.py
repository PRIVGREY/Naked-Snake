
def fuck():
    print ('fuck the world!')

def roc(date):

    #This function transform datetime object to R.O.C year string

    year = str(int(date.strftime('%Y')) - 1911)
    return year


