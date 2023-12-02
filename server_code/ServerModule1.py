import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def SUBMIT(name,company_name,address,mobile_number,email_id,requirement):
  app_table.meet.add_row(name=name,company_name=company_name,address=address,number=number,email_id=email_id,requirement=requirement)

