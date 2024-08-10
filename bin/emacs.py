import sys

from abbr import load

abbr = load(sys.argv[1])

print("""
(define-abbrev-table 'apropos-mode-abbrev-table '(
    ))

(define-abbrev-table 'occur-mode-abbrev-table '(
    ))

(define-abbrev-table 'text-mode-abbrev-table '(
    ))

(define-abbrev-table 'lisp-interaction-mode-abbrev-table '(
    ))

(define-abbrev-table 'emacs-lisp-mode-abbrev-table '(
    ))

(define-abbrev-table 'lisp-mode-abbrev-table '(
    ))

(define-abbrev-table 'fundamental-mode-abbrev-table '(
    ))

(define-abbrev-table 'global-abbrev-table '(
""")

for k, v in sorted(abbr.items()):
    print("""    ("%s" "%s" nil 0)""" % (k, v))

print("    ))")
