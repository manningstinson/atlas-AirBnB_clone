import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()
        self.held_output = StringIO()

    def tearDown(self):
        self.held_output.close()
        
    def test_do_create(self):
        with patch('sys.stdout', self.held_output):
        self.console.onecmd("create BaseModel")
        output = self.held_output.getvalue().strip()
        print("Output:", output)  # Add this line for debugging
        self.assertTrue(output.isalnum())


    def test_do_show(self):
        with patch('sys.stdout', self.held_output):
            self.console.onecmd("create BaseModel")
            created_output = self.held_output.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(created_output))
            output = self.held_output.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_do_destroy(self):
        with patch('sys.stdout', self.held_output):
            self.console.onecmd("create BaseModel")
            created_output = self.held_output.getvalue().strip()
            self.console.onecmd("destroy BaseModel {}".format(created_output))
            self.console.onecmd("show BaseModel {}".format(created_output))
            output = self.held_output.getvalue().strip()
            self.assertIn("** no instance found **", output)

    def test_do_all(self):
        with patch('sys.stdout', self.held_output):
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all")
            output = self.held_output.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_do_update(self):
        with patch('sys.stdout', self.held_output):
            self.console.onecmd("create BaseModel")
            created_output = self.held_output.getvalue().strip()
            self.console.onecmd("update BaseModel {} name 'new_name'".format(created_output))
            self.console.onecmd("show BaseModel {}".format(created_output))
            output = self.held_output.getvalue().strip()
            self.assertIn("'new_name'", output)

    def test_do_quit(self):
        with patch('sys.stdout', self.held_output):
            self.assertTrue(self.console.onecmd("quit"))

    def test_do_EOF(self):
        with patch('sys.stdout', self.held_output):
            self.assertTrue(self.console.onecmd("EOF"))

if __name__ == '__main__':
    unittest.main()