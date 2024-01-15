#!/usr/bin/python3
""" Console """

import cmd

class HBNBCommand(cmd.Cmd):
    """ Console """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program"""
        return True

    def emptyline(self):
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
