import csv
from optparse import OptionParser

# Paths to the files
LICENSE_FNAME = ''
OWNER_FNAME = ''

# license data
LICENSE_ID = 1
ACCOUNT_NUMBER_license = 2

# business owner data
ACCOUNT_NUMBER_owner = 0
LEGAL_NAME = 1
OWNER_FIRST_NAME = 2
OWNER_LAST_NAME = 3
TITLE = 7


def read_file(fname):
    '''
    Read in a file given the file name
    
    Parameters
    ----------
    fname : str
        path to the file 
        
    Returns
    -------
    content: list
        a list of strings

    '''
    content = []

    return content


def get_owners(owners, acnt_num):
    '''
    Find a list of owners associated with an account number given the a file of business owners and an account number
    
    Parameters
    ----------
    owners : a list of string
        an list of entries from Business_Owners.csv
    
    acnt_num: the account number searched for
    
    Returns
    -------
    owner_titles: a list of tuple
        a list of (full name, title) tuple pairs associated with the account number
    '''
    
    owner_titles = []

    return owner_titles


def get_license(licenses, acnt_num):
    
    '''
    Find a list of business licenses associated with an account number 
    given the a file of business licenses and an account number
    
    Parameters
    ----------
    licenses : a list of string
        an list of entries from Business_Licenses.csv
    
    acnt_num: the account number searched for
    
    Returns
    -------
    owner_titles: a list of string
        a list of license IDs associated with the account number
    '''
    
    license_ids = []

    return license_ids


def main():
    '''
        DO NOT MODIFY THE MAIN FUNCTION
    '''
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-a", "--account", dest="account")
    (options, args) = parser.parse_args()

    if len(vars(options)) > 1:
        parser.error("Incorrect number of arguments.")
        return
    else:
        print("Searching...")
        licenses = read_file(LICENSE_FNAME)
        owners = read_file(OWNER_FIRST_NAME)
        account_num = options.account
        license_ids = get_license(licenses, account_num)
        owner_titles = get_owners(owners, account_num)
        if len(license_ids):
            print(license_ids)
        else:
            print("No license ids associated with the account number")
        if len(owner_titles):
            print(owner_titles)
        else:
            print("No business owners associated with the account number")


if __name__ == "__main__":
    main()