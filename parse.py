import imaplib
import getpass
imap = imaplib.IMAP4_SSL('imap.yandex.ru')
imap.login('FilyaKert@yandex.ru',getpass.getpass())