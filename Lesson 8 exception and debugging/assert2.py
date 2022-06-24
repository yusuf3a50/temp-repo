assert (1==2, "This should fail")

# if you run this in python with a -O flag 
# it will turn off assert, thus not throwing 
# an exception

# When an exception is raised, it must
# either be handled immediately,
# otherwise it breaks the flow,
# terminates and quits .