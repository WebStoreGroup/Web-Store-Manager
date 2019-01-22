# TODO 

# Create permissions for if authenticated or read only, then allow to POST / PUT (create transactions)
# Create permissions for if owner of the transaction, then allow to GET and 
    # Idea: if request.header.ID == customer.auth_id
# Create permissions for if admin, then allow to GET, PATCH
    # Idea: set auth_id for admin, set it on ENV, check if request.header.ID == admin.auth_id