#------------------------------ imports --------------------------------

# standard modules
from getpass import getpass

# intra-project modules
from browsers import WFBrowser

# external libraries
# N/A

#-----------------------------------------------------------------------


def main():
    """Downloads all account exports with the input account info."""

    # get login details from terminal
    username = raw_input('username: ')
    password = getpass('password: ')

    # create a driver for Wells Fargo
    with WFBrowser() as browser:

        # go to wellsfargo.com and login
        browser.nav_home()
        browser.login(username, password)

        # go to the download activity page, and download the account exports
        browser.nav_to_download_page()
        browser.download_all_accounts()

        # give some extra time in case Firefox makes download alerts
        browser.wait()


if __name__ == "__main__":
    main()